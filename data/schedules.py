import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Schedule(SqlAlchemyBase):
    __tablename__ = 'schedules'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    lession_id = sa.Column(sa.Integer, sa.ForeignKey("lession.id"), nullable=False)
    day_of_week = sa.Column(sa.Integer, nullable=False)
    start_time = sa.Column(sa.Time, nullable=False)
    end_time = sa.Column(sa.Time, nullable=False)
    on_one_star = sa.Column(sa.Boolean, nullable=False, default=True)
    on_two_star = sa.Column(sa.Boolean, nullable=False, default=True)
    start_date = sa.Column(sa.Date, nullable=False, default=datetime.date.today())
    end_date = sa.Column(sa.Date, nullable=True, default=None)

    lession = orm.relationship("Lession", back_populates='schedules')

    @property
    def day_of_week_name(self) -> str:
        arr = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
        return arr[self.day_of_week]

    @property
    def stars(self) -> str:
        if self.on_one_star and not self.on_two_star:
            return '★'
        elif not self.on_one_star and self.on_two_star:
            return '★★'
        elif self.on_one_star and self.on_two_star:
            return ''

    @property
    def time_interval(self) -> str:
        return f'{self.start_time.strftime("%H:%M")} - {self.end_time.strftime("%H:%M")}'

    @property
    def date_interval(self) -> str:
        if self.end_date is None:
            return f'{self.start_date.strftime("%d.%m.%Y")} - наст. время'
        if self.start_date == self.end_date:
            return f'{self.start_date.strftime("%d.%m.%Y")}'
        return f'{self.start_date.strftime("%d.%m.%Y")} - {self.end_date.strftime("%d.%m.%Y")}'
