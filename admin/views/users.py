from sqlalchemy.orm import Session
from wtforms.validators import DataRequired, Email

from ._default_view import DefaultView
from data.users import User


class UsersView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(User, db_session, name='Пользователи')

    column_exclude_list = ['password']
    column_searchable_list = ['email', 'name']
    column_filters = ['created']
    column_editable_list = ['name', 'about']
    form_excluded_columns = ['created', 'password']
    column_formatters = dict(
        email=DefaultView.link_mail_formatter,
    )
    column_labels = {
        'name': 'Имя',
        'about': 'О пользователе',
        'created': 'Зарегистрирован',
    }
    form_args = {
        'name': {
            'label': 'Имя',
            'validators': []
        },
        'email': {
            'label': 'Email',
            'validators': [
                DataRequired('Ошибка. Электронная почта не указана!'),
                Email('Введён некорректный адрес электронной почты!')
            ]
        },
        'about': {
            'label': 'О пользователе',
            'validators': []
        }
    }