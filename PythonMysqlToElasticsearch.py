import MySQLdb
import MySQLdb.cursors
from pyes import ES
import random
import string
import json
import collections

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


conn = ES('localhost:9200')
type_name = 'shrimp'
es_index = 'shrimp'

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="password", # your password
                     db="shrimp", # name of the data base
                     cursorclass = MySQLdb.cursors.SSCursor)

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("select * from PERIODS;")
row = cur.fetchone()
while row is not None:
    MysqlToES = collections.OrderedDict()
    MysqlToES['period'] = row[4]
    MysqlToES['a'] = row[1]
    MysqlToES['b'] = row[2]
    MysqlToES['c'] = row[3]
    MyESJson = json.dumps(MysqlToES)
    thisid = id_generator()
    conn.index(MyESJson, es_index, type_name, id=thisid)
    row = cur.fetchone()


