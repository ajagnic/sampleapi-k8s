import os
import sys
import json
from time import time

from flask import Flask, request

from storage.mongo import MongoDB

app = Flask(__name__)
client = MongoDB()


@app.route('/api/read/<table>', methods=['GET'])
def get(table):
    query = dict(request.args)
    records = client.get(table, query)
    return json.dumps(records, sort_keys=True)

@app.route('/api/create/<table>', methods=['POST'])
def insert(table):
    new_record = dict(request.form)
    new_record['_id'] = str(time())
    updated_ids = client.insert(table, [new_record])
    return json.dumps(updated_ids)

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
    conn_str = os.environ.get('MONGODB_URI')
    if conn_str is None:
        sys.exit('Cannot find MONGODB_URI env variable.')
    
    if client.try_connect(conn_str):
        app.run(debug=True, host='0.0.0.0', port='5001')
        client.close()
    else:
        print('Database connection failed.\n')
