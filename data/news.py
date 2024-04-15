from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    title = sa.Column(sa.String, nullable=False)
    text = sa.Column(sa.String, nullable=False)
    image = sa.Column(sa.String)
    created = sa.Column(sa.DateTime, default=datetime.now)

    author = orm.relationship("User", backref='news')

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)
