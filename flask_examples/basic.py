from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    di = { 'name': 'felipe', 'user_logged_in': True }
    return render_template('index.html', data = di)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/thank-you')
def thank_you():
    email = request.args.get('email')
    return render_template('thank-you.html', email = email)

@app.route('/profile/<name>')
def profile(name):
    return 'User: {0}'.format(name)

@app.errorhandler(404)
def fourofour(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)   # DEBUG Should be disabled in production environments.