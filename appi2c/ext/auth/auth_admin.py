from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action


class UserAdmin(ModelView):
    """Interface User Admin"""

    column_list = ('username', 'email', 'admin')
    column_searchable_list = ['username', 'email']
