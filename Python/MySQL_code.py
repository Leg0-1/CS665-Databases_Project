import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="leg0",
  password="hackerman99",
  database = 'mydb'
)

cursor = mydb.cursor()


