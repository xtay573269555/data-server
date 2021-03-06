# _*_ coding:utf-8 _*_
#!/usr/bin/env python

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command("runserver", 
        Server(host="0.0.0.0", port=21050, use_debugger=True))

if __name__ == '__main__':
    manager.run()
