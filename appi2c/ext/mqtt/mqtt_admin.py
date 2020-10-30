from flask_admin.contrib.sqla import ModelView


class MqttAdmin(ModelView):
    """Interface Mqtt Admin"""

    column_list = ('name',
                   'address_url',
                   'port',
                   'keep_alive',
                   'username',
                   'password',
                   'last_will_topic',
                   'last_will_message',
                   'last_will_qos',
                   'last_will_retain')
                   
    column_searchable_list = ['name',
                              'address_url',
                              'port',
                              'keep_alive',
                              'username',
                              'password',
                              'last_will_topic',
                              'last_will_message',
                              'last_will_qos',
                              'last_will_retain']
