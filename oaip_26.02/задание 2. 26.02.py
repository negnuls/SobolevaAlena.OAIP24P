from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return 'напишите число в поисковую строчку браузера'
@app.route('/<float:r>')
def circle_area(r):
    pi = 3.14
    return render_template('index2.html', r=r, pi=pi)
if __name__ == '__main__':
    app.run(debug=True)