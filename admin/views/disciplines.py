from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.disciplines import Discipline


class DisciplinesView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Discipline, db_session, name='Дисциплины')

    column_list = ['title']
    column_searchable_list = ['title']
    column_editable_list = ['title']
    form_excluded_columns = ['lessions']
    column_labels = {
        'title': 'Наименование',
    }
