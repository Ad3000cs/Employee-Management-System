"""
IMPORTANT !!

My program has two modes - Admin and Employee

Admin Login ID - am03

Admin Password - am201

Employee Login ID - Cameron

Employee Password - EMSE03

Employee ID (asked when employee updates/sees/deletes his own data OR data is updated/deleted by Admin) - E03

*******************************************************************************************************************************************************************

I AM GIVING SAMPLE NEW DATA TO MAKE IT EASIER FOR YOU TO REGISTER AN EMPLOYEE (CAN ONLY BE DONE BY ADMIN). SEE THAT THIS DATA IS USED AS IT IS AT RIGHT PLACES:

REGISTRATION 
ID - E01
Login ID - Jack
PASSWORD - EMSE01 (ENTER THIS TWO TIMES AS ASKED BY PROGRAM)

DETAILS
ID - E01 
First Name - Jack
Last Name - Cummins 
E - mail - jackcummins123@gmail.com 
Phone Number - +353 874357432 
Address - House 12, Magazine Road
County - Cork
Join Date - 01-04-2023 --> dd-mm-yyyy
Department - Software Development
Role - Code Tester
Type - Permanent
Level - Junior
Total leaves - 30
Taken leaves - 4
Left leaves - 26
LEAVE THE Termination date empty, employee is permanent. If you want, you can change ID, First and last names and type as Freelance
to give Termination date 

Bank Details
ID - E01
First Name - Jack
Last Name - Cummins
Bank - AIB
Branch - Western Gateway Building
IBAN - IE95AIB995829864181
Account Number - 1129809873
PSC - IE2423567E

Salary Details
ID - E01
CTC - 42000
House rent allowance - 9000
Travel allowance - 3000
Taxable Income - 30000
Tax Rate - 40
In hand - 18000

KINDLY LET ME KNOW IF FURTHER ASSISTANCE REQUIRED AT 123104113@umail.ucc.ie
"""


#--------------------------------------------- PROGRAM STARTS BELOW ---------------------------------------------------------------------------------

from flask import Flask, render_template, url_for, session, redirect, url_for, g, request
from flask_session import Session
from database import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from empforms import empLoginform, UpdatebanksForm, UpdateForm, Showform
from adminforms import Loginform, RegisterForm, DetailsForm, BankForm, SalaryForm, DeletedetailsForm, UpdatedetailsForm, UpdatesalaryForm, UpdatebankForm

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.before_request
def load_logged_in_user():
    g.user = session.get("loginID", None)
    g.admin = session.get("ID")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employee")
def employee():
    return render_template("employee.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/licence")
def citations():
    return render_template("licences.html")


@app.route("/salarydetails", methods = ["GET", "POST"])
def empsalary():
    form = SalaryForm()
    message = ""
    if form.validate_on_submit():
        ID = form.ID.data
        CTC = form.CTC.data
        House_rent_allowance = form.House_rent_allowance.data
        Travel_allowance = form.Travel_allowance.data
        Taxable_income = form.Taxable_income.data
        Tax_rate = form.Tax_rate.data
        In_hand = form.In_hand.data
        db = get_db()
        db.execute(""" INSERT INTO Salary(ID, CTC, House_rent_allowance, Travel_allowance, Taxable_income, Tax_rate, In_hand) VALUES (?,?,?,?,?,?,?)""",(ID, CTC, House_rent_allowance, Travel_allowance, Taxable_income, Tax_rate, In_hand))
        db.commit()
        message += "Data added successfully"
        return redirect(url_for('admin'))
    return render_template("salary.html", form=form)

@app.route("/bankdetails", methods = ["GET", "POST"])
def empbank():
    form = BankForm()
    if form.validate_on_submit():
        ID = form.ID.data
        First_name = form.First_name.data
        Last_name = form.Last_name.data
        Bank = form.Bank.data
        Branch = form.Branch.data
        IBAN = form.IBAN.data
        Account_Number = form.Account_Number.data
        PSC = form.PSC.data
        db = get_db()
        db.execute("""INSERT INTO Bank_details(ID, First_name, Last_name, Bank, Branch, IBAN, Account_Number, PSC) VALUES (?,?,?,?,?,?,?,?)""",(ID, First_name, Last_name, Bank, Branch, IBAN, Account_Number, PSC))
        db.commit()
        return redirect(url_for("empsalary"))
    return render_template("bank.html", form = form)

