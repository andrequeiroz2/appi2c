from flask_admin.contrib.sqla import ModelView


class GroupAdmin(ModelView):
    """Interface Local Admin"""

    column_list = ('name', 'description')
    column_searchable_list = ['name', 'description']
