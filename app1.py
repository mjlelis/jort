from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>---Olha só que coisa mais linda!--</h1> <p> <a href="/browsver"/>Veja isso!</a></p>'


@app.route('/user/<name>')
def user(name):
    return '<h1> Meu nome é %s!!</h1>' % name


@app.route('/browsver/')
def page():
    user_agent = request.headers.get('User-Agent')
    return '<p>Seu navegador é %s</p>' % user_agent


if __name__ == '__main__':
    app.run(debug=True)
