import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Classroom(SqlAlchemyBase):
    __tablename__ = 'classroom'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, unique=True)
    number_of_seats = sa.Column(sa.Integer, nullable=False)
    number_of_pc = sa.Column(sa.Integer, nullable=False, default=0)
    has_projector = sa.Column(sa.Boolean, nullable=False, default=False)

    lessions = orm.relationship('Lession')

    def __str__(self):
        return self.title
