'''
Created on Dec 4, 2020

@author: opc
'''
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request




        
@app.route('/add', methods=['POST'])
def add_emp():
    try:
        _json =  request.json
        _name = _json['name']
        _cpf = _json['cpf']
        _address = _json['address']        
        if _name and _cpf and _address and request.method == 'POST':            
            sqlQuery = '''INSERT INTO employees(Name, cpf, address) VALUES(%s, %s, %s)'''
            bindData = (_name, _cpf, _address)
            db = pymysql.connect("172.18.0.1","app","app","clients",3306)
            cur = db.cursor()
            cur.execute(sqlQuery, bindData)
            db.commit() 
            db.close()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except (pymysql.DatabaseError,pymysql.MySQLError) as e:
        return str(e)
   
        
@app.route('/emp')
def emp():
    try:
        db = pymysql.connect("172.18.0.1","app","app","clients",3306)
        cur = db.cursor()
        cur.execute('''SELECT Name, cpf, address FROM employees''')
        empRows = cur.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        return str(e)
   
       
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
