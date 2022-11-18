from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#auth user
LOGINMANAGER = LoginManager()
LOGINMANAGER.init_app(app)


@LOGINMANAGER.user_loader
def user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # if User.query.filter_by(email=request.form.get('email')).first():
        #     flash("Email Exists, you can try to log in")
        #     return redirect(url_for('login'))
        hashPassword = generate_password_hash(
            request.form.get('password'),
            method='sha256',
            salt_length=8
        )
        newUser = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hashPassword
        )

        db.session.add(newUser)
        db.session.commit()

        login_user(newUser)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        usser = User.query.filter_by(email=email).first()

        if not usser:
            flash("The email does not exisit, please try again")
            return redirect(url_for('login'))

        elif not check_password_hash(usser.password, password):
            flash("Password inccorrect, please try again")
            return redirect(url_for('login'))
        else:
            login_user(usser)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
