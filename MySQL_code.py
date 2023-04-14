import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="leg0",
  password="hackerman99"
)

print(mydb) 