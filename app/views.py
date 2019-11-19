from datetime import datetime
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
from app import app, db, admin
from .models import task
from .forms import taskForm, searchForm
admin.add_view(ModelView(task, db.session))


@app.route("/")
def homepage():
    Tasks = task.query.filter_by(date=datetime.now().strftime('%Y-%m-%d')).all()
    return render_template('index.html',
                           title='homepage',
                           Tasks=Tasks)


@app.route('/create_task', methods=['GET', 'POST'])
def create_student():
    form = taskForm()
    if form.validate_on_submit():
        Tasks = task(title=form.title.data, description=form.description.data, date=form.date.data)
        db.session.add(Tasks)
        db.session.commit()
        return redirect('/')

    return render_template('create_task.html',
                           title='Create Task',
                           form=form)


@app.route('/tasks', methods=['GET'])
def tasks():
    Tasks = task.query.all()
    return render_template('tasks.html',
                           title='All Tasks',
                           Tasks=Tasks)


@app.route('/delete_task1/<id>', methods=['GET'])
def delete_task1(id):
    Task = task.query.get(id)
    db.session.delete(Task)
    db.session.commit()
    return redirect('/tasks')


@app.route('/delete_task2/<id>', methods=['GET'])
def delete_task2(id):
    Task = task.query.get(id)
    db.session.delete(Task)
    db.session.commit()
    return redirect('/finished_tasks')


@app.route('/delete_task3/<id>', methods=['GET'])
def delete_task3(id):
    Task = task.query.get(id)
    db.session.delete(Task)
    db.session.commit()
    return redirect('/unfinished_tasks')


@app.route('/delete_task4/<id>', methods=['GET'])
def delete_task4(id):
    Task = task.query.get(id)
    db.session.delete(Task)
    db.session.commit()
    return redirect('/')


@app.route('/delete_task5/<id>', methods=['GET'])
def delete_task5(id):
    Task = task.query.get(id)
    db.session.delete(Task)
    db.session.commit()
    return redirect('/search_task')


@app.route('/edit_task1/<id>', methods=['GET', 'POST'])
def edit_task1(id):
    Task = task.query.get(id)
    form = taskForm(obj=Task)
    if form.validate_on_submit():
        t = Task
        t.title = form.title.data
        t.description = form.description.data
        db.session.commit()
        return redirect('/tasks')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)


@app.route('/edit_task3/<id>', methods=['GET', 'POST'])
def edit_task3(id):
    Task = task.query.get(id)
    form = taskForm(obj=Task)
    if form.validate_on_submit():
        t = Task
        t.title = form.title.data
        t.description = form.description.data
        db.session.commit()
        return redirect('/unfinished_tasks')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)


@app.route('/edit_task4/<id>', methods=['GET', 'POST'])
def edit_task4(id):
    Task = task.query.get(id)
    form = taskForm(obj=Task)
    if form.validate_on_submit():
        t = Task
        t.title = form.title.data
        t.description = form.description.data
        db.session.commit()
        return redirect('/')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)


@app.route('/edit_task5/<id>', methods=['GET', 'POST'])
def edit_task5(id):
    Task = task.query.get(id)
    form = taskForm(obj=Task)
    if form.validate_on_submit():
        t = Task
        t.title = form.title.data
        t.description = form.description.data
        db.session.commit()
        return redirect('/search_task')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)


@app.route('/change_state_true1/<id>', methods=['GET'])
def change_state1(id):
    Task = task.query.get(id)
    Task.state = True
    db.session.add(Task)
    db.session.commit()
    return redirect('/tasks')


@app.route('/change_state_true3/<id>', methods=['GET'])
def change_state3(id):
    Task = task.query.get(id)
    Task.state = True
    db.session.add(Task)
    db.session.commit()
    return redirect('/unfinished_tasks')


@app.route('/change_state_true4/<id>', methods=['GET'])
def change_state4(id):
    Task = task.query.get(id)
    Task.state = True
    db.session.add(Task)
    db.session.commit()
    return redirect('/')


@app.route('/change_state_true5/<id>', methods=['GET'])
def change_state5(id):
    Task = task.query.get(id)
    Task.state = True
    db.session.add(Task)
    db.session.commit()
    return redirect('/search_task')


@app.route('/unfinished_tasks', methods=['GET'])
def unfinished_tasks():
    Tasks = task.query.filter_by(state=False).all()
    return render_template('unfinished_task.html',
                           title='Unfinished Tasks',
                           Tasks=Tasks)


@app.route('/finished_tasks', methods=['GET'])
def finished_tasks():
    Tasks = task.query.filter_by(state=True).all()
    return render_template('finished_task.html',
                           title='Finished Tasks',
                           Tasks=Tasks)


@app.route('/search_task', methods=['GET', 'POST'])
def search_task():
    form = searchForm()
    if form.validate_on_submit():
        Tasks = task.query.filter_by(date=form.searchdate.data).all()
        return redirect('/search_task')

    return render_template('search_task.html',
                           title='Search task',
                           form=form)
