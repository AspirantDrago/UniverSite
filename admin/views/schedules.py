from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.schedules import Schedule


class ScheduleView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(Schedule, db_session, name='Расписание')

    column_list = ['lession', 'day_of_week_name', 'time_interval', 'stars', 'date_interval']
    form_excluded_columns = ['day_of_week']
    # column_list = ['name', 'course', 'speciality']
    # column_searchable_list = ['name', 'course']
    # column_editable_list = ['name', 'course', 'speciality']
    # column_filters = ['name', 'course', 'speciality']
    column_labels = {
        'lession': 'Занятие',
        'day_of_week_name': 'День недели',
        'day_of_week': 'День недели',
        'start_time': 'Время начала занятия',
        'end_time': 'Время окончания занятия',
        'on_one_star': 'Проводится по неделям с 1 звездой',
        'on_two_star': 'Проводится по неделям с 2 звездами',
        'stars': 'Звезды',
        'start_date': 'Начало обучения',
        'end_date': 'Окончание обучения',
        'time_interval': 'Время',
        'date_interval': 'Период обучения'
    }
