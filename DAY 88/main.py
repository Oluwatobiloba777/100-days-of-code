from flask import Flask, request, render_template,redirect
from models import db, TodoList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    #could also serve as retrieve page still thinking sha
    new_list = TodoList.query.all()
    return render_template('index.html', new_list=new_list)


@app.route('/todolist/create', methods =['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_list = TodoList(title=title,content=content)
        db.session.add(new_list)
        db.session.commit()
        #check if you want the index to show data or show another page for data
        return redirect('/')

@app.route('/todolist')
def Retrievelist():
    #use for loop to retrieve data in html and create a new html i like sha, make we dey look
    new_list = TodoList.query.all()
    return render_template('todolist.html', new_list=new_list)


#update
@app.route('/todolist/<int:id>/update', methods = ['GET', 'POST'])
def update(id):
    new_list = TodoList.query.filter_by(user_id=id)
    if request.method == 'POST':
        if new_list:
            db.session.delete(new_list)
            db.session.commit()

            title = request.form['title']
            content = request.form['content']
            new_list = TodoList(title=title, content=content)


            db.session.add(new_list)
            db.session.commit()
            return redirect(f'todolist/{id}')
    return render_template('update.html', new_list=new_list)


#delete
@app.route('todolist/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    new_list = TodoList.query.filter_by(user_id=id)
    if request.method == 'POST':
        if new_list:
            db.session.delete(new_list)
            db.session.commit()
            return redirect('/todolist')
    return render_template('delete.html')

