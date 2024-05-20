from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.cathedras import Cathedra


class CathedrasView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Cathedra, db_session, name='Кафедры')

    column_searchable_list = ['title']
    column_editable_list = ['title']
    column_labels = {
        'title': 'Наименование',
        'teachers': 'Сотрудники',
    }
