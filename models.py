from base_user import BaseUser
from __init__ import db

class Assets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    asset_name = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(300))
    serial_no = db.Column(db.String(10))
    serial_code = db.Column(db.String(10))
    colour = db.Column(db.String(10))
    date_bought = db.Column(db.String(10)) #yyyy-mm-dd format

    def __repr__(self):
        return "<Asset '{}': '{}' >".format(self.name, self.serial_code)

class Admins(db.Model, BaseUser):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String)

    @staticmethod
    def get_by_username(username):
        return Admins.query.filter_by(username=username).first()


class User(db.Model, BaseUser):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

class Cases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_description = db.Column(db.String(300))
    case_item = db.Column(db.String(10))
    case_type = db.Column(db.String(10))

    def __repr__(self):
        return '<Case: %r>' %self.case_type
