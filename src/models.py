from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        return '<Todo %r>' % self.text

    def serialize(self):
        return {
            "text": self.text,
            "done": self.done,
            "id": self.id
        }