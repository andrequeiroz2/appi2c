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
    last_command = db.Column('last_command', db.String(60))
    last_date = db.Column('last_date', db.String(60))
    prefix = db.Column('prefix', db.String(10))
    postfix = db.Column('postfix', db.String(10))
    qos = db.Column('qos', db.Integer, nullable=False)
    retained = db.Column("retained", db.String(5), default='True')
    type_device = db.Column('type', db.String(60), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False) 
    group_id = db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False) 

    def __repr__(self):
        return f"Device('{self.name}',\
                        '{self.topic_pub}',\
                        '{self.topic_pub}',\
                        '{self.last_will_topic}',\
                        '{self.qos}',\
                        '{self.retained}')"
