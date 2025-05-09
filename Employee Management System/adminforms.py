from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField,IntegerField, SelectField, RadioField
from wtforms.validators import InputRequired, EqualTo, Length

class Loginform(FlaskForm):
    ID = StringField("Login ID: ", validators=[InputRequired()])
    Password = PasswordField("Password: ", validators=[InputRequired()])
    Submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    empID = StringField("Enter Employee ID: ", validators=[InputRequired()])
    loginID = StringField("Enter Login ID: ", validators=[InputRequired()])
    Password = PasswordField("Enter Passoword: ", validators=[InputRequired()])
    Password2 = PasswordField("Re - enter Password: ", validators=[InputRequired(), EqualTo("Password")])
    Submit = SubmitField("Submit")

class DetailsForm(FlaskForm):
    ID = StringField("Enter Employee ID: ", validators=[InputRequired()])
    First_name = StringField("Enter First Name: ", validators=[InputRequired()])
    Last_name = StringField("Enter Last Name: ", validators=[InputRequired()])
    E_mail = StringField("Enter E-mail: ", validators=[InputRequired()])
    Phone_Number = StringField("Enter Phone Number: ", validators=[InputRequired()])
    Address = StringField("Enter Address: ", validators=[InputRequired()])
    County = StringField("Enter County: ", validators=[InputRequired()])
    Join_date = DateField("Enter Join Date: ", validators=[InputRequired()])
    Department = StringField("Enter Department: ", validators=[InputRequired()])
    Role = StringField("Enter Role: ", validators=[InputRequired()])
    Type = StringField("Enter Type: ", validators=[InputRequired()])
    level = StringField("Enter level: ", validators=[InputRequired()])
    Total_leaves = IntegerField("Enter Total Leaves: ", validators=[InputRequired()])
    Taken_leaves = IntegerField("Enter Taken Leaves: ", validators=[InputRequired()])
    Left_leaves = IntegerField("Enter Left Leaves: ", validators=[InputRequired()])
    Termination_date = StringField("Enter Termination date if employee not permanent (separate with hyphens): ")
    submit = SubmitField("Submit")

class BankForm(FlaskForm):
    ID = StringField("Enter Employee ID: ", validators=[InputRequired()])
    First_name = StringField("Enter First Name: ", validators=[InputRequired()])
    Last_name = StringField("Enter Last Name: ", validators=[InputRequired()])
    Bank = StringField("Enter Bank name: ", validators=[InputRequired()])
    Branch = StringField("Enter Bank Branch: ", validators=[InputRequired()])
    IBAN = StringField("Enter IBAN: ", validators=[InputRequired(), Length(min = 19, max=19)])
    Account_Number = StringField("Enter Account Number: ", validators=[InputRequired(), Length(min = 10, max=10)])
    PSC = StringField("Enter PSC number: ", validators=[InputRequired(), Length(min = 10, max=10)])
    submit = SubmitField("Submit")
    
class SalaryForm(FlaskForm):
    ID = StringField("Enter Employee ID: ", validators=[InputRequired()])
    CTC = FloatField("Enter Annual CTC: ", validators=[InputRequired()])
    House_rent_allowance = FloatField("Enter House rent allowance: ", validators=[InputRequired()])
    Travel_allowance = FloatField("Enter Travel allowance: ", validators=[InputRequired()])
    Taxable_income = FloatField("Enter Taxable Income: ", validators=[InputRequired()])
    Tax_rate = FloatField("Enter Tax rate: ", validators=[InputRequired()])
    In_hand = FloatField("Enter In hand Salary: ", validators=[InputRequired()])
    submit = SubmitField("Submit")

class UpdatedetailsForm(FlaskForm):
    ID = StringField("Enter the ID for which you want to change data: ", validators=[InputRequired()])
    column = SelectField("Select which column you want to change data: ", choices=["ID", "First_name", "Last_name", "E_mail", "Phone_Number", "Address", "County", "Join_date", "Department", "Role", "Type", "level", "Total_leaves", "Taken_leaves", "Left_leaves", "Termination_date"])
    newdata = StringField("Enter newdata: ", validators=[InputRequired()])
    submit = SubmitField("submit")

class UpdatesalaryForm(FlaskForm):
    ID = StringField("Enter the ID for which you want to change data: ", validators=[InputRequired()])
    column = SelectField("Select which column you want to change data: ", choices=["CTC", "House_rent_allowance", "Travel_allowance"])
    newdata = StringField("Enter newdata: ", validators=[InputRequired()])
    submit = SubmitField("submit")

class UpdatebankForm(FlaskForm):
    ID = StringField("Enter the ID for which you want to change data: ", validators=[InputRequired()])
    column = SelectField("Select which column you want to change data: ", choices=["First_name", "Last_name", "Bank", "Branch", "IBAN", "Account_Number", "PSC"])
    newdata = StringField("Enter newdata: ", validators=[InputRequired()])
    submit = SubmitField("submit")
    
class DeletedetailsForm(FlaskForm):
    ID = StringField("Enter employee ID to delete details: ", validators=[InputRequired()])
    submit = SubmitField("submit")