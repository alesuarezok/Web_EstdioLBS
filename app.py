from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave segura

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Aquí puedes procesar el mensaje, por ejemplo, enviarlo por email
    # Por ahora, solo mostramos un mensaje de éxito
    flash(f'Gracias {name}, hemos recibido tu mensaje. Te contactaremos pronto.', 'success')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)