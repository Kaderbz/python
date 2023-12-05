from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
bcrypt =Bcrypt(app)



@app.route('/')
def root():
    return render_template("index.html")

@app.route('/register' , methods=['post'])
def create():
    print("*"*20,"Hey")
    data = request.form
    if not User.validate_register(data):
        return redirect('/')
    encrypted_data = {
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'password': bcrypt.generate_password_hash(data['password'])
    }
    User.create(encrypted_data)
    session['user'] = User.get_by_email(encrypted_data).__dict__
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if session.get('user'):
        data = session['user']
        print("|"*30,data)
        if not User.get_by_email(data) == False:
            return render_template("dashboard.html")
    return redirect('/')

@app.route('/login' , methods = ['post'])
def login():
    data = request.form
    if not User.validate_login(data):
        return redirect('/')
    session['user'] = User.get_by_email(data).__dict__
    print("-"*30,session['user'])
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')