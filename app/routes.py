from app import app
import pandas as pd
from app.forms import SubmissionForm
from model.music_model import MusicModel
from flask import render_template, flash

model = MusicModel()
model.train_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubmissionForm()
    if form.validate_on_submit():
        
        form_data = [
            form.danceability.data,
            form.energy.data,
            form.loudness.data,
            form.acousticness.data,
            form.instrumentalness.data,
            form.liveness.data,
            form.valence.data,
            form.tempo.data
        ]

        flash('Prediction Made!', 'success')
        results = model.predict(form_data)
        print (results)

        # redirect back to this page
        return render_template('base.html', form=form, results=results)

    return render_template('form.html', form=form, results=pd.DataFrame())

