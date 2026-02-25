from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/me')
def me():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #проверка данных
        if username == "kid" and password == "12345lol":
            return redirect('/me')
        else:
            error = "неверный логин или пароль"
    return render_template('login.html', error=error)
if __name__ == '__main__':
    app.run(debug=True)