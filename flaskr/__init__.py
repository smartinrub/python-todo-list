from flask import Flask, jsonify, request


class Task:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}


task_id = 1
tasks = []


def create_app():
    app = Flask(__name__)

    @app.route("/tasks")
    def get_tasks():
        return list(map(Task.to_dict, tasks))

    @app.route("/tasks", methods=["POST"])
    def add_task():
        global task_id

        name = request.json["name"]
        new_task = Task(task_id, name)
        tasks.append(new_task)

        task_id += 1

        return jsonify(new_task.to_dict()), 201

    @app.route("/tasks/<int:id>", methods=["PUT"])
    def updateTask(id):
        task = next((task for task in tasks if task.id == id), None)

        if task is None:
            return jsonify({"error": "Task not found"}), 404

        task.name = request.json["name"]

        return jsonify(task.to_dict())

    @app.route("/tasks/<int:id>", methods=["DELETE"])
    def deleteTask(id):
        global tasks

        tasks = [task for task in tasks if task.id != id]

        return jsonify({"result": "Task deleted"})

    return app
