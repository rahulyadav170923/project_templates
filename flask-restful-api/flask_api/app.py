import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from resources.Todo import Todo
from resources.TodoList import TodoList

app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

