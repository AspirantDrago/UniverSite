from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.lession_types import LessionType


class LessionTypesView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(LessionType, db_session, name='Типы занятий')

    column_editable_list = ['title', 'short_title']
    column_labels = {
        'title': 'Наименование',
        'short_title': 'Краткое наименование',
    }
