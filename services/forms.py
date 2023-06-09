from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField, SelectMultipleField


class UserBaseForm(FlaskForm):
    username = StringField(
        'username',
        [validators.DataRequired()],
    )
    email = StringField(
        'Email Address',
        [
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )
    first_name = StringField('First Name')
    last_name = StringField('Last Name')


class RegistrationForm(UserBaseForm):
    password = PasswordField(
        'New Password',
        [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Passwords must match'),
        ],
    )
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField(
        'username',
        [validators.DataRequired()],
    )
    password = PasswordField(
        'Password',
        [validators.DataRequired()],
    )
    submit = SubmitField('Login')


class CreateArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Create')
