import paho.mqtt.client as mqtt
import logging
import uuid


#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

client_id = 'appi2c' + str(uuid.uuid4())
client_connect = mqtt.Client(client_id)

flag_log = False
flag_conn = False
mgs = None


def on_log(client, userdata, level, buf):
    print("============On Log============")
    if 'Connection failed' in buf:
        flag_log = False
    else:
        flag_log = True
    return flag_log


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("============On Conn============")
        print('Connection successful')
        msg = 'Connection Result: ', rc, '\n Connection successful'
        flag_conn = True
    elif rc == 1:
        print("============On Conn============")
        print('Connection refused - incorrect protocol')
        msg = 'Connection Result: ', rc, '\n Connection refused - incorrect protocol'
        flag_conn = False
    elif rc == 2:
        print("============On Conn============")
        print('Connection refused - invalid client identifier')
        msg = 'Connection Result: ', rc, '\n Connection refused - invalid client identifier'
        flag_conn = False
    elif rc == 3:
        print("============On Conn============")
        print('Connection refused - server unavailable')
        msg = 'Connection Result: ', rc, '\n Connection refused - server unavailable'
        flag_conn = False
    elif rc == 4:
        print("============On Conn============")
        print('Connection refused - bad username or password')
        msg = 'Connection Result: ', rc, '\n Connection refused - bad username or password'
        flag_conn = False
    else:
        print("============On Conn============")
        print('Connection refused - not authorised 6-255: Currently unused')
        msg = 'Connection Result: ', rc, '\n Connection refused - not authorised 6-255: Currently unused'
        flag_conn = False
    return (msg, flag_conn)


def on_message(client, userdata, message, rc):
    print("============On Message============")
    print('Client:', client)
    print('Userdata:', userdata)
    print("Received Message: ", str(message.payload.decode("utf-8")))
    print("Connection Returned Result: ", rc)
    print("==================================")


def get_connect(client):
    get_will_set(client_connect,
                 client.last_will_topic,
                 client.last_will_message,
                 client.last_will_qos,
                 client.last_will_retain)

    if client.username is None:
        pass
    else:
        if client.password is None:
            client_connect.username_pw_set(username=client.username, password=None)
        else:
            client_connect.username_pw_set(username=client.username, password=client.password)

    client_connect.connect_async(client.address_url,
                                 client.port,
                                 client.keep_alive)

    get_on_line(client)

    client_connect.on_log = on_log
    client_connect.on_connect = on_connect
    client_connect.on_message = on_message
    client_connect.loop_start()


def get_on_line(client):
    topic = client.last_will_topic
    payload = 'on-line'
    qos = 1
    client_publish(topic, payload, qos, retain=True)


def get_will_set(client, topic, payload, qos, retain):
    client.will_set(topic=topic, payload=payload, qos=qos, retain=retain)


def get_disconect():
    client_connect.loop_stop()
    client_connect.disconnect()


def get_reinitialise():
    client_connect.reinitialise()


def client_publish(topic, payload: str, qos: int, retain: bool):
    client_connect.publish(topic=topic, payload=payload, qos=qos, retain=retain)


def client_subscrib(topic: str, qos: int):
    client_connect.subscribe(topic, qos)