@app.route("/enterdetails", methods = ["GET", "POST"])
def empdetails():
    form = DetailsForm()
    message = ""
    if form.validate_on_submit():
        ID = form.ID.data
        First_name = form.First_name.data
        Last_name = form.Last_name.data
        E_mail = form.E_mail.data
        Phone_Number = form.Phone_Number.data
        Address = form.Address.data
        County = form.County.data
        Join_date = form.Join_date.data
        Department = form.Department.data
        Role = form.Role.data
        Type = form.Type.data
        level = form.level.data
        Total_leaves = form.Total_leaves.data
        Taken_leaves = form.Taken_leaves.data
        Left_leaves = form.Left_leaves.data
        Termination_date = form.Termination_date.data
        db = get_db()
        if Termination_date == "":
            db.execute("""INSERT INTO details(ID, First_name, Last_name, E_mail, Phone_Number, Address, County, Join_date, Department, Role, Type, level, Total_leaves, Taken_leaves, Left_leaves)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", (ID, First_name, Last_name, E_mail, Phone_Number, Address, County, Join_date, Department, Role, Type,level, Total_leaves, Taken_leaves, Left_leaves))
        else:
            db.execute("""INSERT INTO details(ID, First_name, Last_name, E_mail, Phone_Number, Address, County, Join_date, Department, Role, Type, level, Total_leaves, Taken_leaves, Left_leaves, Termination_date)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", (ID, First_name, Last_name, E_mail, Phone_Number, Address, County, Join_date, Department, Role, Type,level, Total_leaves, Taken_leaves, Left_leaves, Termination_date))
        message += "Employee details successfully added"
        db.commit()
        return redirect(url_for("empbank"))
    return render_template("details.html", form = form, message = message)

@app.route("/showdetails", methods = ["GET", "POST"])

def all_details():
    db = get_db()
    details = db.execute("""SELECT * FROM details;""").fetchall()
    return render_template("showdetails.html", caption = "Employee Details", details = details)

@app.route("/showsalary", methods = ["GET", "POST"])
def pay():
    db = get_db()
    payment = db.execute("""SELECT * FROM Salary;""").fetchall()
    return render_template("showsalary.html", caption = "Salary Details", payment = payment)

@app.route("/showbankdetails", methods = ["GET", "POST"])
def showbank():
    db = get_db()
    banks = db.execute("""SELECT * FROM Bank_details;""").fetchall()
    return render_template("showbank.html", caption = "Bank Details", banks = banks)

@app.route("/updatedetails", methods = ["GET", "POST"])
def updetails():
    message = ""
    form = UpdatedetailsForm()
    if form.validate_on_submit():
        ID = form.ID.data
        column = form.column.data
        newdata = form.newdata.data
        db = get_db()
        cursor = db.cursor()
        if column == "First_name":
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column), (newdata, ID))
            cursor.execute("""UPDATE emplogininfo SET loginID = ? WHERE empID = ?;""", (newdata, ID))
            db.commit()
        elif column == "Last_name":
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column), (newdata, ID))
            db.commit()
        elif column == "ID":
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column), (newdata, ID))
            cursor.execute("""UPDATE Salary SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE emplogininfo SET empID = ? WHERE empID = ?;""",(newdata, ID))
            db.commit()
        else:
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit()
        message += "Data updated successfully!" 
    return render_template("update.html", form = form, message = message)

@app.route("/updatesalary", methods = ["GET", "POST"])
def upsalary():
    message = ""
    form = UpdatesalaryForm()
    if form.validate_on_submit():
        ID = form.ID.data
        column = form.column.data
        newdata = form.newdata.data
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""UPDATE Salary SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
        db.commit()
        cursor.execute("""UPDATE Salary SET Taxable_income = CTC - (House_rent_allowance + Travel_allowance)
                        WHERE ID = ?;""", (ID,))
        db.commit()
        cursor.execute("""UPDATE Salary SET In_hand = Taxable_income - (Taxable_income * (Tax_rate/100.00)) WHERE ID = ?;""", (ID,))
        db.commit()
        
        message += "Data updated successfully!" 
    return render_template("update.html", form = form, message = message)

@app.route("/updatebanks", methods = ["GET", "POST"])
def upbank():
    message = ""
    form = UpdatebankForm()
    if form.validate_on_submit():
        ID = form.ID.data
        column = form.column.data
        newdata = form.newdata.data
        db = get_db()
        cursor = db.cursor()
        if column == "First_name" or column == "Last_name":
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit()
        else:
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit()
        message += "Data updated successfully!" 
    return render_template("update.html", form = form, message = message)

@app.route("/showIDdetails", methods = ["GET", "POST"])

def your_details():
    form = Showform()
    ID = form.ID.data
    if form.validate_on_submit():

        db = get_db()
        detail = db.execute("""SELECT * FROM details WHERE ID = ?;""", (ID,)).fetchone()

        return render_template("detail.html", detail = detail)
    return render_template("showempdata.html", form = form)

