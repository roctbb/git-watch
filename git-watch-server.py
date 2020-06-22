from flask import Flask, request
from config import *
import os
import threading

app = Flask(__name__)

def delayed(delay, f, args):
    timer = threading.Timer(delay, f, args=args)
    timer.start()

def update(repository):
    try:
        os.system('sh {}/scripts/{}'.format(PATH, SCRIPTS[repository]))
    except Exception as e:
        print(e)

@app.route('/', methods=['POST'])
def process():
    event = request.json
    token = request.headers.get('X-Gitlab-Token')

    if token != TOKEN:
        print("wrong token", request.headers)
        return "TOKEN"
    try:
        if event['object_kind'] == 'push':
            repository = event['repository']['name']
            delayed(5, update, [repository])
    except Exception as e:
       print(e)

    return "OK"

app.run(host=HOST, port=PORT)