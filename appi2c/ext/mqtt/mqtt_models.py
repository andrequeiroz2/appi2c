from appi2c.ext.database import db


class ClientMqtt(db.Model):
    __tablename__ = "client_mqtt"
    id = db.Column('id', db.Integer, primary_key=True)
    client_id = db.Column('client_id', db.String(60), nullable=False)
    name = db.Column('name', db.String(60), nullable=False)
    address_url = db.Column('address_url',db.String(120), nullable=False)
    port = db.Column('port', db.Integer, nullable=False)
    username = db.Column('username', db.String(20))
    password = db.Column('password', db.String(20))
    keep_alive = db.Column('keep_alive', db.Integer, default=60)

    last_will_topic = db.Column('last_will_topic', db.String(120), nullable=False)
    last_will_message = db.Column('last_will_message', db.String(120), nullable=False)
    last_will_qos = db.Column('last_will_qos', db.Integer, default=0)
    last_will_retain = db.Column('last_will_retain', db.Boolean, default=False)

    msg_online = db.Column('message_online', db.String(10), default='On-line', nullable=False)

    last_state = db.Column('last_state', db.String(120), default='Off-line')

    status = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Client MQTT('{self.name}',\
                             '{self.address_url}',\
                             '{self.port}',\
                             '{self.keep_alive}',\
                             '{self.status}')"
