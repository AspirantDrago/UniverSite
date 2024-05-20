import sqlalchemy as sa
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Teacher(SqlAlchemyBase):
    __tablename__ = 'teachers'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    surname = sa.Column(sa.String, nullable=False)
    patronymic = sa.Column(sa.String, nullable=True)
    staff = sa.Column(sa.String, nullable=True)
    academic_degree = sa.Column(sa.String, nullable=True)

    cathedras = orm.relationship('Cathedra', back_populates='teachers', secondary='teachers_cathedra')

    def __str__(self):
        if self.patronymic:
            return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'
        return f'{self.surname} {self.name[0]}.'


teachers_cathedra = sa.Table(
    "teachers_cathedra",
    SqlAlchemyBase.metadata,
    sa.Column("teacher", sa.ForeignKey("teachers.id")),
    sa.Column("cathedra", sa.ForeignKey("cathedras.id"))
)
