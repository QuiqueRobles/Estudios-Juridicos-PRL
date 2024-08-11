from flask import render_template, request, flash, redirect, url_for
from app import app
from app.forms import ConsultaForm, ContactForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    form = ConsultaForm()
    if form.validate_on_submit():
        # Lógica para manejar la consulta
        flash('Consulta enviada con éxito.', 'success')
        return redirect(url_for('index'))
    return render_template('consulta.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Lógica para manejar el contacto
        flash('Mensaje enviado con éxito.', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

@app.route('/herencias_form')
def herencias_form():
    return render_template('herencias_form.html')

@app.route('/particiones_form')
def particiones_form():
    return render_template('particiones_form.html')