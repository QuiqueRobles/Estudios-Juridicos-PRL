from app import app
from flask_mail import Mail

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.secureserver.net'  # SMTP de GoDaddy
app.config['MAIL_PORT'] = 465  # Puerto SMTP para SSL
app.config['MAIL_USE_SSL'] = True  # Habilitar SSL
app.config['MAIL_USE_TLS'] = False  # No habilitar TLS
app.config['MAIL_USERNAME'] = 'pedro.robles@estudiojuridicoprl.es'  # Tu dirección de correo de GoDaddy
app.config['MAIL_PASSWORD'] = 'tu_contraseña'  # La contraseña de tu correo
app.config['MAIL_DEFAULT_SENDER'] = ('Pedro Robles Latorre', 'pedro.robles@estudiojuridicoprl.es')

mail = Mail(app)

if __name__ == "__main__":

    app.run(debug=True)
