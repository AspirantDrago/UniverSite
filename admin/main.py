from flask import Flask
from flask_admin import Admin

from sqlalchemy.orm import Session
from flask_babel import Babel

from .views.users import UsersView
from .views.news import NewsView
from .views.departments import DepartmentsView
from .views.specialties import SpecialtiesView
from .views.groups import GroupsView
from .views.disciplines import DisciplinesView
from .views.cathedras import CathedrasView
from .views.teachers import TeachersView
from .views.classrooms import ClassroomsView
from .views.lession_types import LessionTypesView


def init_admin(app: Flask, db_session: Session) -> None:
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['BABEL_DEFAULT_LOCALE'] = 'ru'

    admin = Admin(app, name='Расписание', template_mode='bootstrap4')
    admin.add_view(UsersView(db_session))
    admin.add_view(NewsView(db_session))
    admin.add_view(DepartmentsView(db_session))
    admin.add_view(SpecialtiesView(db_session))
    admin.add_view(GroupsView(db_session))
    admin.add_view(DisciplinesView(db_session))
    admin.add_view(CathedrasView(db_session))
    admin.add_view(TeachersView(db_session))
    admin.add_view(ClassroomsView(db_session))
    admin.add_view(LessionTypesView(db_session))

    babel = Babel(app, )
