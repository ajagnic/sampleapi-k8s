from flask import Flask

import storage.dummy_data
from storage.mongo import MongoDB

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world.'


if __name__ == '__main__':
    client = MongoDB()
    app.run(debug=True, host='0.0.0.0', port='5001')
