from appi2c.ext.database import db


class Group(db.Model):
    __tablename__ = "group"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(60), nullable=False)
    description = db.Column("description", db.String(100), nullable=False)
    file = db.Column("file_name", db.String(120))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    devices = db.relationship('Device', backref='group', lazy=True)
    def __repr__(self):
        return f"Group('{self.name}')"
