'''
Windows:
MySQL Installer
https://dev.mysql.com/downloads/mysql/

MySQL Client
https://dbeaver.io/download/
https://www.heidisql.com/download.php


Mac:
MySQL Installer
https://dev.mysql.com/downloads/mysql/

MySQL client
https://dbeaver.io/download/

activate virtual env before going further

pip install -r requirement.txt
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Userkrisha-24",
  database="todo"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)