from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, Length, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    name = StringField('Pet Name', validators=[InputRequired(message='Please include name of pet')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message='Please enter a valid URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=1, max=30, message='Please enter an age from 1 to 30')])
    notes = StringField('Notes', validators=[Optional()])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')], validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet"""

    photo_url = StringField('Photo URL', validators=[Optional(), URL(message='Please enter a valid URL')])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available', validators=[Optional()], default=True)