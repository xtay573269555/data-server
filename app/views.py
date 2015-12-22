# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app
from flask import render_template
from flask import request
from flask import json,jsonify
import time

@app.route('/')
def index():
    return "Hello World!"

@app.route('/device',methods=['POST'])
def device():
    print request.json
    bak = {
        'at':'14646464',
        'code':'200'
    }
    bak['at']=str(int(time.time()))
    return  jsonify(bak),200