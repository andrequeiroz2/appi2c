from flask_admin.contrib.sqla import ModelView


class IconAdmin(ModelView):
    """Interface Icon Admin"""

    column_list = ('Id', 'Html Class')               
    column_searchable_list = ['id', 'html_class']