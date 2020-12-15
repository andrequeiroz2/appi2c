from appi2c.ext.mqtt.mqtt_routes import bp
from appi2c.ext.admin import admin
from appi2c.ext.database import db 
from appi2c.ext.mqtt.mqtt_models import ClientMqtt
from appi2c.ext.mqtt.mqtt_admin import MqttAdmin


def init_app(app):
    app.register_blueprint(bp)
    admin.add_view(MqttAdmin(ClientMqtt, db.session))
