import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Lession(SqlAlchemyBase):
    __tablename__ = 'lession'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    discipline_id = sa.Column(sa.Integer, sa.ForeignKey("disciplines.id"))
    teacher_id = sa.Column(sa.Integer, sa.ForeignKey("teachers.id"))
    lession_type_id = sa.Column(sa.Integer, sa.ForeignKey("lession_types.id"))
    classroom_id = sa.Column(sa.Integer, sa.ForeignKey("classroom.id"))

    discipline = orm.relationship('Discipline', back_populates='lessions')
    teacher = orm.relationship('Teacher', back_populates='lessions')
    lession_type = orm.relationship('LessionType', back_populates='lessions')
    classroom = orm.relationship('Classroom', back_populates='lessions')
    groups = orm.relationship('Group', secondary='group_lession', back_populates='lessions')
    schedules = orm.relationship('Schedule')

    def __str__(self):
        groups_text = ', '.join(map(str, self.groups))
        return f'{groups_text} - {self.discipline} ({self.lession_type.short_title}) преп. {self.teacher}, ауд. {self.classroom}'


group_lession = sa.Table(
    "group_lession",
    SqlAlchemyBase.metadata,
    sa.Column("group", sa.ForeignKey("groups.id")),
    sa.Column("lession", sa.ForeignKey("lession.id"))
)
