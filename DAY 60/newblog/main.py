import smtplib

from flask import Flask, render_template,request
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

YOUR_EMAIL = "YOUR EMAIL ADDRESS"
EMAIL_PASSWORD = "YOUR EMAIL PASSWORD"



@app.route('/')
def home():
    return render_template('index.html', post=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', method=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phoneNumber"])
        print(data["message"])
        sendEmail(data["name"], data["email"], data["phone"], data["message"])
        return f"<h1>Successfully sent your Message<h1>"
    return render_template('contact.html')


def sendEmail(name, email, phone, message):
    emailMessage = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(YOUR_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(YOUR_EMAIL, emailMessage)


# @app.route('/form-entry', method=["GET","POST"])
# def recieveData():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phoneNumber"])
#     print(data["message"])
#     return f"<h1>Successfully sent your Message<h1>"


@app.route('/post/<int:index>')
def allPost(index):
    showPosts = None
    for blogposts in posts:
        if blogposts["id"] == index:
            showPosts = blogposts
    return render_template("post.html", post=showPosts)
