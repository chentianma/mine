# -*- coding: utf8 -*-


from flask import Flask
from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand
from blog import create_app, db
from blog.models import User, Role, Article, Category


app = create_app()
manager = Manager(app)
migreate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role,
                Article=Article, Category=Category)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # manager.run()
