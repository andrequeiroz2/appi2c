from flask_admin.contrib.sqla import ModelView


class IconAdmin(ModelView):
    """Interface Icon Admin"""

    can_delete = False
    can_edit = False
    can_create = False
    page_size = 50
    column_list = ('id', 'html_class')               
    column_searchable_list = ['id', 'html_class']