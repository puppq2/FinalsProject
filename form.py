from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeForm(FlaskForm):
    add = SubmitField('Add Employee')
    search = StringField('Search',
                        validators=[DataRequired()])
    employeeid = StringField('EmployeeID',
                        validators=[DataRequired() ])
    fname = StringField('FirstName',
                           validators=[DataRequired() ])
    lname = StringField('LastName',
                           validators=[DataRequired() ])
    email = StringField('Email',
                           validators=[DataRequired() ])
    username = StringField('Username',
                           validators=[DataRequired() ])
    password = StringField('Password',
                           validators=[DataRequired() ])

class ItemsForm(FlaskForm):
    search = StringField('Search',
                        validators=[DataRequired()])
    icode = StringField('ItemCode',
                        validators=[DataRequired() ])
    iname = StringField('ItemName',
                           validators=[DataRequired() ])
    ibrand = StringField('ItemBrand',
                           validators=[DataRequired() ])
    iprice = StringField('ItemPrice',
                           validators=[DataRequired() ])

class SupplierForm(FlaskForm):
    search = StringField('Search',
                        validators=[DataRequired()])
    supp_id = StringField('SupplierID',
                        validators=[DataRequired() ])
    supp_name = StringField('SupplierName',
                           validators=[DataRequired() ])
    supp_contact = StringField('SupplierContact',
                           validators=[DataRequired() ])
    supp_email = StringField('SupplierEmail',
                           validators=[DataRequired() ])

if __name__ == "__main__":
    print(__name__)