@app.route("/showIDsalary", methods = ["GET", "POST"])
def yourpay():
    form = Showform()
    ID = form.ID.data
    if form.validate_on_submit():
        db = get_db()
        pay = db.execute("""SELECT * FROM Salary WHERE ID = ?;""", (ID,)).fetchone()

        return render_template("pay.html", pay = pay)
    return render_template("showempdata.html", form = form)

@app.route("/showIDbankdetails", methods = ["GET", "POST"])
def yourbank():
    form = Showform()
    ID = form.ID.data
    if form.validate_on_submit():

        db = get_db()
        bank = db.execute("""SELECT * FROM Bank_details WHERE ID = ?;""", (ID,)).fetchone()

        return render_template("seeyourbank.html", caption = "Your Bank Details", bank = bank)
    return render_template("showempdata.html", form = form)

@app.route("/individual", methods = ["GET", "POST"])
def individualdetails():
    message = ""
    form = UpdateForm()
    if form.validate_on_submit():
        ID = form.ID.data
        column = form.column.data
        newdata = form.newdata.data
        db = get_db()
        cursor = db.cursor()
        if column == "First_name":
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column), (newdata, ID))
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE emplogininfo SET loginID = ? WHERE empID = ?;""", (newdata, ID))
            db.commit()
        elif column == "Last_name":
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column), (newdata, ID))
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit()
        else:
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit()
        message += "Data updated successfully!" 
    return render_template("update.html", form = form, message = message)

@app.route("/individualbank", methods = ["GET", "POST"])
def individualbank():
    message = ""
    form = UpdatebanksForm()
    if form.validate_on_submit():
        ID = form.ID.data
        column = form.column.data
        newdata = form.newdata.data
        db = get_db()
        cursor = db.cursor()
        if column == "First_name" or column == "Last_name":
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            cursor.execute("""UPDATE details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit()
        else:
            cursor.execute("""UPDATE Bank_details SET {} = ? WHERE ID = ?;""".format(column) ,(newdata, ID))
            db.commit() 
        message += "Data updated successfully!"
    return render_template("update.html", form = form, message = message)

@app.route("/deletedetails", methods = ["GET", "POST"])
def deldetails():
    form = DeletedetailsForm()
    message = ""
    if form.validate_on_submit():
        ID = form.ID.data
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM details WHERE ID = ?;", (ID,))
        cursor.execute("DELETE FROM Bank_details WHERE ID = ?;", (ID,))
        cursor.execute("DELETE FROM Salary WHERE ID = ?;", (ID,))
        cursor.execute("DELETE FROM emplogininfo WHERE empID = ?; ", (ID,))
        db.commit()
        message += "Data deleted successfully, press back button to go back"
    return render_template("delete.html", form = form, message = message)

@app.route("/emplogin", methods = ["GET", "POST"])
def emplog():
    form = empLoginform()
    if form.validate_on_submit():
        loginID = form.loginID.data
        password = form.Password.data
        db = get_db()
        user = db.execute(""" SELECT * FROM emplogininfo WHERE loginID = ?; """, (loginID,)).fetchone()
        if user is None:
            form.loginID.errors.append("No such user name")
        elif not check_password_hash(user["Password"],password):
            form.Password.errors.append("Incorrect Password")
        else:
            session.clear()
            session["loginID"] = loginID
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("employee") 
            return redirect(next_page)
    return render_template ("emplogin.html", form = form)

@app.route("/adminlogin", methods = ["GET", "POST"])
def adminlog():
    form = Loginform()
    if form.validate_on_submit():
        ID = form.ID.data
        Password = form.Password.data
        db = get_db()
        user = db.execute(""" SELECT * FROM Admin WHERE ID = ?; """, (ID,)).fetchone()
        if user is None:
            form.ID.errors.append("No such user name")
        elif not check_password_hash(user["Password"], Password):
            form.Password.errors.append("Incorrect Password")
        else:
            session.clear()
            session["ID"] = ID
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("admin") 
            return redirect(next_page)
    return render_template ("adminform.html", form = form)

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        empID = form.empID.data
        loginID = form.loginID.data
        Password = form.Password.data
        db = get_db()
        conflict_user = db.execute("""SELECT * FROM emplogininfo WHERE empID = ?;""", (empID, )).fetchone()
        if conflict_user is not None:
            form.empID.errors.append("Employee ID already taken")
        else:
            db.execute("""INSERT INTO emplogininfo(empID, loginID, Password) VALUES (?, ?, ?); """, (empID, loginID, generate_password_hash(Password)))
            db.commit()
            return redirect(url_for("empdetails"))
    return render_template("register.html", form = form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


