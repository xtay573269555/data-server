# _*_ coding:utf-8 _*_
#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)
#app.config.from_object("config.product")



#put to the last
from app import views,models

