from flask import Flask, request
from config import *
import os

app = Flask(__name__)


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
            os.system('{}/scripts/{}'.format(PATH, SCRIPTS[repository]))
    except Exception as e:
       print(e)

    return "OK"

app.run(host=HOST, port=PORT)