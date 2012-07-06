from flask import redirect, url_for, render_template, request
from model import app, Task
import model

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)


@app.route("/add", methods=["GET"])
def make_task():
    return render_template("add_task.html")

@app.route("/add", methods=["POST"])
def save_task():
    t = Task(request.form['title'],
            request.form['notes'])
    model.add(t)
    model.save_all()
    print request.form 
    return "Save a task"


@app.route("/task/<task_id>", methods=["GET"])
def edit_task(task_id):
    task = Task.query.get(task_id)
    return render_template("task.html", task=task)

@app.route("/task/<task_id>", methods=["POST"])
def update_task(task_id):
    task = Task.query.get(task_id)

@app.route('/', methods=["POST"])
def mark_completed():
    tasks_completed_ids = request.form.getlist('completed')
    for id_num in tasks_completed_ids:
        task = Task.query.get(id_num)
        task.complete()
    model.save_all()
    return redirect(url_for("home"))

