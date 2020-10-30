#import paho.mqtt.client as mqtt
from appi2c.ext.mqtt.mqtt_connect import connect, handle_disconnect
import uuid
from appi2c.ext.mqtt.mqtt_models import ClientMqtt
from appi2c.ext.database import db


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


#def activate_client_mqtt(client):
#    client_is_activit = ClientMqtt.query.filter_by(status=True).first()
#    if client_is_activit is None:
#        client.status = True
#    else:
#        client_is_activit.status = False
#        client.status = True
#    get_connect(client)
#    db.session.commit()


def activate_client_mqtt(client):
    client_is_activit = ClientMqtt.query.filter_by(status=True).first()
    if client_is_activit is None:
        connect(client)
        client.status = True
    else:
        handle_disconnect()
        client_is_activit.status = False
        connect(client)
        client.status = True
    db.session.commit()


def deactivate_client_mqtt(client):
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

#==========Paho MQTT===================#

#logging.basicConfig(level=logging.DEBUG)
#client_id = 'appi2c' + str(uuid.uuid4())
#client_connect = mqtt.Client(client_id)


#==============Logs====================#


#def on_log(client, userdata, level, buf):
#    print("============On Log============")
#    print('Buf:', buf)


#def on_connect(client, userdata, flags, rc):
#    print("============On Connect============")
#    #print("Result from connect: {}".format(mqtt.connack_string(rc)))


#def on_message(client, userdata, message, rc):
#    print("============On Message============")
#    print('Client:', client)
#    print('Userdata:', userdata)
#    print("Received Message: ", str(message.payload.decode("utf-8")))
#    print("Connection Returned Result: ", rc)
#    print("==================================")


#def get_connect(client):

    #get_will_set(client_connect,
    #             client.last_will_topic,
    #             client.last_will_message,
    #             client.last_will_qos,
    #            client.last_will_retain)

    #if client.username is None:
    #    pass
    #else:
    #    if client.password is None:
    #        client_connect.username_pw_set(username=client.username, password=None)
    #    else:
    #        client_connect.username_pw_set(username=client.username, password=client.password)

    #client_connect.on_log = on_log
    #client_connect.on_connect = on_connect

    #client_connect.connect_async(client.address_url,
    #                             client.port,
    #                             client.keep_alive)

    #client_connect.on_log = on_log
    #client_connect.on_connect = on_connect
    #client_connect.on_message = on_message
    #get_on_line(client)
    #client_connect.loop_start()


#def get_on_line(client):
#    topic = client.last_will_topic
#    payload = 'on-line'
#    qos = 1
#    client_publish(topic, payload, qos, retain=True)


#def get_will_set(client, topic, payload, qos, retain=True):
#    client.will_set(topic=topic, payload=payload, qos=qos, retain=retain)


#def get_disconect():
#    client_connect.disconnect()
#    client_connect.loop_stop()


#def get_reinitialise():
#    client_connect.reinitialise()


#def client_publish(topic, payload: str, qos: int, retain: bool):
#    client_connect.publish(topic=topic, payload=payload, qos=qos, retain=retain)


#def client_subscrib(topic: str, qos: int):
#    client_connect.subscribe(topic, qos)