from flask_mail import Message
# from config import ADMINS
from app import app, mail, session
from .decorators import async

# Called to send mail async
@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

def send_email_request_voting_rights():
        subject="Request Dallas Maker Space Membership Voting Rights"
        sender='accounts@dallasmakerspace.org'
        recipients=[session['email']]


        msg = Message(subject, sender=sender, recipients=recipients)
        text_body = "[DMS Member - Please reply to this email and you will be registered for voting rights.]\n\n"
        text_body = text_body + "As a member in good standing I am requesting voting rights"
        text_body = text_body + " for the upcoming board of director's election."
        text_body = text_body + "\n\nIf you don't receive confirmation of being registered within 72 hours please send this again."
        text_body = text_body + '\n\n ** This is request originated from the DMS Membership Portal. **'

        msg.body = text_body
        # msg.html = html_body
        send_async_email(app, msg)

def send_email_sample():
    send_email("[microblog] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template("follower_email.txt",
                               user=followed, follower=follower),
               render_template("follower_email.html",
                               user=followed, follower=follower))
