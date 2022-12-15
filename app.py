
import random

from flask import Flask, render_template, request, session
import smtplib

import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(host="localhost", database="hms", user="root", password="1400")
c = db.cursor()


@app.route("/")  # mapping  or decorator
def myroot():
    return render_template("index.html")


@app.route("/reg")
def red():
    return render_template("register.html")


@app.route("/regdb", methods=['POST'])
def regdb():
    fname = request.form['fname']
    lname = request.form['lname']
    age = request.form['age']
    gender = request.form['gender']
    adhar = request.form['adhar']
    cont = request.form['contact']
    mail = request.form['email']
    address = request.form['add']
    sql = "insert into customers values('" + fname + "','" + lname + "','" + age + "','" + gender + "','" + adhar + "','" + mail + "','" + cont + "','" + address + "') "
    c.execute(sql)
    db.commit()
    ref = random.randint(1000000, 9999999)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("hemanthyegireddyad@gmail.com", "cmnwgfvoriviabzv")
    s.sendmail("hemanthyegireddyad@gmail.com", mail,
               "You have successfully registered and your reference is" + str(ref))
    s.quit()

    return render_template("staffview.html")


@app.route("/adminLogin")
def adminLogin():
    return render_template("adminLogin.html")


@app.route("/adminLoginCheck", methods=['POST'])
def adminLoginCheck():
    un = request.form['uname']
    pwd = request.form['pwd']

    if un == 'admin' and pwd == 'admin':
        return render_template("adminHome.html")

    else:
        return render_template("adminLogin.html")


@app.route("/staffview")
def staffview():
    c.execute("select * from staff")
    data = c.fetchall()
    # data is tuples in a list
    return render_template("staffview.html", d=data)


@app.route("/rooms")
def rooms():
    c.execute("select * from roomsdb")
    data = c.fetchall()
    return render_template("rooms.html", d=data)


@app.route("/updateroom", methods=['POST'])
def updateroom():
    id = request.form['rid']
    c.execute("select * from roomsdb where roomno = " + id)
    data = c.fetchall()
    return render_template("updateroom.html", d=data)


@app.route("/updateroomdb", methods=['POST'])
def updateroomdb():
    a = request.form['t1']
    b = request.form['t2']
    d = request.form['t3']
    e = request.form['t4']
    f = request.form['t5']

    # print(sql)
    sql = "update roomsdb set roomtype = %s , strength = %s , warden = %s , cost= %s where roomno = %s"
    data = (b, d, e, f, a)
    c.execute(sql, data)

    # "update roomsdb set roomtype='" + b + "',strength='" + d + "',warden='" + e + "',cost='"+f+"' ,  where roomno=" + a)
    db.commit()

    c.execute("select * from roomsdb")
    data = c.fetchall()
    return render_template("rooms.html", d=data)


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/canteen")
def canteen():
    return render_template("canteen.html")


@app.route("/internet")
def internet():
    return render_template("internet.html")


@app.route("/spa")
def spa():
    return render_template("spa.html")


@app.route("/aircon")
def aircon():
    return render_template("aircon.html")


@app.route("/security")
def security():
    return render_template("sequrity.html")


@app.route("/staffportel")
def staff():
    return render_template("slogin.html")


@app.route("/stafflog", methods=['POST'])
def stafflog():
    uname = request.form['uname']
    pas = request.form['pwd']

    sql = "SELECT * FROM `staff` WHERE sname='" + uname + "' and sid='" + pas + "'"
    c.execute(sql)
    d = c.fetchall()

    if len(d) > 0:
        return render_template("staffpage.html")
    else:
        return render_template("slogin.html")


@app.route("/roompic")
def roompic():
    return "room pics"


@app.route("/updatestaff", methods=['POST'])
def updatestaff():
    sd = request.form['sid']
    # sql = "select * from staff where sname = " + sid
    c.execute("select * from staff where sid = " + sd)

    data1 = c.fetchall()

    return render_template("updatestaff.html", d=data1)


@app.route("/updatestaffdb", methods=['POST'])
def updatestaffdb():
    sid = request.form['t1']
    sname = request.form['t2']
    des = request.form['t3']
    sal = request.form['t4']
    cont = request.form['t5']
    add = request.form['t6']

    sql = "update staff set  sname=%s, sdesig=%s, ssal=%s, scon=%s , sadd=%s where sid=%s"
    data = (sname, des, sal, cont, add, sid)

    c.execute(sql, data)
    c.execute("select * from staff")
    data1 = c.fetchall()
    print(data1)
    return render_template("staffview.html", d=data1)


@app.route("/terminate", methods=['POST'])
def terminate():
    id = request.form['sid']
    c.execute("delete from staff where sid = " + id)
    db.commit()
    return render_template("terminate.html")


@app.route("/addstaff")
def addstaff():
    return render_template("addstaff.html")


@app.route("/addstaffdb", methods=['POST'])
def addstaffdb():
    t7 = request.form['t1']
    t8 = request.form['t2']
    t9 = request.form['t3']
    t10 = request.form['t4']
    t11 = request.form['t5']
    t12 = request.form['t6']
    t13 = request.form['t7']

    sql = "insert into staff values('" + t7 + "','" + t8 + "','" + t9 + "','" + t10 + "','" + t11 + "','" + t12 + "', '" + t13 + "')"
    c.execute(sql)
    db.commit()

    return render_template("addstaff.html")


@app.route("/customers")
def customers():
    sql = "select * from customers"
    c.execute(sql)
    data = c.fetchall()
    return render_template("/customerview.html", d=data)


@app.route("/addroom")
def addroom():
    return render_template("addroom.html")


@app.route("/addroomdb", methods=['POST'])
def addroomdb():
    t1 = request.form['t1']
    t2 = request.form['t2']
    t3 = request.form['t3']
    t4 = request.form['t4']
    t5 = request.form['t5']

    sql = "insert into roomsdb values('" + t1 + "', '" + t2 + "', '" + t3 + "', '" + t4 + "','" + t5 + "')"
    c.execute(sql)
    db.commit()
    c.execute("select * from roomsdb where roomno =  " + t1)
    data = c.fetchall()

    return render_template("newroom.html", d=data)


@app.route("/cuslog")
def cuslog():
    return render_template("/cuslog.html")


# @app.route("/customercheck")
# def customercheck():
#
#     uname = request.form['uname']
#     pwd = request.form['pwd']
#
#     sql = "select * from customers where contact = %s and email = %s"
#     data=[uname,pwd]
#     c.execute(sql,data)
#     c.fetchall()
#     if len(data>0):
#         session(email=)
#         return render_template()


if __name__ == '__main__':
    app.run(port=8999, debug=True)
