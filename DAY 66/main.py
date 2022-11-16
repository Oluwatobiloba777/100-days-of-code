import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)



@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/route", methods=["GET"])
def route():
    cafe = db.session.query(Cafe).all()
    randomCafe = random.choice(cafe)
    return jsonify(cafe={
        "id": randomCafe.id,
        "name": randomCafe.name,
        "map_url": randomCafe.map_url,
        "img_url": randomCafe.img_url,
        "location": randomCafe.location,
        "seats": randomCafe.seats,
        "has_toilet": randomCafe.has_toilet,
        "has_wifi": randomCafe.has_wifi,
        "has_sockets": randomCafe.has_sockets,
        "can_take_calls": randomCafe.can_take_calls,
        "coffee_price": randomCafe.coffee_price,
    })


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def addCafe():
    newCafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        sockets=bool(request.form.get("sockets")),
        toilet=bool(request.form.get("toilet")),
        wifi=bool(request.form.get("wifi")),
        calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(newCafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def updatePrice(cafe_id):
    newPrice = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = newPrice
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    apiKey = request.args.get('api-key')
    if apiKey == "tihddhdidn":
        deleteCafe = db.session.query(Cafe).get(cafe_id)

        if deleteCafe:
            db.session.delete(deleteCafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403



@app.route("/all")
def allCafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search():
    queryLocation = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=queryLocation).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})



if __name__ == '__main__':
    app.run(debug=True)
