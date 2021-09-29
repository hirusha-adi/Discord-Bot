import sqlite3

database_name = "game.db"

def connect():
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, balance integer)")
    # id - integer - primary key
    # balance - integer
    conn.commit()
    conn.close()

def insert_first(id):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("INSERT INTO game VALUES (?,1) OR UPDATE game SET ", (id,))
    # cur.execute("INSERT OR REPLACE INTO game VALUES (?,1)", (id,))
    # cur.execute("INSERT INTO game VALUES (?,?)", (id, balance))
    conn.commit()
    conn.close()

def insert(id, balance):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO game VALUES (?,?)", (id, balance))
    # cur.execute("INSERT OR REPLACE INTO game VALUES (?,?)", (id, balance))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM game")
    rows = cur.fetchall()
    conn.close()
    return rows

def view(id):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE id=(?)", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("DELETE FROM game WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, newbalance):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute("UPDATE game SET balance=? WHERE id=?", (newbalance, id))
    conn.commit()
    conn.close()


connect()
insert_first(9955)
insert_first(5566)
print("\n", view_all())
update(9955, 2)
insert_first(9955)
print("\n", view_all())


