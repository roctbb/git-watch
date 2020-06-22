from flask import Flask, request
from config import *
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process():
    event = request.json
    try:
        if event['object_kind'] == 'push':
            repository = event['repository']['name']
            os.system('./scripts/{}'.format(SCRIPTS[repository]))
    except Exception as e:
       print(e)

    return "OK"

app.run(host=HOST, port=PORT)