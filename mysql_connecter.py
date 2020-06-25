import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sanjeevi",
  password="1234",
  database="testdb"
)
mycursor= mydb.cursor()
print(mydb)

#showing the databases
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#   print(db)

#creating a table
#mycursor.execute('CREATE TABLE students (name VARCHAR(255),age INT(10))')
#mycursor.execute('CREATE TABLE people (name VARCHAR(255),address VARCHAR(255))')

#showing the tables
#mycursor.execute("SHOW TABLES")
mycursor.execute("USE testdb")
#for tb in mycursor:
#  print(tb)

sqlformula ="INSERT INTO students (name,age) VALUES (%s, %s)"
students=[("sanjay",24),
          ("dheeju",20),
          ("nishanth",18),
          ("varsha",19),]

mycursor.executemany(sqlformula,students)

#commit database
mydb.commit()