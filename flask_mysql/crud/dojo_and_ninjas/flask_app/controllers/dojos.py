from flask_app import app
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    """For this assignment redirect to dojos page"""
    return redirect('/dojos')

@app.route('/dojos')
def show_all():
    """Render All the dojos"""
    dojos = Dojo.show_all_dojos()
    print(dojos)
    return render_template('dojos.html', all_dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def add_dojo():
    """Add a dojo location to the list"""

    if request.form['name'] == '':
        return redirect('/dojos')

    data = {
        'name': request.form['name']
    }

    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_all_ninja(dojo_id):
    """Show all the ninja of a particular dojo"""
    data = {
        'dojo_id': dojo_id
    }
    dojo = Dojo.get_dojo_and_all_ninjas(data)
    return render_template('dojo_show.html', dojo=dojo)
