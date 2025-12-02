from flask_wtf import FlaskForm
from wtforms.widgets import RangeInput
from wtforms.validators import DataRequired, NumberRange
from wtforms import SubmitField, DecimalField, IntegerField

#             'danceability',
#             'energy',
#             'loudness',
#             'speechiness',
#             'acousticness',
#             'instrumentalness',
#             'liveness',
#             'valence',
#             'tempo'

class SubmissionForm(FlaskForm):
    danceability = DecimalField('Danceability', validators=[
        DataRequired(),
        NumberRange(0, 1)
    ], widget=RangeInput(.01))
    
    energy = DecimalField('Energy', validators=[
        DataRequired(),
        NumberRange(0, 1)
    ], widget=RangeInput(.01))
    
    loudness = DecimalField('Loudness', validators=[
        DataRequired(),
        NumberRange(-50, 5)
    ], widget=RangeInput(.25))
    
    acousticness = DecimalField('Acousticness', validators=[
        DataRequired(),
        NumberRange(0, 1)
    ], widget=RangeInput(.01))
    
    instrumentalness = DecimalField('Instrumentalness', validators=[
        DataRequired(),
        NumberRange(0, 1)
    ], widget=RangeInput(.01))

    liveness = DecimalField('Liveness', validators=[
        DataRequired(),
        NumberRange(0, 1)
    ], widget=RangeInput(.01))

    valence = DecimalField('Valence', validators=[
        DataRequired(),
        NumberRange(0, 1)
    ], widget=RangeInput(.01))

    tempo = IntegerField('Tempo', validators=[
        DataRequired(),
        NumberRange(50, 250)
    ], widget=RangeInput(5))

    submit = SubmitField('Find Music')
