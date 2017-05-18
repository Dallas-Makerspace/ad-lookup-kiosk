from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# class LoginForm(Form):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)

class IndexForm(Form):
    member_id = StringField('member_id', validators=[DataRequired()])
    # member_id = StringField('memberid', validators=[DataRequired()])
    # remember_me = BooleanField('remember_me', default=False)
