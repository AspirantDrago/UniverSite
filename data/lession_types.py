import sqlalchemy as sa

from .db_session import SqlAlchemyBase


class LessionType(SqlAlchemyBase):
    __tablename__ = 'lession_types'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, unique=True)
    short_title = sa.Column(sa.String, nullable=False, unique=True)

    def __str__(self):
        return self.title
