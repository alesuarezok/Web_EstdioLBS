from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Configuración de email (Outlook/Hotmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    try:
        # Email para ti (propietario del sitio)
        msg = Message(
            subject=f'Nuevo mensaje de contacto de {name}',
            recipients=[os.getenv('OWNER_EMAIL')],
            body=f'''
Nuevo mensaje de contacto:

Nombre: {name}
Email: {email}
Mensaje:
{message}
            '''
        )
        mail.send(msg)
        

        msg_confirm = Message(
            subject='Hemos recibido tu mensaje - LBC y Asociados',
            recipients=[email],
            body=f'''
Hola {name},

Gracias por contactarnos. Hemos recibido tu mensaje y nos pondremos en contacto en breve.

Tu mensaje:
{message}

Saludos,
LBC y Asociados
            '''
        )
        mail.send(msg_confirm)
        
        flash(f'Gracias {name}, hemos recibido tu mensaje. Te contactaremos pronto.', 'success')
    except Exception as e:
        flash(f'Error al enviar el mensaje: {str(e)}', 'error')
        print(f'Error: {str(e)}')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)