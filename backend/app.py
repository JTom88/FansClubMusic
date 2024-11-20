from flask import Flask, jsonify, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token

from models import Usuario, Sorteo, Evento, Entrevista

# Creamos la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creamos instancia de SQLAlchemy
db = SQLAlchemy(app)

migrate = Migrate(app, db)

 
## -------------------->>> USUARIOS, LOGIN Y CREACIÓN TOKEN <<<----------------------- ##

 ## Creación de un nuevo usuario
@app.route('/registro', methods=['POST'])
def crear_usuario():
    data = request.json
    if 'usUsername' not in data or 'usEmail' not in data or 'usPassword' not in data:
        return jsonify ({"error": "falta alguno de los datos"}), 400
    
    if Usuario.query.filter_by(usEmail=data['usEmail']).first():
        return jsonify ({"error": "el correo electrónico ya existe"}), 400
    
    codificar_password = generate_password_hash(data['usPassword'])

    nuevo_usuario = Usuario(
        usUsername = data['usUsername'],
        usEmail = data['usEmail'],
        usPassword = codificar_password
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    access_token = create_access_token(identity=nuevo_usuario.usId)

    return jsonify({
        "mensaje": "nuevo usuario creado correctamente",
        "access_token": access_token,
        **nuevo_usuario.serialize()
    }), 201


#Obtener todos los usuarios
@app.route('/todoslosusuarios', methods=['GET'])
def obtener_todoslosusuarios():
    todosLosUsuarios = Usuario.query.all()
    return jsonify([usuarios.serialize() for usuarios in todosLosUsuarios])



#Obtener un usuario a través de su id
@app.route('/todoslosusuarios/<int:usId>', methods = ['GET'])
def obtener_usuarioPorId(usId):
    usuario = Usuario.query.get(usId)
    if usuario is None:
        return jsonify ({"error": "no se ha encontrado al usuario"}), 404
    
    return jsonify(usuario.serialize())


#Editar datos del usuario desde su perfil
@app.route('/todoslosusuarios/editar/<int:usId>', methods=['PUT'])
def editar_usuario(usId):
    usuario = Usuario.query.get(usId)
    if usuario is None:
        return jsonify({"error": "no se ha encontrado al usuario"}), 404
    
    data = request.json
    if not data:
        return jsonify({"error": "no hay data"}), 400
    
    try:
        if 'usNombre' in data:
            usuario.usNombre = data['usNombre']
        if 'token' in data:
            usuario.token = data['token']
        if 'usEmail' in data:
            usuario.usEmail = data['usEmail']
        if 'usId' in data:
            usuario.usId = data['usId']
        if 'usApellidos' in data:
            usuario.usApellidos = data['usApellidos']
        if 'usTelefono' in data:
            usuario.usTelefono = data['usTelefono']
        if 'usPueblo' in data:
            usuario.usPueblo = data['usPueblo']
        if 'usProvincia' in data:
            usuario.usProvincia = data['usProvincia']
        if 'usDireccion' in data:
            usuario.usDireccion = data['usDireccion']
        
        db.session.commit()
        return jsonify(data), 200

    except Exception as error:
        db.session.rollback()
        return jsonify({"error", str(error)})
    

#Verificar si la contraseña actual es la correcta
@app.route('/verificarPassword', methods=['POST'])
def verificarPassword():
    data = request.json

    usId = data.get('usId')
    password_actual = data.get('usPassword')

    if not usId or not password_actual:
        return jsonify ({"error": "falta algún dato en la solicitud"}), 400
    
    usuario = Usuario.query.get(usId)
    if not usuario:
        return jsonify ({"Error": "usuario no encontrado"}), 400
    
    if check_password_hash(usuario.usPassword, password_actual):
        return jsonify({'correcto': True}), 200
    else:
        return jsonify({'correcto': False}), 200


#Cambio de contraseña desde el perfil del usuario
@app.route('/usuarios/cambiopassword/<int:usId>', methods=['PUT'])
def cambioPassword(usId):
    usuario = Usuario.query.get(usId)
    if usuario is None:
        return jsonify({"error": "usuario no encontrado"}), 404
    
    data = request.json

    codificar_password = generate_password_hash(data['usPassword'])

    usuario.usPassword = codificar_password
    db.session.commit()
    return jsonify ({"mensaje": "contraseña cambiada ok"}), 200


#Login a la página y creación del token
@app.route('/login', methods = ['POST'])
def login():
    usEmail = request.json.get('usEmail', None)
    usPassword = request.json.get('usPassword', None)

    usuario = Usuario.query.filter_by(usEmail = usEmail).first()

    if usuario is None:
        return jsonify({"Error": "no se ha encontrado el correo o la contrasela"}), 404
    
    if not check_password_hash(usuario.usPassword, usPassword):
        return jsonify({"Error": "contraseña incorrecta"})
    
    #Creación del nuevo token de entrada del usuario a la página
    access_token = create_access_token(identity=usuario.usId)

    return jsonify({"id": usuario.usId, "Token": access_token, "email": usuario.usEmail, "userName": usuario.usUsername, "rol": usuario.usRol})




























if __name__ == '__main__':
    app.run(debug=True)