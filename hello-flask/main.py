from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form["first_name"]
    template = jinja_env.get_template("hello_greeting.html")
    return  render_template(name=first_name) 

@app.route("/valid_time")
def valid_time():
    time = request.args.get("time")
    return "<h1> You submitted {0}. Thanks for submitting a valid time!</h1>".format(time)

tasks = []

@app.route("/todos", methods=["POST", "GET"])
def todos ():
    if request.methods == "POST":
        task = request.form["task"]
        task.append(task)

    templaste = jinja_env.get_template(*"todos.html")
    return template.render(tasks=tasks)    

app.run()