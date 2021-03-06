from market import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user, login_manager




@app.route('/')
@app.route('/home')
def home_page():
    return render_template("child.html")


@app.route('/market')
def market():
    items = Item.query.all()
     
    return render_template("market.html", items=items)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_adress= form.email_adress.data, password= form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Hubo un error: {err_msg}', category='danger')
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user= User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Succes! You arre logged in as:{attempted_user.username}', category='success')
            return redirect(url_for('market'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    
    
    return render_template('login.html', form=form)
 