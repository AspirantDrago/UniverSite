import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Group(SqlAlchemyBase):
    __tablename__ = 'groups'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    course = sa.Column(sa.Integer, nullable=False)
    speciality_id = sa.Column(sa.Integer, sa.ForeignKey('specialties.id'))

    speciality = orm.relationship('Specialties', backref='groups')

    def __str__(self):
        return self.name
