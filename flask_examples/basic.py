from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    di = { 'name': 'felipe', 'user_logged_in': True }
    return render_template('index.html', data = di)

@app.route('/info')
def info():
    return '<h1>Information.</h1>'

@app.route('/profile/<name>')
def profile(name):
    return 'User: {0}'.format(name)

if __name__ == '__main__':
    app.run(debug = True)   # DEBUG Should be disabled in production environments.