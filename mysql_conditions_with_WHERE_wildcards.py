import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sanjeevi",
  password="1234",
  database="testdb"
)
mycursor= mydb.cursor()
#sql = "SELECT * FROM students WHERE age < 24"
#sql = "SELECT * FROM students WHERE name  = ('nishanth')"
#sql = "SELECT * FROM students WHERE name LIKE '%a%'"
# mycursor.execute(sql)
sql = "SELECT * FROM students WHERE name = %s"
mycursor.execute(sql,('sanjay',))
myresult = mycursor.fetchall()

for result in myresult:
    print(result)