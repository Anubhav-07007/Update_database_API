from flask import Flask,request,jsonify
import mysql.connector as conn

app=Flask(__name__)

mydb=conn.connect(host="localhost",user="root",passwd="ar@66007")

cursor=mydb.cursor()

cursor.execute("use anubhav")


@app.route('/insert',methods=["POST","GET"])

def insert():
    if request.method=="POST":
        empid=request.json['empid']
        empname=request.json['empname']
        emp_mail=request.json['emp_mail']
        emp_phone=request.json['emp_phone']
        cursor.execute('insert into anubhav.python values(%s,%s,%s,%s)',(empid,empname,emp_mail,emp_phone))
        mydb.commit()
        return jsonify(str('done'))

@app.route('/update',methods=["POST","GET"])

def update():
    if request.method=="POST":
        empid=request.json['empid']
        empname=request.json['empname']
        cursor.execute('update python set empid= %s where empname=%s',(empid,empname))
        mydb.commit()
        return jsonify(str('done'))

@app.route('/delete',methods=["POST","GET"])
def delete_record():
    if request.method=="POST":
        empid=request.json['empid']
        cursor.execute('delete from python where empid=%s',(empid,))
        mydb.commit()
        return jsonify(str("Successfully done"))

if __name__=='__main__':
    app.run(port=5001)