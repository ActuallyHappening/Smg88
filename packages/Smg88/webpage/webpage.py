"""Test Doc for webpage.py
"""

from datetime import datetime
import flask
from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self) -> str:
    return f"<Task {self.id}>"


@app.route("/", methods=["POST", "GET"])
def index():
  if flask.request.method == "POST":
    taskContent = flask.request.form["content"]
    newTask = Todo(content=taskContent)

    try:
      db.session.add(newTask)
      db.session.commit()
      return redirect("/")
    except Exception as err:
      print(f"Cool error caught! {err}")
      raise err
      return render_template("error.html")
  else:
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
  taskToDelete = Todo.query.get_or_404(id)

  try:
    db.session.delete(taskToDelete)
    db.session.commit()
    return redirect("/")
  except Exception as err:
    print(f"AWESOME ERROR caught!! {err}")
    raise err
    return render_template("error.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
  task = Todo.query.get_or_404(id)
  if flask.request.method == "POST":
    task.content = flask.request.form["content"]
    try:
      db.session.commit()
      return redirect("/")
    except Exception as err:
      print("Boring update error caught :( {err}")
      raise err
      return render_template("error.html")
  else:
    return render_template("update.html", task=task)


if __name__ == "__main__":
  #db.create_all()
  app.run(debug=True)
