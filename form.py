from flask import Flask, url_for
from flask import request
from flask import json


app = Flask(__name__)


@app.route('/messages', methods = ['POST'])
def api_message():
    return "hi"

if __name__ == '__main__':
    app.run()

# downloaded flask http://flask.pocoo.org/, used curl to test it out on my CLI, set it up on a digital ocean droplet 
