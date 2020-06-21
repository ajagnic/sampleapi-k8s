import sys
import json
from time import time

from flask import Flask, request

from storage.mongo import MongoDB
from storage.dummy_data import insert_dummy_data

app = Flask(__name__)
client = MongoDB()


@app.route('/api/read/<table>', methods=['GET'])
def get(table):
    query = dict(request.args)
    records = client.get(table, query)
    return json.dumps(records)

@app.route('/api/create/<table>', methods=['POST'])
def insert(table):
    new_record = dict(request.form)
    new_record['_id'] = str(time())
    success = client.insert(table, [new_record])
    return json.dumps(success)

@app.route('/api/update/<table>', methods=['PUT', 'POST'])
def update(table):
    query = dict(request.args)
    new_record = dict(request.form)
    result = client.update(table, query, new_record)
    return result

@app.route('/api/delete/<table>', methods=['DELETE', 'GET'])
def delete(table):
    query = dict(request.args)
    result = client.delete(table, query)
    return result


if __name__ == '__main__':
    conn_str = sys.argv[1]
    insert_dummy_data(conn_str)

    client.try_connect(conn_str)

    app.run(debug=True, host='0.0.0.0', port='5001')
    client.close()
