from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

my_secret_key = os.environ['SECRET_KEY']

app = Flask(__name__)
Bootstrap(app)
app.secret_key = my_secret_key

class LoginForm(FlaskForm):
    # CREATE FLASK-FORM TEMPLATES FOR EMAIL AND SUBMISSION
    # USING FLASK_WTF
    email = StringField(label='Email', validators=[Email(), Length(min=8)])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log in')

@app.route("/", methods=['GET', 'POST'])
def login():
    # test to get login working by returning success/denied if correct abc@gmail.com
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'abc@gmail.com':
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)