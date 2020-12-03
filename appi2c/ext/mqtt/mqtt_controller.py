from datetime import datetime
from appi2c.ext.database import db
from appi2c.ext.mqtt.mqtt_models import ClientMqtt
from appi2c.ext.mqtt.mqtt_connect import (connect,
                                          handle_disconnect,
                                          handle_publish)

def get_date():
    date_now = datetime.now()
    date_time_now = date_now.strftime('%d/%m/%Y %H:%M')
    return date_time_now


def create_client_mqtt(name: str,
                       client_id: str,
                       address_url: str,
                       port: int,
                       username: str = None,
                       password: str = None,
                       keep_alive: int = 60,
                       last_will_topic: str = None,
                       last_will_message: str = None,
                       last_will_qos: int = 0,
                       last_will_retain: bool = True,
                       status: bool = False):

    client = ClientMqtt(name=name,
                        client_id=client_id,
                        address_url=address_url,
                        port=port,
                        username=username,
                        password=password,
                        keep_alive=keep_alive,
                        last_will_topic=last_will_topic,
                        last_will_message=last_will_message,
                        last_will_qos=last_will_qos,
                        last_will_retain=last_will_retain,
                        status=status)
    db.session.add(client)
    db.session.commit()


def get_client_mqtt():
    client = ClientMqtt.query.filter_by(status=True).first()
    return client


def list_all_client_mqtt():
    client_mqtt = ClientMqtt.query.all()
    return client_mqtt


def list_client_mqtt_id(id: int):
    client_mqtt = ClientMqtt.query.filter_by(id=id).first()
    return client_mqtt


def delete_client_mqtt(id: int):
    client_mqtt = ClientMqtt.query.filter_by(id=id).first()
    if client_mqtt.status == 0:
        pass
    else:
        #todo: desconect client mqtt
        pass
    client_mqtt.delete()
    db.session.commit()


def activate_client_mqtt(client):
    client_is_activit = ClientMqtt.query.filter_by(status=True).first()
    if client_is_activit is None:
        connect(client)
        handle_publish(client.last_will_topic, client.msg_online, 1, True)
        client.status = True
        client.last_state = client.msg_online
        
    else:
        handle_disconnect()
        client_is_activit.status = False
        connect(client)
        handle_publish(client.last_will_topic, client.msg_online, 1, True)
        client.status = True
        client.last_state = client.msg_online
        
    db.session.commit()


def deactivate_client_mqtt(client):
    handle_publish(client.last_will_topic, client.last_will_message, 1, True)
    client.last_state = client.last_will_message
    handle_disconnect()
    client.status = False
    db.session.commit()


def reinitialise_client_mqtt(broker):
    if broker.status is True:
        #get_reinitialise(broker)
        ""
    else:
        pass


def num_broker():
    broker = ClientMqtt.query.all()
    num_broker = len(broker)
    return num_broker


def update_client_mqtt(id: int,
                       name: str,
                       address_url: str,
                       port: int,
                       username: str,
                       password: str,
                       keep_alive: int,
                       last_will_topic: str,
                       last_will_message: str,
                       last_will_qos: int,
                       last_will_retain: bool):
    ClientMqtt.query.filter_by(id=id).update(dict(
                                        name=name,
                                        address_url=address_url,
                                        port=port, username=username,
                                        password=password,
                                        keep_alive=keep_alive,
                                        last_will_topic=last_will_topic,
                                        last_will_message=last_will_message,
                                        last_will_qos=last_will_qos,
                                        last_will_retain=last_will_retain))
    db.session.commit()
