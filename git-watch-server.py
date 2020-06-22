from flask import Flask, request
from config import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process():
    print(request.headers)
    print(request.data)
    return 'Hello, World!'

app.run(host=HOST, port=PORT)