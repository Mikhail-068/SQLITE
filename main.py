import sqlite3
from config import *

connection = sqlite3.connect('Diesel.db')
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER AUTO_INCREMENT,"
            "surname TEXT,"
            "money INTEGER DEFAULT 0,"
            "PRIMARY KEY(id)"
            ")")
connection.commit()

cur.execute("CREATE TABLE IF NOT EXISTS garage ("
            "id INTEGER AUTO_INCREMENT,"
            "data_stopped DATE,"
            "liters INTEGER DEFAULT 0,"
            "id_driver INTEGER,"
            "PRIMARY KEY(id)"
            ")")
connection.commit()

cur.executemany("INSERT INTO `garage` (data_stopped, liters, id_driver) VALUES" \
            "(?, ?, ?)", (list_garage))
connection.commit()
connection.close()