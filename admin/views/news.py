from sqlalchemy.orm import Session

from ._default_view import DefaultView
from data.news import News


class NewsView(DefaultView):
    def __init__(self, db_session: Session):
        super().__init__(News, db_session, name='Новости')

    column_exclude_list = ['text', ]
    column_searchable_list = ['text', 'title']
    column_filters = ['created']
    column_editable_list = ['title']
    form_excluded_columns = ['created']
    column_labels = {
        'title': 'Заголовок',
        'text': 'Текст новости',
        'created': 'Создано',
        'image': 'Изображение'
    }

    column_formatters = dict(
        image=DefaultView.image_preview_formatter,
    )
