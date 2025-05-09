from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired

class empLoginform(FlaskForm):
    loginID = StringField("Login ID: ", validators=[InputRequired()])
    Password = PasswordField("Password: ", validators=[InputRequired()])
    Submit = SubmitField("Submit")

class UpdateForm(FlaskForm):
    ID = StringField("Enter your Employee ID: ", validators=[InputRequired()])
    column = SelectField("Select which column you want to change data: ", choices=["First_name", "Last_name", "E_mail", "Phone_Number", "Address"])
    newdata = StringField("Enter newdata: ", validators=[InputRequired()])
    submit = SubmitField("submit")

class UpdatebanksForm(FlaskForm):
    ID = StringField("Enter your Employee ID ", validators=[InputRequired()])
    column = SelectField("Select which column you want to change data: ", choices=["First_name", "Last_name", "Bank", "Branch", "IBAN", "Account_Number", "PSC"])
    newdata = StringField("Enter newdata: ", validators=[InputRequired()])
    submit = SubmitField("submit")

class Showform(FlaskForm):
    ID = StringField("Enter your Employee ID ", validators=[InputRequired()])
    submit = SubmitField("Submit")