from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import (Required, Length, Email, ValidationError,
                                EqualTo)
from app.models import User


class Unique(object):

    '''
    Custom validator to check an object's attribute
    is unique. For example users should not be able
    to create an account if the account's email
    address is already in the database. This class
    supposes you are using SQLAlchemy to query the
    database.
    '''

    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class Forgot(Form):

    ''' User forgot password form. '''

    email = TextField(validators=[Required(), Email()],
                      description='Email address')


class Reset(Form):

    ''' User reset password form. '''

    password = PasswordField(validators=[
        Required(), Length(min=6),
        EqualTo('confirm', message='Passwords must match.')
    ], description='Password')
    confirm = PasswordField(description='Confirm password')


class Login(Form):

    ''' User login form. '''

    email = TextField(validators=[Required(), Email()],
                      description='Email address')
    password = PasswordField(validators=[Required()],
                             description='Password')

def clinician_keys(form, field):
        keys = "679c618bb9b13"
        if (field.data==keys):
            return True
        else:
            raise ValidationError('Incorrect Clinician Key')

class SignUp(Form):
    ''' User sign up form. '''

    clinician_key = TextField(validators=[Required(), clinician_keys],description='Clinician Key')


    first_name = TextField(validators=[Required(), Length(min=2)],
                     description='Patient Name')
    last_name = TextField(validators=[Required(), Length(min=2)],
                        description='Patient Surname')
    phone = TextField(validators=[Required(), Length(min=6)],
                      description='Patient Phone number')
    email = TextField(validators=[Required(), Email(),
                                  Unique(User, User.email,
                                         'This email address is ' +
                                         'already linked to an account.')],
                      description='Patient Chosen Email Address')
    password = PasswordField(validators=[
        Required(), Length(min=6),
        EqualTo('confirm', message='Passwords must match.')
    ], description='Patient Chosen Password')
    confirm = PasswordField(description='Confirm Patient Chosen Password')

class Measurements(Form):

    age = TextField(validators=[Required(), Length(min=1)],
                      description='eg. 34')
                      
    heart_rate = TextField(validators=[Required(), Length(min=1)],
                     description='BPM')

    weight = TextField(validators=[Required(), Length(min=1)],
                     description='KG')
    blood_pressure = TextField(validators=[Required(), Length(min=1)],
                     description='mm Hg')