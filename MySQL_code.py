import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="leg0",
  password="hackerman99",
  database = 'mydb'
)

cursor = mydb.cursor()

# cursor.execute("DROP TABLE lawyers")
# exit()


sql = """
CREATE TABLE Lawyers(
    LawyerID int AUTO_INCREMENT,
    LastName varchar(255),
    FirstName varchar(255),
    PRIMARY KEY (LawyerID));
"""

cursor.execute(sql)

sql2 = """
INSERT INTO Lawyers(LastName, FirstName)
VALUES ("Pearson", "Jessica")
"""

cursor.execute(sql2)
mydb.commit()


sql3 = """
    SELECT * FROM Lawyers;
"""
cursor.execute(sql3)
result = cursor.fetchall()

for x in result:
    print(x)
