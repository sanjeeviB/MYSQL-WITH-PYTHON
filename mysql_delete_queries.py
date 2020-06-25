import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sanjeevi",
  password="1234",
  database="testdb"
)
mycursor= mydb.cursor()
# sql = "DELETE   FROM students WHERE name='sanjay'"
# sql = "DELETE   FROM students WHERE age='12'"
# sql = "DROP TABLE IF EXISTS students "
mycursor.execute(sql)
mydb.commit()