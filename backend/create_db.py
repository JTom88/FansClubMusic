from app import app, db

# Asegúrate de que estamos dentro del contexto de la aplicación
with app.app_context():
    # Crear las tablas en la base de datos
    db.create_all()

print("Tablas creadas correctamente")
