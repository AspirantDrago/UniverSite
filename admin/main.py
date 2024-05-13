from flask import Flask
from flask_admin import Admin

from sqlalchemy.orm import Session
from flask_babel import Babel

from .views.users import UsersView
from .views.news import NewsView
from .views.departments import DepartmentsView
from .views.specialties import SpecialtiesView
from .views.groups import GroupsView


def init_admin(app: Flask, db_session: Session) -> None:
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['BABEL_DEFAULT_LOCALE'] = 'ru'

    admin = Admin(app, name='Расписание', template_mode='bootstrap4')
    admin.add_view(UsersView(db_session))
    admin.add_view(NewsView(db_session))
    admin.add_view(DepartmentsView(db_session))
    admin.add_view(SpecialtiesView(db_session))
    admin.add_view(GroupsView(db_session))

    babel = Babel(app, )
