from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/autores/<int:id>', methods=['DELETE'])
def eliminar_autor(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM autores WHERE id = %s', (id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'mensaje': 'Autor eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=7500)
