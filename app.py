from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
TASK_ID = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global TASK_ID
    data = request.get_json()
    new_task = Task(id=TASK_ID,title=data.get("title"), done=data.get("done") )
    TASK_ID+=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso.", "id": new_task.id})

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

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_update = None
    for t in tasks:
        if t.id == id:
            task_update = t
            break
    if task_update is None:
        return jsonify({"message": "Tarefa não encontrada"}, 404)
    data = request.get_json()
    task_update.title = data['title']
    task_update.done = data['done']
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

@app.route('/tasks/<int:id>' , methods=['DELETE'])
def detele_task(id):
    task_delete = None
    for t in tasks:
        if t.id == id:
            task_delete = t
            break
    if task_delete is None:
        return jsonify({"message": "Tarefa não encontrada"}, 404)
    if task_delete is not None:
        tasks.remove(task_delete)
        return jsonify({"message":"Tarefa deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
