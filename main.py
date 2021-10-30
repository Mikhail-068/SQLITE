import sqlite3
from config import *

def del_(x):
    cur.execute(f"DROP TABLE IF EXISTS {x}")
def add_(x):
    cur.execute("INSERT INTO users (surname) VALUES (?)", (x,))

connection = sqlite3.connect('Diesel.db')
cur = connection.cursor()

# del_('users')
cur.execute("CREATE TABLE IF NOT EXISTS users ("
            "id INT AUTO_INCREMENT,"
            "surname VARCHAR(15),"
            "money INT DEFAULT 0,"
            "PRIMARY KEY(id)"
            ")")
cur.execute("CREATE TABLE IF NOT EXISTS `garage` ("
            "`id` INT AUTO_INCREMENT,"
            "`data_stopped` DATE,"
            "`liters` INT DEFAULT 0,"
            "`id_driver` INT,"
            "PRIMARY KEY(id)"
            ")"
            )

for i in range(len(list_users)):
    add_(users[i])
    connection.commit()

connection.close()
