from flask import Flask, render_template
import requests

app = Flask(__name__)


def getData():
    blogUrl = "https://www.npoint.io/docs/c790b4d5cab58020d391"
    response = requests.get(blogUrl)
    blogData = response.json()
    return blogData


@app.route('/')
def home():
    return render_template("index.html", posts=getData())

@app.route('/post/<int:post_id>')
def postData(post_id):
    post = getData()[post_id-1]
    return render_template("post.html", posts=getData(), postss=post)

if __name__ == "__main__":
    app.run(debug=True)
