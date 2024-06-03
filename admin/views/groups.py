from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.groups import Group
from wtforms import IntegerField
from wtforms.validators import NumberRange


class GroupsView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Group, db_session, name='Группы')

    column_list = ['name', 'course', 'speciality']
    column_searchable_list = ['name', 'course']
    column_editable_list = ['name', 'course', 'speciality']
    column_filters = ['name', 'course', 'speciality']
    column_labels = {
        'name': 'Наименование',
        'course': 'Курс',
        'speciality': 'Специальность'
    }
    form_excluded_columns = ['lessions']
    form_args = dict(
        course=dict(label='Курс', validators=[NumberRange(min=1, max=6)])
    )
