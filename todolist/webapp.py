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

