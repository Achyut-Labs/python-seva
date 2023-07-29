import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE DATABASE todo")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), task VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Python Homework")
mycursor.execute(sql, val)

mycursor.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)


mycursor.close()
