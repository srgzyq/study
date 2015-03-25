import mysql.connector
config={'host':'127.0.0.1',
        'user':'root',
        'password':'870830',
        'port':3306 ,
        'db':'test',
        'charset':'utf8'
        }
try:
  cnn=mysql.connector.connect(**config)
except mysql.connector.Error as e:
  print('connect fails!{}'.format(e))
