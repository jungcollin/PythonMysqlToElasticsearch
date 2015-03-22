import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="password", # your password
                     db="shrimp", # name of the data base
                     cursorclass = MySQLdb.cursors.SSCursor)

cur = db.cursor() 
cur.execute("select * from PERIODS where a > 0.179 and a < 0.18 \
             and b = 0.2 and period = 2 and c > 8 and c < 12;")
row = cur.fetchone()
while row is not None:
    print row
    row = cur.fetchone()
