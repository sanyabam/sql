import sqlite3

#with sqlite3.connect("game.db") as con:
#    cur = con.cursor()
#    cur.execute("""CREATE TABLE IF NOT EXISTS user2(
#    last_name TEXT,
#    password INTEGER
#    )
#    """)
#con.close()


#with sqlite3.connect("game.db") as con:
#    cur = con.cursor()
#    cur.execute("""DROP TABLE user2
#    """)
#
#con.close()


#with sqlite3.connect("game.db") as con:
#    cur = con.cursor()
#    cur.execute("""CREATE TABLE new_users(
#    user_id INTEGER PREMARY KEY,
#    name TEXT NOT MALL,
#    sex INTEGER DEFAULT 1,
#    score INTEGER
#    )
#    """)
#con.close()

with sqlite3.connect("game.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM users 
        """)
    result = cur.fetchone()
    print(result)
