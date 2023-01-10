import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12451245',
    database='fantasy'
)
mycursor = db.cursor()
mycursor.execute("INSERT users (name, country, race) VALUES ('Dean', '1', '1');")
db.commit()