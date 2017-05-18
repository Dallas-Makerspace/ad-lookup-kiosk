from flask import render_template, flash, redirect, request, url_for, session
from app import app
import os
import requests
import json
from wtforms import TextField
from .forms import IndexForm
from .forms import MemberNotFoundForm
from .forms import RegisterToVoteForm
from .emails import send_email
from .emails import send_email_request_voting_rights

@app.before_request
def session_management():
    # make the session last indefinitely until it is cleared
    session.permanent = True

@app.route('/', methods=['GET', 'POST'])
def index():
    # reset the session data
    session.clear()
    form  = IndexForm()
    if request.method == 'POST':
        # if form.validate_on_submit():
        # return redirect('/member/0003343095')
        return redirect('/member/'+ str(form.member_id))

    return render_template('index.html',
                           title='Home',
                           form=form)


@app.route('/member/<member_id>')
def dms(member_id):
    # return render_template('member-not-found.html')
    url = "http://192.168.200.130:8080/api/v1/lookupByRfid"
    payload = "rfid=" + member_id
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    details = json.loads(response.text)

    # Did the request return a member's record
    if 'user' in details['result']:
        #Store member data in session for future use
        session['member_id'] = member_id
        session['fullname'] = details['result']['user']['fullName']
        session['username'] = details['result']['user']['username']
        session['email'] = details['result']['user']['email']

        #Process AD groups for display in two columns
        # Create new list of AD groups
        ad_group = []
        ad_group_1 = [] #left column
        ad_group_2 = [] #right column
        for element in details['result']['user']['groups']:
            ad_group.append(str(element))
        #Get the total number of items
        count = len(ad_group)
        half = count//2
        remainder = count%2
        #Grab voting rights from list and add to details[]
        voting_rights_label = "Voting Members"
        if voting_rights_label in ad_group:
            details['result']['user']['votingMember'] = "Yes"


        #Process half of the list plus extra item( if odd remainder)
        if remainder > 0:
            length = half + 1
            #process first list(left column)
            ad_group_1 = ad_group[0:length]
            #Process second list(right column)
            ad_group_2 = ad_group[length+1:count]
        else:
            length = half + 0  # Just to help you incase
            #process first list(left column)
            ad_group_1 = ad_group[0:length]
            #Process second list(right column)
            ad_group_2 = ad_group[length+1:count]


        return render_template('member-details.html', details=details, ad_group_1=ad_group_1, ad_group_2=ad_group_2)
    else:
        return redirect(url_for('member_not_found'))

@app.route('/register-to-vote/<details>', methods=['GET', 'POST'])
def register_to_vote(details):
    form = RegisterToVoteForm()
    # contact = details['result']['user']['username'] + details['result']['user']['email']

    if form.validate_on_submit():
        if form.register.data:
            flash('Please check your email and respond.')
            send_email_request_voting_rights()
        elif form.cancel.data:
            flash('You have not requested voting rights.')
        # flash('Login requested for OpenID="%s"' %
        #       (form.member_id))

        return redirect(url_for('index'))

    return render_template('register-to-vote.html', form=form, details=details)

@app.route('/member-not-found', methods=['GET', 'POST'])
def member_not_found():
    form=MemberNotFoundForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('member-not-found.html',
                                        form=form)


@app.route('/test-good')
def test_good():
    # Load local json test file
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "member-sample.json")
    #load static test file
    response = json.load(open(json_url))
    details = response



    member_id = 1233445556
    #Store member data in session for future use
    session['member_id'] = member_id
    session['fullname'] = details['result']['user']['fullName']
    session['username'] = details['result']['user']['username']
    session['email'] = details['result']['user']['email']

    #Process AD groups for display in two columns
    # Create new list of AD groups
    ad_group = []
    ad_group_1 = [] #left column
    ad_group_2 = [] #right column
    for element in details['result']['user']['groups']:
        ad_group.append(str(element))
    #Get the total number of items
    count = len(ad_group)
    half = count//2
    remainder = count%2
    #Process half of the list plus extra item( if odd remainder)
    if remainder > 0:
        length = half + 1
        #process first list(left column)
        ad_group_1 = ad_group[0:length]
        #Process second list(right column)
        ad_group_2 = ad_group[length+1:count]
    else:
        length = half + 0  # Just to help you incase
        #process first list(left column)
        ad_group_1 = ad_group[0:length]
        #Process second list(right column)
        ad_group_2 = ad_group[length+1:count]

    #Get count of items
    return render_template('member-details.html',
                               details=details, ad_group_1=ad_group_1, ad_group_2=ad_group_2)

@app.route('/test-bad', methods=['GET', 'POST'])
def test_bad():
    form = MemberNotFoundForm()
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('member-not-found.html',
                                        form=form)
