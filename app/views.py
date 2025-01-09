from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


from app import app, db
from app.models import User


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmed_password = request.form.get('confirm_password')

        if password != confirmed_password:
            flash("Passwords are not equal")
        else:
            print('added user')
            hash_password = generate_password_hash(password)
            db.session.add(User(login = login, email = email, password = hash_password))
            db.session.commit()
            return redirect(url_for('login_page'))

    return render_template('register.html')

@app.route('/login', methods = ['GET','POST'])
def login_page():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login or password is not correct')

    return render_template('login.html')

def logout():
    pass