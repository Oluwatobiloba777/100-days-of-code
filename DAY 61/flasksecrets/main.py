from flask import Flask, render_template, request
from wtforms import Form,StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class LoginForm(Form):
    email = StringField(label='Email Address', validators=[DataRequired(), validators.Length(min=6, max=80), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
Bootstrap(app)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)