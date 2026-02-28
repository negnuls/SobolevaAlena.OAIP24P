from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/')
def index():
    return 'напишите в поисковую строчку браузера: /srednee/число/число/число'
@app.route('/srednee/<int:a>/<int:b>/<int:c>')
def med(a, b, c):
    return render_template('index1.html', a=a, b=b, c=c)
if __name__ == '__main__': 
    app.run(debug=True)