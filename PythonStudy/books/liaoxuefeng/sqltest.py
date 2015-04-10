import mysql.connector
from mysql.connector import errorcode

config={
        'user':'root',
        'password':'870830',
        'db':'test',
        'charset':'utf8'
        }

try:
  cnn=mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print('connect fails!{}'.format(err))

'''
import MySQLdb
conn = MySQLdb.connect(user="root",passwd="870830",db="performance_schema",charset="utf8")
print conn.cursor().execute('show tables;')
'''
