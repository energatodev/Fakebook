from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('home.html')
    if request.method == 'POST':
        email = request.form.get['user-email']
        passwd = request.form.get['user-passwd']
        print(f"Email: {email}, Senha: {passwd}")    

if __name__ == '__main__':
    app.run(debug=true)
