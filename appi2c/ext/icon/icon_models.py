from appi2c.ext.database import db
from appi2c.ext.device.device_models import Device


class Icon(db.Model):
    __tablename__ = "icon"
    id = db.Column('id', db.Integer, primary_key=True)
    html_class = db.Column('html_class', db.String(60), nullable=False)
    devices = db.relationship('Device', backref='icon', lazy=True)

    def __repr__(self):
        return f"'{self.html_class}'"

    def validate_html_class(self, key, html_class):
        if not html_class:
            raise AssertionError('No name provided')
        if Icon.query.filter(Icon.html_class == html_class).first():
            raise AssertionError('Icon is already in use')
