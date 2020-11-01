from flask import (Blueprint,
                   render_template,
                   url_for,
                   flash,
                   redirect,
                   request)
from appi2c.ext.mqtt.mqtt_forms import MqttClientForm, EditMqttForm
from appi2c.ext.mqtt.mqtt_controller import (create_client_mqtt,
                                             deactivate_client_mqtt,
                                             list_all_client_mqtt,
                                             list_client_mqtt_id,
                                             activate_client_mqtt,
                                             update_client_mqtt,
                                             reinitialise_client_mqtt)
from appi2c.ext.encrypt import bcrypt
import time


t = int(time.time())
t = str(t)

bp = Blueprint('mqtt', __name__, template_folder='appi2c/templates/mqtt')


@bp.route("/aboult/mqtt")
def aboult_mqtt():
    return render_template('mqtt/mqtt_aboult.html')


@bp.route("/register/mqtt", methods=['GET', 'POST'])
def register_mqtt():
    form = MqttClientForm()
    if form.validate_on_submit():

        #if not form.password.data:
        #    hash_password = form.password.data
        #else:
        #    hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #print(form.last_will_topic)

        if form.last_will_topic is None:
            retain = False
        else:
            if form.last_will_retain.data == 'True':
                retain = True
            else:
                retain = False

        create_client_mqtt(
                name=form.name.data,
                client_id=form.name.data+t,
                address_url=form.address_url.data,
                port=form.port.data,
                username=form.username.data,
                password=form.password.data,
                keep_alive=form.keep_alive.data,
                last_will_topic=form.last_will_topic.data,
                last_will_message=form.last_will_message.data,
                last_will_qos=form.last_will_qos.data,
                last_will_retain=retain
                )
        flash('Client MQTT ' + form.name.data + ' has benn created!', 'success')
        return redirect(url_for('mqtt.list_mqtt'))
    return render_template('mqtt/mqtt_create.html', title='Register Broker MQTT', form=form)


@bp.route("/list/mqtt", methods=['GET', 'POST'])
def list_mqtt():
    clients = list_all_client_mqtt()
    if not clients:
        flash('There are no records. Register a Broker MQTT', 'error')
        return redirect(url_for('mqtt.register_mqtt'))
    return render_template('mqtt/mqtt_list.html', title='Mqtt List', clients=clients)


@bp.route("/admin/Mqtt", methods=['GET', 'POST'])
def admin_mqtt():
    clients = list_all_client_mqtt()
    if not clients:
        flash('There are no records. Register a Broker MQTT', 'error')
        return redirect(url_for('mqtt.register_mqtt'))
    return render_template('mqtt/mqtt_admin.html', title='Mqtt Admin', clients=clients)   


@bp.route("/activate/mqtt/<int:id>", methods=['GET', 'POST'])
def activate_mqtt(id):
    client = list_client_mqtt_id(id)
    activate_client_mqtt(client)
    return redirect(url_for('mqtt.admin_mqtt'))


@bp.route("/deactivate/mqtt/<int:id>", methods=['GET', 'POST'])
def deactivate_mqtt(id):
    client = list_client_mqtt_id(id)
    deactivate_client_mqtt(client)
    return redirect(url_for('mqtt.admin_mqtt'))


@bp.route('/edit/mqtt/<int:id>', methods=['GET', 'POST'])
def edit_mqtt(id):
    form = EditMqttForm()
    mqtt_client = list_client_mqtt_id(id)
    if form.validate_on_submit():

        if form.last_will_topic is None:
            retain = False
        else:
            if form.last_will_retain.data == 'True':
                retain = True
            else:
                retain = False

        mqtt_client.name = form.name.data
        mqtt_client.address_url = form.address_url.data
        mqtt_client.port = form.port.data
        mqtt_client.username = form.username.data
        mqtt_client.password = form.password.data
        mqtt_client.keep_alive = form.keep_alive.data
        mqtt_client.last_will_topic = form.last_will_topic.data
        mqtt_client.last_will_message = form.last_will_message.data
        mqtt_client.last_will_qos = form.last_will_qos.data
        mqtt_client.last_will_retain = retain
        update_client_mqtt(mqtt_client.id,
                           mqtt_client.name,
                           mqtt_client.address_url,
                           mqtt_client.port,
                           mqtt_client.username,
                           mqtt_client.password,
                           mqtt_client.keep_alive,
                           mqtt_client.last_will_topic,
                           mqtt_client.last_will_message,
                           mqtt_client.last_will_qos,
                           mqtt_client.last_will_retain)
        reinitialise_client_mqtt(mqtt_client)
        flash('Your changes have been saved.')
        return redirect(url_for('mqtt.admin_mqtt'))
    elif request.method == 'GET':
        form.name.data = mqtt_client.name
        form.address_url.data = mqtt_client.address_url
        form.port.data = mqtt_client.port
        form.username.data = mqtt_client.username
        form.password.data = mqtt_client.password
        form.keep_alive.data = mqtt_client.keep_alive
        form.last_will_topic.data = mqtt_client.last_will_topic
        form.last_will_message.data = mqtt_client.last_will_message
        form.last_will_qos.data = mqtt_client.last_will_qos
        form.last_will_retain.data = mqtt_client.last_will_retain
    return render_template('mqtt/mqtt_edit.html', title='Edit Client Mqtt', form=form)


@bp.route("/delete/mqtt/<int:id>", methods=['GET', 'POST'])
def delete_mqtt(id):
    return 'OIIIIII'


@bp.route("/options/mqtt", methods=['GET', 'POST'])
def mqtt_opts():
    return render_template("mqtt/mqtt_opts.html", title='Mqtt Options')
