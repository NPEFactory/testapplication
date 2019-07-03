from flask import Flask

import os
import socket

app = Flask(__name__)

msg = """<html><body style='{}'>
Hello World from Python Flask!
Currently we are in '{}'
hostname is '{}'
</body></html>"""


@app.route('/hello')
def helloIndex():
    style = "background: " + str(os.environ.get('bgcolor'))
    namespace = str(os.environ.get('NAMESPACE'))
    return msg.format(style, namespace, socket.gethostname())

app.run(host='0.0.0.0', port=80)
