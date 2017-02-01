from flask_restful import Resource,reqparse
from flask.common.models import Task,TaskSchema
from os import sys, path
sys.path.append(path.split(path.dirname(path.dirname(path.abspath(__file__))))[0])


from flask_api import db

parser = reqparse.RequestParser()
parser.add_argument('task')
taskschema = TaskSchema()


class TodoList(Resource):
    def get(self):
        tasks = Task.query.all()
        data=[]
        for i in tasks:
            data.append(taskschema.dump(i).data)
        return data

    def post(self):
        args = parser.parse_args()
        task = Task(args['task'])
        db.session.add(task)
        db.session.commit()
        return taskschema.jsonify(task), 201

