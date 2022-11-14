from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


#APIS
MOVIE_URL = "API"
MOVIE_API = "API KEY"
MOVIE_IMAGE_URL = "IMAGE URL"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    imgUrl = db.Column(db.String(250), nullable=False)
db.create_all()


# newMovie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(newMovie)
# db.session.commit()

class RateForm(FlaskForm):
    rating = StringField("Your rating over 10")
    review = StringField("Your review")
    submit = SubmitField("Done")

class GetMovie(FlaskForm):
    title = StringField("Movie title", validators=[DataRequired()])
    submit = SubmitField("Add movie")

@app.route("/")
def home():
    allMovies = Movie.query.order_by(Movie.rating).all()

    for films in range(len(allMovies)):
        allMovies[films].ranking = len(allMovies) - films
    db.session.commit()
    return render_template("index.html", movies=allMovies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = GetMovie()

    if form.validate_on_submit():
        movieTitle = form.title.data
        response = requests.get(MOVIE_URL, params={"api_key":MOVIE_API, "query": movieTitle})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateForm()
    movieId = request.args.get("id")
    movie = Movie.query.get(movieId)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movieID= request.args.get("id")

    deleteMovie = Movie.query.get(movieID)
    db.session.delete(deleteMovie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/find")
def findMovie():
    movieApiId = request.args.get("id")
    if movieApiId:
        movie_api_url = f"{MOVIE_API}/{movieApiId}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_URL})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
