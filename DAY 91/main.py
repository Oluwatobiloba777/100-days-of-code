import extcolors
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/images"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


test_img_path = "test.jpg"
test_hex = ['#de9b6e', '#004032', '#010000', '#fffeff',
            '#75674a', '#4e8f71', '#8a4d0e', '#afa3ad', '#441800', '#004800']
test_percent = [53.91, 16.12, 11.52, 9.38, 8.06, 0.38, 0.3, 0.29, 0.01, 0.01]


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_colors(image_path):
    colors, pixel_count = extcolors.extract_from_path(image_path)

    hex_colors = []
    total_pixels = 0

    for color in colors:
        total_pixels += color[1]

    for color in colors:
        hex_colors.append((RGB2HEX(color[0]), round((color[1] / total_pixels) * 100, 2)))

    top_10 = hex_colors[:10]

    return top_10


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    files = [f for f in os.listdir("static/images") if os.path.isfile(os.path.join("static/images", f))]
    for file in files:
        if file != test_img_path:
            os.remove(f"static/images/{file}")
    return render_template("index.html", filename=test_img_path, hex_codes=test_hex, percent=test_percent)


@app.route('/<prev_filename>', methods=['POST'])
def upload_image(prev_filename):
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        top_10_tups = get_colors(f"static/images/{filename}")
        hex_codes = [color[0] for color in top_10_tups]
        percent = [color[1] for color in top_10_tups]

        return render_template('index.html', filename=filename, hex_codes=hex_codes, percent=percent)
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='images/' + filename), code=301)

