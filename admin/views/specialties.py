from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.specialties import Specialties


class SpecialtiesView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Specialties, db_session, name='Направления')

    column_list = ['name', 'shortname', 'department']
    column_searchable_list = ['name', 'shortname']
    column_editable_list = ['name', 'shortname', 'department']
    column_filters = ['department']
    column_labels = {
        'name': 'Наименование',
        'shortname': 'Краткое наименование',
        'department': 'Подразделение',
        'groups': 'Группы'
    }
