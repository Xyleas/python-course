import sqlite3

# open a database connection
connection = sqlite3.connect('chinook.db')

# cursors allow us to interact with the databse
cursor = connection.cursor()

result_set = cursor.execute('SELECT * FROM Track')
for row in result_set:
    # row = tuple object where each element is a value
    # print(row)
    pass

# this must be a tuple!
favorite_artist = ('Miles Davis')
result_set = cursor.execute('SELECT * FROM Track WHERE Composer=?', favorite_artist)
# DON'T USE PYTHON'S format FUNCTION or % BECAUSE OF SQL INJECTION ATTACKS!

# get one row at a time
print(result_set.fetchone())
print(result_set.fetchone())

# close the database connection
connection.close()

# close the cursor
cursor.close()