from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class AllEmployees(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    workflow = db.Column(db.Float, nullable=True)

    def __init__(self, name, department, workflow=None):
        self.name = name
        self.department = department
        self.workflow = workflow

    def __repr__(self):
        return f"{self.name} - {self.department}"
