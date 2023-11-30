import sqlite3

# Establish a connection to the SQLite database file
CONN = sqlite3.connect('user_base.db')
# Create a cursor object to interact with the database
CURSOR = CONN.cursor()
