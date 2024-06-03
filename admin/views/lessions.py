from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.lession import Lession


class LessionView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Lession, db_session, name='Занятия')

    # column_list = ['name', 'course', 'speciality']
    # column_searchable_list = ['name', 'course']
    # column_editable_list = ['name', 'course', 'speciality']
    # column_filters = ['name', 'course', 'speciality']
    column_labels = {
        'discipline': 'Дисциплина',
        'teacher': 'Преподаватель',
        'classroom': 'Аудитория',
        'groups': 'Группы',
        'lession_type': 'Тип занятия',
    }
