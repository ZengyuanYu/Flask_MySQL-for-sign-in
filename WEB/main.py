#enconding： utf-8

from flask import Flask
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
