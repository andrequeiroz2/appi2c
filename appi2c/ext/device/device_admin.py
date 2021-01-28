from flask_admin.contrib.sqla import ModelView



class DeviceAdmin(ModelView):
    """Interface Admin Device"""

    can_delete = False
    can_edit = False
    can_delete = False
    can_create = False
    page_size = 50
    form_excluded_columns = ['position_left', 'position_top', 'type_id', 'icon_id', 'group_id']
    column_searchable_list = ['name']


class DeviceTypeAdmin(ModelView):
    """Interface Admin DeviceType"""

    can_delete = False
    can_edit = False
    can_delete = False
    can_create = False
    page_size = 50
    column_list = ('id', 'name')
    column_searchable_list = ['id', 'name']
