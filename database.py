from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/libros', methods=['GET'])
def get_libros():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM libros')
    libros = cursor.fetchall()
    cursor.close()
    res = jsonify(libros)
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

if __name__ == '__main__':
    app.run(debug=True, port=7500)