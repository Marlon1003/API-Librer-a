from flask import Flask, jsonify

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

@app.route('/informacion_libros', methods=['GET'])
def obtener_informacion_libros():
    try:
        cursor = mysql.connection.cursor()

        query = """
            SELECT 
                libros.id AS id_libro,
                libros.titulo AS titulo_libro,
                autores.nombre AS nombre_autor,
                generos.nombre AS nombre_genero,
                reseñas.contenido AS texto_reseña,
                usuarios.nombre AS nombre_usuario_reseña
            FROM 
                libros
                JOIN autores ON libros.autor_id = autores.id
                JOIN generos ON libros.genero_id = generos.id
                JOIN reseñas ON libros.id = reseñas.libro_id
                JOIN usuarios ON reseñas.usuario_id = usuarios.id
        """

        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]

        cursor.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
