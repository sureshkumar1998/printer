import psycopg2


conn = psycopg2.connect(database="testdb", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
cur=conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       EMPLOYEE       TEXT     NOT NULL,
#       TEAM         TEXT     NOT NULL);''')
# conn.commit()
print("success")
# cur.execute(f"INSERT INTO COMPANY (ID,NAME,EMPLOYEE,TEAM) \
#                         VALUES ('1', 'suresh','555','smart' )");
# conn.commit()
# m='suresh'
cur.execute(f"select * from company WHERE NAME='suresh';")
edit = cur.fetchall()
# for row in rows:
#    # kk= row[0]+1
#    print ("NAME = ", row[1])
#    print ("EMPLOYEE = ", row[2])
#    print ("TEAM = ", row[3]), "\n"
# conn.commit()
data=list(edit)
for i in data:
   A=i[0]
   B=i[1]
   C=i[2]
   D=i[3]
   print(A,"\n",B,"\n",C,"\n",D)
         
conn.commit()
cur.close()
# print(kk)

