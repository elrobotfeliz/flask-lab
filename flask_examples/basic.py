from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Root route</h1>'

@app.route('/info')
def info():
    return '<h1>Information.</h1>'

@app.route('/profile/<name>')
def profile(name):
    return 'User: {0}'.format(name[100])

if __name__ == '__main__':
    app.run(debug = True)   # DEBUG Should be disabled in production environments.