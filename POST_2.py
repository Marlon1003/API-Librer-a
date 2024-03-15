from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/generos', methods=['POST'])
def agregar_genero():
    try:
        datos = request.get_json()
        nombre = datos['nombre']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO generos (nombre) VALUES (%s)', (nombre,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'mensaje': 'Género agregado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=7500)
