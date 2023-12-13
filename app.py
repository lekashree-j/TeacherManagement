from flask import Flask, render_template,request, redirect,send_from_directory
from teachers import get_all, add_teacher,  delete_teachers

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show')
def show_all():
    teachers = get_all()
    return render_template('show.html', teachers=teachers)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        details = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'dob': request.form['dob'],
            'class': int(request.form['class'])
        }
        add_teacher(details)
    return render_template('add.html')

@app.route('/delete', methods=['GET','POST'])
def delete_teacher():
    if request.method == 'POST':
        name = request.form.get('deleteTeacher', '')
        delete_teachers(name)
    return render_template('delete.html')




@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

#if __name__ == '__main__':
    #app.run(debug=True)
