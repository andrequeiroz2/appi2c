#from flask import json
#from appi2c.ext.mqtt.mqtt_socketio import socketio
from flask import current_app
from flask_mqtt import Mqtt
import uuid


mqtt = Mqtt()
mqtt.client_id = 'appi2c-' + str(uuid.uuid4())


def connect(client):
    if client is None:
        pass
    else:
        current_app.config['MQTT_BROKER_URL'] = client.address_url
        current_app.config['MQTT_BROKER_PORT'] = client.port
        current_app.config['MQTT_USERNAME'] = client.username
        current_app.config['MQTT_PASSWORD'] = client.password
        current_app.config['MQTT_KEEPALIVE'] = client.keep_alive
        current_app.config['MQTT_LAST_WILL_TOPIC'] = client.last_will_topic
        current_app.config['MQTT_LAST_WILL_MESSAGE'] = client.last_will_message
        current_app.config['MQTT_LAST_WILL_QOS'] = client.last_will_qos
        if client.last_will_retain == 'True':
            current_app.config['MQTT_LAST_WILL_RETAIN'] = True
        else:
            current_app.config['MQTT_LAST_WILL_RETAIN'] = False
        mqtt.init_app(current_app)


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    print('===On Msg===')
    print('Client: ', client)
    print('User: ', userdata)
    print('Topic: ', message.topic)
    print('Payload: ', message.payload.decode())
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print("===ON LOG===")
    print('Client: ', client)
    print('User: ', userdata)
    print('Level: ', level)
    print('Buf: ', buf)


@mqtt.on_disconnect()
def handle_disconnect():
    mqtt._disconnect()


def handle_publish(topic, msg, qos, retain):
    mqtt.publish(topic, msg, qos)