from flask_admin.contrib.sqla import ModelView


class DeviceAdmin(ModelView):
    """Interface Admin Device"""
    column_list = ('Name',
                   'Topic_Pub',
                   'Topic_Sub',
                   'Last_Will_topic',
                   'Qos', 'Retained',
                   )

    column_searchable_list = ['name',
                              'topic_pub',
                              'topic_sub',
                              'last_will_topic',
                              'qos',
                              'retained',
                              ]


class DeviceTypeAdmin(ModelView):
    """Interface Admin DeviceType"""
    column_list = ('Id', 'Name')
    column_searchable_list = ['id', 'name']
