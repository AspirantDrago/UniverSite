from collections import defaultdict
from datetime import datetime

from flask import Flask, render_template, redirect, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from config import config
from forms.form_login import FormLogin, FormRegister, FormChangePassword
from data import db_session
from data.users import User
from data.news import News
from data.departments import Department
from data.groups import Group
from data.specialties import Specialties
from admin import init_admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_phrase'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int) -> User:
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    departments = db_sess.query(Department).all()
    return render_template('index.html', departments=departments)


@app.route('/dep/<int:department_id>')
def department(department_id: int):
    db_sess = db_session.create_session()
    department = db_sess.get(Department, department_id)
    if department is None:
        return abort(404)
    specialties = db_sess.query(Specialties).filter(Specialties.department_id == department_id).all()
    return render_template('department.html', department=department, specialties=specialties)


@app.route('/spec/<int:specialty_id>')
def specialty(specialty_id: int):
    db_sess = db_session.create_session()
    specialty = db_sess.get(Specialties, specialty_id)
    if specialty is None:
        return abort(404)
    groups = db_sess.query(Group).filter(Group.speciality_id == specialty_id).all()
    groups_dict = defaultdict(list)
    for group in groups:
        groups_dict[group.course].append(group)
    return render_template('speciality.html', specialty=specialty, groups_dict=groups_dict)


@app.route('/group/<int:group_id>')
@app.route('/group/<int:group_id>/<date>')
def group(group_id: int, date: str = None):
    db_sess = db_session.create_session()
    group = db_sess.get(Group, group_id)
    if group is None:
        return abort(404)
    is_current_day = date is None
    if date is not None:
        try:
            current_day = datetime.strptime(date, '%Y-%m-%d').date()
        except:
            abort(400)
    else:
        current_day = datetime.today()
    return render_template(
        'group.html',
        group=group,
        is_current_day=is_current_day,
        current_day=current_day
    )


@app.route('/news')
def news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return render_template('news.html', news=news)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            return render_template('form.html', form=form, form_header='Войти',
                                   error_message='Пользователя с указанным email/паролем не существует')
        login_user(user, remember=form.is_remember.data)
        return redirect('/profile')
    return render_template('form.html', form=form, form_header='Войти')


@login_required
@app.route('/profile')
def profile():
    return render_template('profile.html', user=current_user)


@login_required
@app.route('/changepassword', methods=['GET', 'POST'])
def change_password():
    form = FormChangePassword()
    if form.validate_on_submit():
        old_password = form.old_password.data.strip()
        password = form.password.data.strip()
        if not current_user.check_password(old_password):
            return render_template('form.html', form=form, form_header='Смена пароля', error_message='Неверный пароль')
        if password == old_password:
            return render_template('form.html', form=form, form_header='Смена пароля', error_message='Вы ввели тот же пароль')
        db_sess = db_session.create_session()
        current_user.set_password(password)
        db_sess.merge(current_user)
        db_sess.commit()
        logout_user()
        return redirect('/login')
    return render_template('form.html', form=form, form_header='Смена пароля')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        try:
            user = User(
                name=form.name.data,
                about=form.about.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
        except BaseException as e:
            print(e.__class__.__name__, e, sep=': ')
            return render_template('form.html', form=form, form_header='Регистрация', error_message='Ошибка регистрации. Повторите позже')
        else:
            return redirect('/login')
    return render_template('form.html', form=form, form_header='Регистрация')


if __name__ == '__main__':
    db_session.global_init('db/db.db')
    db_sess = db_session.create_session()
    init_admin(app, db_sess)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
