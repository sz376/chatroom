# models.py
import flask_sqlalchemy
from app import db


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(225))
    pfp = db.Column(db.String(225))
    message = db.Column(db.Text)
    link = db.Column(db.Text)
    image = db.Column(db.Text)

    def __init__(self, u, p, m, l, i):
        self.user = u
        self.pfp = p
        self.message = m
        self.link = l
        self.image = i

    def __repr__(self):
        return "<User: %s>" % self.user
