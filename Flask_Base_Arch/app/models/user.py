from datetime import datetime
import bcrypt
from Flask_Base_Arch.app import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    created_by = db.Column(db.BIGINT, nullable=True)
    modified_at = db.Column(db.DateTime, nullable=True)
    modified_by = db.Column(db.BIGINT, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    deleted_by = db.Column(db.BIGINT, nullable=True)

    def __init__(self, email, usename, password, name):
        self.email = email
        self.username = usename
        self.password = bcrypt.hashpw(
            password.encode('utf8'), bcrypt.gensalt())
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active
