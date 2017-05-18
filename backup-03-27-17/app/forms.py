from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired

# class LoginForm(Form):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)

class IndexForm(Form):
    member_id = StringField('member_id', validators=[DataRequired()])
    # member_id = StringField('memberid', validators=[DataRequired()])
    # remember_me = BooleanField('remember_me', default=False)

    # Complex validation
    # http://flask.pocoo.org/snippets/64/

    # def __init__(self, *args, **kwargs):
    #     Form.__init__(self, *args, **kwargs)
    #
    #     self.user = None
    #
    # def validate(self):
    #     rv = Form.validate(self)
    #     if not rv:
    #         return False
    #
    #     user = User.query.filter_by(
    #         username=self.username.data).first()
    #
    #     if user is None:
    #         self.username.errors.append('Unknown username')
    #         return False
    #
    #     if not user.check_password(self.password.data):
    #         self.password.errors.append('Invalid password')
    #         return False
    #
    #     self.user = user
    #     return True

class RegisterToVoteForm(Form):
    hidden = HiddenField()

    register = SubmitField(label='Send My Registration Email')
    cancel = SubmitField(label='Cancel Voting Request')


class NotFoundForm(Form):
    member_id = StringField('member_id', validators=[DataRequired()])
