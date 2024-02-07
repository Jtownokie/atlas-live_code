import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="1234", db="livecode")
cur = conn.cursor()

# Select All Artists, Order by ID Ascending


# Select All Songs, Order by Title Descending


# Select All Artists, With an Age of Less Than 30


# Select All Songs, of a Specific Artist


cur.close()
conn.close()
