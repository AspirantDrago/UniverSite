from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.teachers import Teacher


class TeachersView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Teacher, db_session, name='Преподаватели')

    column_searchable_list = ['name', 'surname', 'patronymic', 'staff', 'academic_degree']
    column_editable_list = ['name', 'surname', 'patronymic', 'staff', 'academic_degree']
    column_labels = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'patronymic': 'Отчество',
        'staff': 'Должность',
        'academic_degree': 'Ученая степень',
        'cathedras': 'Кафедры'
    }
