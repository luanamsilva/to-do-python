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

@app.route('/tasks', methods=['GET'])
def get_tasks():
 task_list = [task.informations() for task in tasks]
 tasks_output = {
   "tasks": task_list,
   "total_tasks": len(task_list)
 }
 return jsonify(tasks_output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.informations())
  return jsonify({'message':'Tarefa não encontrada'}, 404)

if __name__ == "__main__":
  app.run(debug=True)