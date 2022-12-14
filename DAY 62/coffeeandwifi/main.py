from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe location on google maps", validators=[DataRequired(), URL()])
    openTime = StringField("Opening times", validators=[DataRequired()])
    closeTime = StringField("Closing time", validators=[DataRequired()])
    coffeeRating = SelectField("Wifi strength rating", choices=["✘","☕","☕☕","☕☕☕"], validators=[DataRequired()])
    wifiRating = SelectField("wifi strength rating", choices=["✘","💪","💪💪","💪💪💪"], validators=[DataRequired()])
    powerRating = SelectField("power socket available", choices=["✘","🔌","🔌🔌","🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below


@app.route("/home")
def home():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.openTime.data},"
                           f"{form.closeTime.data},"
                           f"{form.coffeeRating.data},"
                           f"{form.wifiRating.data},"
                           f"{form.powerRating.data}")
        return redirect(url_for('cafes'))
        # print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
