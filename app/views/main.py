from flask import render_template, jsonify, Flask, redirect, url_for, request
from app import app
import random
import os
from flask import flash
from app.forms import user as user_forms
from app import models


@app.route('/')
def Home():
    return render_template('index.html', title='Home')

@app.route('/measurement', methods=['GET', 'POST'])
def measurement():
    form = user_forms.Measurements()
    if form.validate_on_submit():
        # Create a user who hasn't validated his email address
        meas = models.Measure(
            age=form.age.data,
            heart_rate=form.heart_rate.data,
            weight=form.weight.data,
            blood_pressure=form.blood_pressure.data
        )
        # Insert the user in the database
        #db.session.add(meas)
        #db.session.commit()
        
        flash('done')
        return redirect(url_for('map'))
    return render_template('/measurement.html', form=form)


@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
