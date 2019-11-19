from flask_wtf import Form
from wtforms import StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class taskForm(Form):
    date = DateField(label='Date', validators=[DataRequired()])
    title = StringField(label='Title', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])


class searchForm(Form):
    searchdate = DateField(validators=[DataRequired])
