from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from os import sys, path
sys.path.append(path.split(path.dirname(path.dirname(path.abspath(__file__))))[0])

from flask_api import app,db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()