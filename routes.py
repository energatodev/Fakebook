from flask import render_template, request, redirect, url_for
from app import app
#Rotas
@app.route('/')
def home():
    print("Site Acessado", flush=True)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('user-email')
        passwd = request.form.get('user-passwd')

        print(f"Email: {email} \nSenha: {passwd}", flush=True)


    return render_template('home.html')

