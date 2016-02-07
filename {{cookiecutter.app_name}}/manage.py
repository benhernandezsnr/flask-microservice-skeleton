from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os
import app
from app.app_factory import AppFactory
from app.models import db

app = app.create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def runserver():
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

if __name__ == '__main__':
    manager.run()
