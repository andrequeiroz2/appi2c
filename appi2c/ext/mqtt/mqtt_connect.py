from appi2c.ext.database import db
from appi2c.ext.socketio import socketio
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
    print('Topic: ', message.topic)
    print('Payload: ', message.payload.decode())
    topic = message.topic
    data = dict(topic=message.topic, payload=message.payload.decode(), qos=message.qos)
    socketio.emit(topic, data)

    from appi2c.ext.device.device_controller import get_data
    get_data(topic=topic, payload=message.payload.decode())


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


@mqtt.on_publish()
def handle_publish(topic: str, payload: str, qos: int, retain: bool):
    mqtt.publish(topic=topic, payload=payload, qos=qos, retain=retain)


@socketio.on('subscribe')
def handle_subscribe(topic: str, qos: int):
    print('Device Sub Topic: ', topic)
    mqtt.subscribe(topic=topic, qos=qos)
