from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from models import Usuario, Sorteo, Evento, Entrevista

# Creamos la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creamos instancia de SQLAlchemy
db = SQLAlchemy(app)

# @app.before_first_request
# def crear_tablas():
#     db.create_all()

@app.route('/api/hello', methods=['GET'])
def hello():
    message = {'message': '¡Hola desde Flask y tu backend!'}
    return Response(response=jsonify(message).data, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True)
