from appi2c.ext.database import db


class Notifier(db.Model):
    __tablename__ = "notifier"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(120), index=True, nullable=False)
    token = db.Column("token", db.String(120), index=True, nullable=False)
    chat_id = db.Column("chat_id", db.String(120), index=True, nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Notifier('{self.name}')"
