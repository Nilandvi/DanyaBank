import sqlite3
file = open("files\\user.txt", "r").read()
sqlite_connection1 = sqlite3.connect('bases\\users_info.db')
cursor1 = sqlite_connection1.cursor()

debet = cursor1.execute(f"SELECT balance FROM Info WHERE username = '{file}'").fetchall()
us = cursor1.execute(f"SELECT username FROM Info").fetchall()
print(len(us))