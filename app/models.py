from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin

   

from app import db, bcrypt


class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    _password = db.Column(db.String)
    confirmation = db.Column(db.Boolean)
    

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email

class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(100), nullable=False)
    heart_rate = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.String(100), nullable=False)
    blood_pressure = db.Column(db.String(100), nullable=False)
    

    def __repr__(self):
        return f"m('{self.age}', '{self.heart_rate}','{self.weight}','{self.blood_pressure}')"

'''



class Measurements(db.Model):

    __tablename__ = 'measurements'

    age = db.Column(db.String)
    heart_rate = db.Column(db.String)
    weight = db.Column(db.String)
    blood_pressure = db.Column(db.String)

    def __repr__(self):
        return f"Measurements('{self.title}', '{self.date_posted}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"




'''