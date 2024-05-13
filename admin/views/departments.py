from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.departments import Department


class DepartmentsView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Department, db_session, name='Подразделения')

    column_searchable_list = ['name', 'shortname']
    column_editable_list = ['name', 'shortname']
    column_labels = {
        'name': 'Наименование',
        'shortname': 'Краткое наименование'
    }
