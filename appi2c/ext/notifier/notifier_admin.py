from flask_admin.contrib.sqla import ModelView


class NotifierAdmin(ModelView):
    """Interface Notifier Admin"""
    can_delete = False
    can_edit = False
    can_create = False
    page_size = 50
    form_excluded_columns = ['token', 'chat_id']
