from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    
    # Importar el diccionario de configuración dentro de la función
    from .config import config
    app.config.from_object(config[config_name])

    mail.init_app(app)

    # Importar rutas aquí
    with app.app_context():
        from . import routes

    return app
