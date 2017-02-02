from flask_restful import Resource, reqparse

class Todo(Resource):
    def get(self, todo_id):
        task = Task.query.filter_by(id=todo_id).first()
        task = taskschema.jsonify(task)
        return task

    def delete(self, todo_id):
        Task.query.filter_by(id=todo_id).delete()
        db.session.commit()
        return 'deleted', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task_txt = args['task']
        task = Task.query.filter_by(id=todo_id).first()
        task.task = task_txt
        db.session.commit()
        task = taskschema.jsonify(task)
        return task, 201


from flask_api.app import db, ma
from flask_api.common.models import Task, TaskSchema

parser = reqparse.RequestParser()
parser.add_argument('task')
taskschema = TaskSchema()