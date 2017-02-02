from flask_api.app import db, ma


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    done = db.Column(db.Boolean, default=False)

    def __init__(self, task):
        self.task = task
        self.done = False

    def __repr__(self):
        return '<task : %s>' % self.task


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
