from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/book.db'
db = SQLAlchemy(app)

class NewBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    allBooks = db.session.query(NewBooks).all()
    return render_template('index.html', books=allBooks)


@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == 'POST':
        newBooks = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        db.session.add(newBooks)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        bookID = request.form["id"]
        updateBook = NewBooks.query.get(bookID)
        updateBook.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    bookId = request.args.get('id')
    getBook = NewBooks.query.get(bookId)
    return render_template("edit.html", book=getBook)

@app.route("/delete")
def delete():
    bookID = request.args.get('id')

    deleteBook = NewBooks.query.get(bookID)
    db.session.delete(deleteBook)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

