from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template('index.html', post=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def allPost(index):
    showPosts = None
    for blogposts in posts:
        if blogposts["id"] == index:
            showPosts = blogposts
    return render_template("post.html", post=showPosts)
