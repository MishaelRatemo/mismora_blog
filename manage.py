from app import  create_app
from flask_script import Manager, Server
# app instances
app = create_app('development_mode')
# app = create_app('development_mode')

manager = Manager()
manager.add_command('server', Server)


if __name__ == '__main__':
    manager.run()