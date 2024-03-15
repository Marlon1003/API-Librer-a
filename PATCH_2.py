from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/reseñas/<int:id>', methods=['PATCH'])
def update_reseña(id):
    if request.method == 'PATCH':
        cursor = mysql.connection.cursor()
        data = request.json
        nuevo_contenido = data.get('contenido')

        try:
            cursor.execute('UPDATE Reseñas SET contenido = %s WHERE id = %s', (nuevo_contenido, id))
            mysql.connection.commit()
            cursor.close()
            return jsonify({'message': 'Reseña actualizada exitosamente', 'resena_id': id}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=7500)
