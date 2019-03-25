from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SignupForm(FlaskForm):
    username = StringField("Username:")
    password = PasswordField("Password:")
    submit = SubmitField("Sign up!")


@app.route('/')
def index():
    di = { 'name': 'felipe', 'user_logged_in': True }
    return render_template('index.html', data = di)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    username = None
    password = None
    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        form.username.data = ''
        form.password.data = ''

    return render_template('signup.html', form=form, username=username, password=password)

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