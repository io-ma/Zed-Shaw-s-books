from flask import Flask, request, render_template, redirect, url_for, flash, abort, session, escape
from config import Config
from forms import SignupForm, LoginForm
#from models import db, User
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_assets import Environment, Bundle
from app import app
from app import planisphere
from  app.models import db, User

#app = Flask(__name__)
#app.config.from_object(Config)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('styles.scss', filters='scss', output='styles.css')
assets.register('scss_all', scss)
#login = LoginManager(app)
#login.login_view = 'login'
#db.create_all()


@app.route("/")
@app.route('/index')
@login_required
def index():
    user=current_user
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do you need it?
            # return render_template("you_died.html")
            print("no room name")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run
