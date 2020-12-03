from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action


class UserAdmin(ModelView):
    """Interface User Admin"""
    can_delete = False
    page_size = 50
    form_excluded_columns = ['groups', 'devices', 'client_mqtt']
    column_list = ('username', 'email', 'admin')
    column_searchable_list = ['username', 'email']
