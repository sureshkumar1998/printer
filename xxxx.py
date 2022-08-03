import qrcode
import psycopg2
from flask import Flask,render_template,redirect,request
import datetime
import re
date = str(datetime.datetime.now())
to = date.split(" ")
today = (to[1].replace(".",","))
n=today.split(",")
time=(n[0].replace(":","_"))
print(time)


global conn,cur,m
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('print.html')

@app.route('/print',methods=["POST",'GET'])
def dis():
    global n,n1,n2,n3,conn,cur
    login()
    if request.method=='POST':
        n=request.form.get('name')
        n1=request.form.get('employee')
        n2=request.form.get('team')
        n3=n+n1+n2
        print(n3)
        if n3=="":
            n="Please enter the data"
            return render_template('print.html',data=n)
        elif (re.search("[a-zA-Z][0-9]",n1)):
            qr=qrcode.QRCode(box_size=50,border=6)
            qr.add_data(n3)
            qr.make(fit=True)
            qr_code=qr.make_image(fill_color='black',back_color='white')
            image=qr_code.save(f'/home/suresh/Music/print/static/images/image{time}.png')
            cur.execute("select * from company order by id desc limit 1;")
            rows = cur.fetchall()
            for row in rows:
                count=row[0]+1
                cur.execute(f"INSERT INTO COMPANY (ID,NAME,EMPLOYEE,TEAM) \
                                VALUES ({count}, '{n}','{n1}','{n2}' )");
                conn.commit()
            return render_template('Dis.html',name=n,employee=n1,team=n2,pic=f'/images/image{time}.png')
        else:
            k="Invalid Id"
            return render_template('print.html',k1=k)
@app.route('/data',methods=["POST","GET"])
def data():
    global conn,cur,m,A,val1
    login()
    if request.method=='POST':
        m=request.form.get('name')
        print(m)
        cur.execute(f"SELECT * FROM COMPANY WHERE NAME='{m}';")
        rows = cur.fetchall()
        print(rows)
        if request.form['submit'] == 'submit':
            if rows==[]:
                n="Invalid Data"
                return render_template('Dis.html',data=n)
            else:
                row=list(rows)
                for i in row:
                    a=i[0]
                    b=i[1]
                    c=i[2]
                    d=i[3]
                    print(a,"\n",b,"\n",c,"\n",d)
                    qr=qrcode.QRCode(box_size=50,border=6)
                    qr.add_data(row)
                    qr.make(fit=True)
                    qr_code=qr.make_image(fill_color='black',back_color='white')
                    image1=qr_code.save(f'/home/suresh/Music/print/static/images/image111.png')
                    conn.commit()
                    conn.close()       
                    return render_template('data.html',pic1='/images/image111.png',B=b,C=c,D=d)
        elif request.form['submit'] == 'edit':
            if rows==[]:
                kk="Invalid Data"
                return render_template('Dis.html',k1=kk)
            else:
                data=list(rows)
                for i in data:
                    A=i[0]
                    B=i[1]
                    C=i[2]
                    D=i[3]
                    print(A,"\n",B,"\n",C,"\n",D)
                    conn.commit()
                    conn.close()
                    return render_template('edit.html',pic1='/images/image111.png',b=B,c=C,d=D)

        elif request.form['submit'] == 'delete':
            if rows==[]:
                val1="Invalid Data"
                return render_template('Dis.html',v=val1)
            else:
                cur.execute(f"DELETE FROM COMPANY WHERE NAME='{m}';")
                conn.commit()
                conn.close()       
                val="DELETE SUCCESSFULLY"
                return render_template('Dis.html',v1=val)

@app.route('/edit',methods=["POST"])
def edit():
    global conn,cur,A,val1
    login()
    if request.method=='POST':
        name=request.form.get('name')
        emp=request.form.get('employee')
        team=request.form.get('team')
        result="Update Successfully"
        cur.execute(f"UPDATE COMPANY set NAME='{name}',EMPLOYEE='{emp}' , TEAM='{team}' where ID = {A};")
        conn.commit()
        conn.close()  
        return render_template('edit.html',update=result)

@app.route('/back',methods=["POST"])
def back():
    return redirect("/")

@app.route('/img',methods=["POST"])
def back1():
    return render_template('Dis.html')


def login():
    global conn,cur
    conn = psycopg2.connect(database="testdb", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
    cur=conn.cursor()

if __name__=='__main__':
    app.run(debug=True,host='127.0.0.2', port=5008)