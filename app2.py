from flask import request

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello' + request.arge ['name']
    else:
        return 'Hello John Doe'
