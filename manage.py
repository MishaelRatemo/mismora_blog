from app import  create_app
from flask_script import Manager, Server
from app import db
from app.models import Users,Posts,Comments, Likes,Unlikes
from flask_migrate import Migrate,MigrateCommand
# app instances
app = create_app('development_mode')
# app = create_app('development_mode')

manager = Manager()
manager.add_command('server', Server)

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
    manager.run()