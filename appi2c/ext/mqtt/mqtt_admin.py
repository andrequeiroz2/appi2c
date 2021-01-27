from flask_admin.contrib.sqla import ModelView


class MqttAdmin(ModelView):
    """Interface Mqtt Admin"""

    can_delete = False
    can_edit = False
    can_create = False
    page_size = 50
    form_excluded_columns = ('user_id')
    column_searchable_list = ['name', 'address_url']
