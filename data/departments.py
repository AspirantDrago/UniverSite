import sqlalchemy as sa

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    shortname = sa.Column(sa.String, nullable=False, unique=True)

    def __str__(self):
        return self.name
