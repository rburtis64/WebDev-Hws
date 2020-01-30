from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

def validate_password(form, field):
    if not any(char.isupper() for char in field.data):
        raise ValidationError('Password must contain a uppercase letter')
    if not any(char.islower() for char in field.data):
        raise ValidationError('Password must contain a lowercase letter')
    if not any(char.isInteger() for char in field.data):
        raise ValidationError('Password must contain number')


class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), validate_password])
    submit = SubmitField('Sign In')

@app.route ('/', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('base.html')

@app.route ('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run()
