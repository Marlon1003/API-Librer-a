from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        data = request.json
        nombre = data.get('nombre')

        try:
            cursor.execute('INSERT INTO Usuarios (nombre) VALUES (%s)', (nombre,))
            mysql.connection.commit()
            cursor.close()
            return jsonify({'message': 'Usuario agregado exitosamente', 'nombre': nombre}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=7500)
