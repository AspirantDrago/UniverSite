import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Specialties(SqlAlchemyBase):
    __tablename__ = 'specialties'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    shortname = sa.Column(sa.String, nullable=False, unique=True)
    department_id = sa.Column(sa.Integer, sa.ForeignKey('departments.id'))

    department = orm.relationship('Department', backref='specialities')

    def __str__(self):
        return self.name
