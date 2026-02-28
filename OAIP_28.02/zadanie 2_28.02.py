from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return 'напишите необходимые числа и операцию в поисковую строчку браузера числа через /'
@app.route('/<float:n1>/<string:op>/<float:n2>')
def cal(n1, op, n2):
    return render_template('index2.html', n1=n1, op=op, n2=n2)
if __name__ == '__main__':
    app.run(debug=True)