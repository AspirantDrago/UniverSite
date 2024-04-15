from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)
    name = sa.Column(sa.String, nullable=False)
    about = sa.Column(sa.String)
    created = sa.Column(sa.DateTime, default=datetime.now)
    password = sa.Column(sa.String)

    def __str__(self):
        return f'{self.name} ({self.email})'

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

