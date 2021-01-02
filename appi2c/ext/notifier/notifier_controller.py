from appi2c.ext.database import db
from appi2c.ext.notifier.notifier_models import Notifier


def create_notifier(name: str, token: str, chat_id: str, user_id: int):
    notifier = Notifier(name=name, token=token, chat_id=chat_id, user_id=user_id)
    db.session.add(notifier)
    db.session.commit()


def list_all_notifier(user) -> Notifier:
    notifier = user.notifiers
    return notifier


def list_notifier_id(id: int) -> Notifier:
    notifier = Notifier.query.filter_by(id=id).first()
    return notifier


def update_notifier(id: int, name: str, token: str, chat_id: str):
    Notifier.query.filter_by(id=id).update(dict(name=name, token=token, chat_id=chat_id))
    db.session.commit()


def delete_notifier_id(id: int):
    notifier = Notifier.query.filter_by(id=id).first()
    db.session.delete(notifier)
    db.session.commit()