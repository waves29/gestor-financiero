from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# En memoria para simplificar, en una aplicación real usarías una base de datos
entries_basic = []
entries_plus = []
entries_premium = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plus')
def plus():
    total_ingresos = sum(entry['amount'] for entry in entries_plus if entry['type'] == 'ingreso')
    total_gastos = sum(entry['amount'] for entry in entries_plus if entry['type'] == 'gasto')
    balance = total_ingresos - total_gastos
    return render_template('plus.html', entries=entries_plus, total_ingresos=total_ingresos, total_gastos=total_gastos, balance=balance)

@app.route('/premium')
def premium():
    total_ingresos = sum(entry['amount'] for entry in entries_premium if entry['type'] == 'ingreso')
    total_gastos = sum(entry['amount'] for entry in entries_premium if entry['type'] == 'gasto')
    balance = total_ingresos - total_gastos
    # Implementar lógica adicional para proyecciones y reportes aquí
    return render_template('premium.html', entries=entries_premium, total_ingresos=total_ingresos, total_gastos=total_gastos, balance=balance)

@app.route('/add_plus', methods=['POST'])
def add_plus_entry():
    type_ = request.form['type']
    amount = float(request.form['amount'])
    description = request.form['description']
    
    # Agregar la nueva entrada a la lista del plan Plus
    entries_plus.append({
        'type': type_,
        'amount': amount,
        'description': description
    })
    
    return redirect(url_for('plus'))

@app.route('/add_premium', methods=['POST'])
def add_premium_entry():
    type_ = request.form['type']
    amount = float(request.form['amount'])
    description = request.form['description']
    
    # Agregar la nueva entrada a la lista del plan Premium
    entries_premium.append({
        'type': type_,
        'amount': amount,
        'description': description
    })
    
    return redirect(url_for('premium'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar sesiones y mensajes flash

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/basico')
def basico():
    return render_template('basico.html')

@app.route('/ayuda', methods=['GET', 'POST'])
def ayuda():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Configura el mensaje
        msg = Message('Nuevo mensaje de contacto', sender=email, recipients=['your_email@gmail.com'])
        msg.body = f'Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nMensaje:\n{mensaje}'

        try:
            mail.send(msg)
            flash('Mensaje enviado exitosamente!', 'success')
            return redirect(url_for('ayuda'))
        except:
            flash('Hubo un error al enviar el mensaje. Inténtalo de nuevo.', 'error')

    return render_template('ayuda.html')

if __name__ == '__main__':
    app.run(debug=True)

