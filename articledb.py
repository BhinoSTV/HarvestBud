from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///article.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), unique=True, nullable=False)
    gwterm = db.Column(db.String(50), unique=False, nullable=False)
    authors = db.Column(db.String(150), unique=False, nullable=False)
    publisher = db.Column(db.String(100), unique=False, nullable=True)
    study_area =  db.Column(db.String(30), unique=False)
    methodology = db.Column(db.String(50), unique=False, nullable=True)
    doi = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=True)
    number_factor = db.Column(db.Integer, nullable=True)
    factors = db.relationship('Factor', backref='author', lazy=True)

    def __repr__(self):
        return f"Article('{self.title}', '{self.gwterm}', '{self.authors}', '{self.publisher}', '{self.study_area}','{self.methodology}','{self.doi}' ,'{self.year}', '{self.number_factor}')"


class Factor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

    def __repr__(self):
        return f"Factor('{self.name}')"
    

class FactorInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


