import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sanjeevi",
  password="1234",
  database="testdb"
)
mycursor= mydb.cursor()
# sql = "UPDATE students SET age = 18 where name = 'nishanth'"
# mycursor.execute(sql)

mycursor.execute("SELECT * FROM students LIMIT 2 OFFSET 2")
myresult= mycursor.fetchall()
for result in myresult:
    print(result)
mydb.commit()