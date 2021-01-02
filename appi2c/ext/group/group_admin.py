from flask_admin.contrib.sqla import ModelView


class GroupAdmin(ModelView):
    """Interface Local Admin"""
    can_delete = False
    can_edit = False
    can_delete = False
    can_create = False
    page_size = 50
    column_list = ('name', 'description', 'file')
    column_searchable_list = ['name', 'description']
