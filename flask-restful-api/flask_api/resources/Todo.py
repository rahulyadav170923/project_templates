from flask_restful import Resource,reqparse
from flask.common.models import Task,TaskSchema
from os import sys, path
sys.path.append(path.split(path.dirname(path.dirname(path.abspath(__file__))))[0])

from flask_api import db


parser = reqparse.RequestParser()
parser.add_argument('task')
taskschema = TaskSchema()


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



