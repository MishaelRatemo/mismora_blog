from app import  create_app
from flask_script import Manager, Server
from app import db
from app.models import Users,Posts,Comments, Likes,Unlikes
from flask_migrate import Migrate,MigrateCommand
# app instances
app = create_app('development_mode')
# app = create_app('development_mode')

manager = Manager(app)
manager.add_command('server', Server)

# initialize migrate class that has been imported
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
                    app =app,
                    db=db,
                    Users=Users,
                    Posts=Posts,
                    Comments =Comments,
                    Likes=Likes,
                    Unlikes = Unlikes        
                )

if __name__ == '__main__':
    # app.run()
    manager.run()