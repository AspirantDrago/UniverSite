from flask import Flask, render_template, request, redirect, Response
import json
from datetime import timedelta

from config import config
from forms.form_login import FormLogin, FormRegister

from data import db_session
from data.users import User
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_phrase'


@app.route('/')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return render_template('index.html', news=news)


@app.route('/click')
def click():
    count_clicks = int(request.cookies.get('x',  0))
    count_clicks += 1
    response = Response(f'Меня открыли {count_clicks} раз')
    response.set_cookie('x', str(count_clicks), timedelta(days=365 * 2))
    return response



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email).first()
        if user is None or not user.check_password(form.password):
            return render_template('form.html', form=form, form_header='Войти',
                                   error_message='Пользователя с указанным email/паролем не существует')
        # TODO: авторизовать пользователя
        return redirect('/profile')
    return render_template('form.html', form=form, form_header='Войти')


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = FormRegister()
#     if form.validate_on_submit():
#         # TODO: авторизовать пользователя
#         return redirect('/login')
#     return render_template('form.html', form=form, form_header='Регистрация')
#


if __name__ == '__main__':
    db_session.global_init('db/db.db')
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
