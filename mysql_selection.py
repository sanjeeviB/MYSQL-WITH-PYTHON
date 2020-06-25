import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sanjeevi",
  password="1234",
  database="testdb"
)
mycursor= mydb.cursor()
#mycursor.execute("SELECT * FROM students")
mycursor.execute("SELECT age FROM students")
#myresult = mycursor.fetchall()
myresult = mycursor.fetchone()
print(myresult)
for row in myresult:
    print(row)