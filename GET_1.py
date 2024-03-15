from flask import Flask, jsonify

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/libros', methods=['GET'])
def get_libros():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM libros')
        libros = cursor.fetchall()
        cursor.close()
        return jsonify(libros)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=7500)
