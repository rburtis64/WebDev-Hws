from main import db, Student, app
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app.config['SECRET_KEY'] = 'secretkey'

class MyForm(FlaskForm):
    name = StringField('Students name')
    grade = StringField('midterm grade')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name =False
    grade=False
    form = MyForm()

    if form.validate_on_submit():
        name = form.name.data
        grade = form.grade.data
        form.name.data = ''
        form.grade.data = ''

        new_student = Student (name, grade)
        db.session.add(new_student)
        db.session.commit()
    return render_template('home.html',form=form, name=form.name.data, grade=form.grade.data)


@app.route('/list')
def list():
    students = Student.query.all()
    check = False

    return render_template('list.html', students=students, check=check)

@app.route('/passing')
def passing():
    pStudents = Student.query.filter(Student.grade >= 85)
    check = True
    return render_template('passing.html', Students=Students, check=check)


db.create_all()

ryan = Student('Ryan', 100)
alan = Student('Alan', 105)

print(ryan.id)
print(alan.id)

db.session.add_all([ryan, alan])

db.session.commit()

print(ryan.id)
print(alan.id)

if __name__ == '__main__':
    app.run(debug=True)
