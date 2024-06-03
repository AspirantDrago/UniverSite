from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.classrooms import Classroom


class ClassroomsView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Classroom, db_session, name='Аудитории')

    column_list = ['title', 'number_of_seats', 'number_of_pc', 'has_projector', 'lessions']
    form_excluded_columns = ['lessions']
    column_searchable_list = ['title']
    column_editable_list = ['title', 'number_of_seats', 'number_of_pc', 'has_projector']
    column_sortable_list = ['title', 'number_of_seats', 'number_of_pc']
    column_filters = ['has_projector']
    column_labels = {
        'title': 'Номер аудитории',
        'number_of_seats': 'К-во мест',
        'number_of_pc': 'К-во ПК',
        'has_projector': 'Наличие проектора',
        'lessions': 'Занятия',
    }
