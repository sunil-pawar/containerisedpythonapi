'''
Created on Dec 4, 2020
creating config file for DB
@author: opc
'''
from app import app
#from  flask_mysql  import MySQL
#import mysql.connector
from flask_mysqldb import MySQL

mysql = MySQL()
app.config['MYSQL_USER'] = 'app'
app.config['MYSQL_PASSWORD'] = 'app'
app.config['MYSQL_DB'] = 'clients'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = '3306'
app.config['auth_plugin'] = 'mysql_native_password'
mysql.init_app(app)
