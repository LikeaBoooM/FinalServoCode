import os
import secrets
import pandas,geopy
from math import pi,cos,sqrt
from geopy.geocoders import Nominatim
from flask import render_template, url_for, flash, redirect, request, abort
from flaskb import app, db, bcrypt
from flaskb.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskb.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flaskb import elevation

x1 = float(0)
y1 = float(0) 
 
y2 = float(0)
x2 = float(0)



@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,range=form.range.data,actually_longitude=form.actually_longitude.data,actually_latitude=form.actually_latitude.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    global y1
    global x1
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.range = form.range.data
        current_user.actually_latitude = form.actually_latitude.data
        current_user.actually_longitude = form.actually_longitude.data
        x1f = form.actually_longitude.data
        y1f = form.actually_latitude.data
        x1 = float(x1f)
        y1 = float(y1f)
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.range.data = current_user.range
        form.actually_latitude.data = current_user.actually_latitude
        form.actually_longitude.data = current_user.actually_longitude
        x1f = form.actually_longitude.data
        y1f = form.actually_latitude.data
        x1 = float(x1f)
        y1 = float(y1f)

        
    return render_template('account.html', title='Account', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        x1 = current_user.actually_longitude
        y1 = current_user.actually_latitude 
        x2f = form.longitude.data
        y2f = form.latitude.data
        x2 = float(x2f)
        y2 = float(y2f)
        post = Post(title=form.title.data, longitude = form.longitude.data,latitude = form.latitude.data,author=current_user,method = sqrt(pow((x2-x1),2)+(cos((x1*pi)/180))*pow((y2-y1),2))*(40075.704/360),elevation = elevation.evalute(x2,y2))
        db.session.add(post)
        db.session.commit()
        flash('Your location has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.longitude  = form.longitude.data
        post.latitude = form.latitude.data
        db.session.commit()
        flash('Your location has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.longitude.data = post.longitude 
        form.latitude.data = post.latitude
    return render_template('create_post.html', title='Update location',
                           form=form, legend='Update location')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your location has been deleted','success')
    return redirect(url_for('home'))