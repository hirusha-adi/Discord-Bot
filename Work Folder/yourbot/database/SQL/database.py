import sqlite3

conn = sqlite3.connect("YourBot.db")
cur = conn.cursor()
conn.close()
