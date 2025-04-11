from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy_serializer import SerializerMixin


class JobsForm(FlaskForm, SerializerMixin):
    team_leader = IntegerField('Руководитель(id)', validators=[DataRequired()])
    job = TextAreaField("Работа")
    work_size = IntegerField("Время работы в часах")
    collaborators = StringField('Участники(id)')
    start_date = DateField("Дата начала")
    end_date = DateField("Дата завершения")
    is_finished = BooleanField('Завершена')
    submit = SubmitField('Применить')
