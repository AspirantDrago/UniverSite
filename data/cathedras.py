import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Cathedra(SqlAlchemyBase):
    __tablename__ = 'cathedras'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, unique=True)

    teachers = orm.relationship('Teacher', back_populates='cathedras', secondary='teachers_cathedra')

    def __str__(self):
        return self.title
