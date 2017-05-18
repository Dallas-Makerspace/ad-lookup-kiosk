from flask import render_template, flash, redirect
from app import app
import os
import requests
import json
from wtforms import TextField
from .forms import IndexForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s"' %
              (form.member_id))
        return redirect('/member-details/'+ str(form.member_id))
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/member-details/<member_id>')
def dms(member_id):
    url = "http://192.168.200.130:8080/api/v1/lookupByRfid"
    payload = "rfid=" + member_id
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    details = json.loads(response.text)
    if 'user' in details['result']:
        return render_template('member-details.html',
                                   details=details)

    return render_template('member-not-found.html')

@app.route('/test-good')
def test_good():
    # Load local json test file
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "member-sample.json")
    #load static test file
    response = json.load(open(json_url))
    # details = json.loads(response)
    return render_template('member-details.html',
                               details=response)

@app.route('/test-bad')
def test_bad():
    # Load local json test file
    return render_template('member-not-found.html')
