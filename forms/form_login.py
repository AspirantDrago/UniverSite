from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class FormLogin(FlaskForm):
    email = EmailField('Электронная почта', validators=[DataRequired('Ошибка. Электронная почта'
                                                                     ' не указана!')])
    password = PasswordField('Введите пароль', validators=[DataRequired('Ошибка. Пароль не указан!')])
    is_remember = BooleanField('Запомнить на этом компьютере')
    submit = SubmitField('Войти')


class Password2Mixin:
    password = PasswordField('Введите пароль (обязательно)', validators=[
        DataRequired('Ошибка. Пароль не указан!'),
        Length(8, 24, 'Ошибка. Пароль должен иметь длину от 8 до 24 символов.'),
        Regexp(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[a-zA-Z0-9]+$', 0,
               'Ошибка. Пароль олжен содержать минимум 1 символ латинского алфавита в верхнем и 1 символ в нижем регистре, а также минимум 1 цифру.')
    ])
    password_repeat = PasswordField('Повторите пароль (обязательно)', validators=[
        DataRequired('Ошибка. Пароль не указан!'),
        EqualTo('password', 'Ошибка. Пароли не совпадают!')
    ])


class FormRegister(FlaskForm, Password2Mixin):
    email = EmailField('Электронная почта (обязательно)', validators=[
        DataRequired('Ошибка. Электронная почта не указана!'),
        Email('Введён некорректный адрес электронной почты!')
    ])
    name = StringField('Имя')
    about = TextAreaField('О себе')
    submit = SubmitField('Зарегистрироваться')


class FormChangePassword(FlaskForm, Password2Mixin):
    old_password = PasswordField('Введите старый пароль')
    submit = SubmitField('Сохранить изменения')
