from flask_admin.contrib.sqla import ModelView


class UserAdmin(ModelView):
    """Interface User Admin"""

    can_edit = False
    can_delete = False
    can_create = False
    page_size = 50
    column_exclude_list = ('password')
    form_excluded_columns = ('password')
    column_auto_select_related = True
