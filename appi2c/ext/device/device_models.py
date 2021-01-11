from appi2c.ext.database import db


class Device(db.Model):
    __tablename__ = "device"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(60), nullable=False)
    topic_pub = db.Column('topic_pub', db.String(120))
    topic_sub = db.Column('topic_sub', db.String(120))
    last_will_topic = db.Column('last_will_topic', db.String(60))
    command_on = db.Column('command_on', db.String(60))
    command_off = db.Column('command_off', db.String(60))
    measure = db.Column('measure', db.String(60))
    last_command = db.Column('last_command', db.String(60))
    last_date = db.Column('last_date', db.DateTime, nullable=False)
    last_data = db.Column('last_data', db.String(120))
    postfix = db.Column('postfix', db.String(10))
    qos = db.Column('qos', db.Integer, nullable=False)
    retained = db.Column("retained", db.Boolean, default=True)
    position_left = db.Column('position_left', db.String(120))
    position_top = db.Column('position_top', db.String(120))
    type_id = db.Column('type_id', db.Integer, db.ForeignKey('device_type.id'), nullable=False)
    icon_id = db.Column('icon_id', db.Integer, db.ForeignKey('icon.id'), nullable=False)
    group_id = db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.relationship('Data', backref='data_device', lazy=True)
    limit = db.relationship('Limit', backref='limit_device', lazy=True)

    def __repr__(self):
        return f"Device('{self.name}',\
                        '{self.topic_pub}',\
                        '{self.topic_pub}',\
                        '{self.last_will_topic}',\
                        '{self.qos}',\
                        '{self.retained}')"


class DeviceType(db.Model):
    __tablename__ = "device_type"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(60))
    devices = db.relationship('Device', backref='device', lazy=True)

    def __repr__(self):
        return f"('{self.name}')"

    def validate_name(self, key, name):
        if not name:
            raise AssertionError('No name provided')
        if DeviceType.query.filter_by(DeviceType.name == name).first():
            raise AssertionError('Name is already in use')

    @property
    def serialize(self):
        return {"name": self.name}


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(60))
    date_time = db.Column('date_time', db.DateTime, nullable=False)
    device_id = db.Column('device_id', db.Integer, db.ForeignKey('device.id'), nullable=False)

    def __repr__(self):
        return f'{self.data, self.date_time}'


class Limit(db.Model):
    __tablename__ = "limit"
    id = db.Column('id', db.Integer, primary_key=True)
    limit_max = db.Column('limit_max', db.Integer)
    limit_min = db.Column('limit_min', db.Integer)
    level = db.Column('level', db.String(60))
    date_time = db.Column('date_time', db.DateTime)
    device_id = db.Column('device_id', db.Integer, db.ForeignKey('device.id'), nullable=False)
    notifier_id = db.Column('notifier_id', db.Integer, db.ForeignKey('notifier.id'), nullable=False)

    def __repr__(self):
        return f'{self.limit_max, self.limit_min, self.level, self.date_time, self.device_id, self.notifier_id}'
