from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class WordsForm(FlaskForm):
    words = TextAreaField('words', validators=[DataRequired()])