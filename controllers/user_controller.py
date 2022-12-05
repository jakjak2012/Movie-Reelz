from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

from flask_app.models.user_model import User





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_in')
def sign_in():
    return render_template('login_register.html')

@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
            return redirect('/sign_in')
    found_user = User.get_one_by_email(request.form)
    session["uid"] = found_user.id
    session["user_name"] = found_user.first_name
    
    return redirect('/dashboard')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/sign_in')
    hash = bcrypt.generate_password_hash(request.form['password'])
    print(hash)

    data = {
        **request.form
    }
    data['password'] = hash

    userid = User.create(data)

    session["uid"] = userid
    return redirect('/dashboard')

@app.route('/logout')
def destroy():
    session.clear()
    return redirect('/')
