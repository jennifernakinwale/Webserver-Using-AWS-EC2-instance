import csv
import sqlite3

conn = sqlite3.connect('user.db')

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS user""")
cur.execute("""CREATE TABLE user
            (Firstname text, Lastname text, Email text, Username text, Password text)""")


conn.commit()
conn.close()
