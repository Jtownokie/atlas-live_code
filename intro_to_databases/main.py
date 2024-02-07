import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="1234", db="livecode")
cur = conn.cursor()

# Select All Artists, Order by ID Ascending
cur.execute("SELECT * FROM artists ORDER BY ArtistID ASC")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

# Select All Songs, Order by Title Descending
cur.execute("SELECT * FROM songs ORDER BY Title DESC")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

# Select All Artists, With an Age of Less Than 30
cur.execute("SELECT * FROM artists WHERE Age < 30")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

# Select All Songs, of a Specific Artist
cur.execute("SELECT * FROM songs WHERE ArtistID = 1")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()
conn.close()
