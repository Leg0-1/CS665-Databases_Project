import mysql.connector

LawyerDB = mysql.connector.connect(
  host="localhost",
  user="root",
  password="project.Password01", # Just bc it's a password I'll never use doesn't mean I shouldn't make it strong
  database = 'LawyerDB'
)

cursor = LawyerDB.cursor()


cursor.execute("SELECT * FROM Lawyers;")

result = cursor.fetchall()

for x in result:
    print(x)