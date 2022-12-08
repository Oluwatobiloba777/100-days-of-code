from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TodoList(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(250))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"{self.id}"
