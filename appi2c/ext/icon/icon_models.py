from appi2c.ext.database import db


class Icon(db.Model):
    __tablename__ = "icon"
    id = db.Column('id', db.Integer, primary_key=True)
    html_class = db.Column('html_class', db.String(60), nullable=False)
    deviceType_id = db.Column('deviceType_id', db.Integer, db.ForeignKey('device_type.id'), nullable=False)
