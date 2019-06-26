from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return '<html><body style="background: yellow;" > Hello World from Python Flask! </body></html>'

app.run(host='0.0.0.0', port= 80)