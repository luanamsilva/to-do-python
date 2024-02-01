from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id
  data = request.get_json()
  newTask = Task(id=task_id,title=data.get("title") )
  task_id+=1
  tasks.append(newTask)
  print(tasks)
  return jsonify({"message": "Nova tarefa criada com sucesso."})


if __name__ == "__main__":
  app.run(debug=True)