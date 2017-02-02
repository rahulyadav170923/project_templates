from flask_restful import Resource, reqparse


class TodoList(Resource):
    def get(self):
        tasks = Task.query.all()
        data = []
        for i in tasks:
            data.append(taskschema.dump(i).data)
        return data

    def post(self):
        args = parser.parse_args()
        task = Task(args['task'])
        db.session.add(task)
        db.session.commit()
        return taskschema.jsonify(task), 201

from flask_api.app import db, ma
from flask_api.common.models import Task, TaskSchema

parser = reqparse.RequestParser()
parser.add_argument('task')
taskschema = TaskSchema()
