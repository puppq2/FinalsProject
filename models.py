from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "employee"
    emp_id = db.Column(db.Integer, primary_key=True, unique=True)
    emp_fname = db.Column(db.String(80), nullable=False)
    emp_lname = db.Column(db.String(80), nullable=False)
    emp_email = db.Column(db.String(121), unique=True, nullable=False)
    emp_username = db.Column(db.String(80), unique=True, nullable=False)
    emp_password = db.Column(db.String(120), nullable=False)

def __repr__(self):
    return "<User %r>" % self.emp_username

class Item(db.Model):
    __tablename__ = "item"
    item_code = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    item_brand = db.Column(db.String(80), unique=True, nullable=False)
    item_price = db.Column(db.Float(121), nullable=False)

def __repr__(self):
    return "<Prod %r>" % self.item_code

class Supplier(db.Model):
    __tablename__ = "supplier"
    supplier_id = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    supplier_name = db.Column(db.String(80), unique=True, nullable=False)
    supplier_contact = db.Column(db.Integer(), unique=True, nullable=False)
    supplier_email = db.Column(db.String(121), nullable=False)

def __repr__(self):
    return "<Prod %r>" % self.supplier_id
