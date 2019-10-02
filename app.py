from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,InputRequired
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from form import LoginForm, EmployeeForm, ItemsForm, SupplierForm
from models import *

bootstrap = Bootstrap()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'final'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/finals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap.init_app(app)
db.init_app(app)



@app.route("/admin")
def admin():
    form = LoginForm()
    return render_template('admin.html', title='Admin',form=form)

@app.route("/employee")
def employee():
    myUser=User.query.all()
    form = EmployeeForm()
    return render_template('employee.html', title='Employee',form=form,myUser=myUser)

@app.route("/item")
def item():
    myItem = Item.query.all()
    forms = ItemsForm()
    return render_template('item.html', title='Items',form=forms,myItem=myItem)

@app.route("/supplier")
def supplier():
    mySupplier=Supplier.query.all()
    form = SupplierForm()
    return render_template('supplier.html', title='Supplier',form=form,mySupplier=mySupplier)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(emp_username=form.username.data).first()
        if user:
            if user.emp_password==form.password.data:
                return render_template('admin.html',form=form)
            else:
                return "<h1><center>INVALID!</center></h1>"
        else:
            return "<h1><center>INVALID!</center></h1>"
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
