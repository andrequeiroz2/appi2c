from appi2c.ext.auth.auth_models import User
from appi2c.ext.encrypt import bcrypt
from appi2c.ext.database import db


def create_user(username: str, email: str, password: str, admin:bool=False) -> User:
    user = User(username=username, email=email, password=password, admin=admin)
    db.session.add(user)
    db.session.commit()
    return user


def login_check_user(username: str) -> User:
    user = User.query.filter_by(username=username).first()
    return user


def login_check_password_hash(user_password: str, form_password: str) -> User:
    password_hash = bcrypt.check_password_hash(pw_hash=user_password, password=form_password)
    return password_hash


def session_commit():
    db.session.commit()


def update_profile(user: User, username: str, email: str, password: str) -> User:
    User.query.filter_by(username=user.username).update(dict(username=username, email=email, password=password))
    print(User.groups)
    db.session.commit()


def num_user():
    user = User.query.all()
    num_user = len(user)
    return num_user
