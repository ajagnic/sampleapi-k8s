import os
import json
from time import time

from flask import Flask, request, jsonify

from storage.mongo import MongoDB

app = Flask(__name__)
client = MongoDB()


@app.route('/api', methods=['GET'])
def connect():
    connected = client.ok
    if not connected:
        connected = client.try_connect(os.environ.get('MONGODB_URI'))
    return jsonify(Connected=connected), 200

@app.route('/api/read/<table>', methods=['GET'])
def get(table):
    if client.ok:
        query = dict(request.args)
        records = client.get(table, query)
        return jsonify(records), 200
    return jsonify({'Server-Error': True}), 503

@app.route('/api/create/<table>', methods=['POST'])
def insert(table):
    if client.ok:
        new_record = dict(request.form)
        new_record['_id'] = str(time())
        updated_ids = client.insert(table, [new_record])
        return jsonify(updated_ids), 201
    return jsonify({'Server-Error': True}), 503

@app.route('/api/update/<table>', methods=['PUT', 'POST'])
def update(table):
    if client.ok:
        query = dict(request.args)
        new_record = dict(request.form)
        result = client.update(table, query, new_record)
        return jsonify(result), 200
    return jsonify({'Server-Error': True}), 503

@app.route('/api/delete/<table>', methods=['DELETE', 'GET'])
def delete(table):
    if client.ok:
        query = dict(request.args)
        result = client.delete(table, query)
        return jsonify(result), 200
    return jsonify({'Server-Error': True}), 503


if __name__ == '__main__':
    client.try_connect(os.environ.get('MONGODB_URI'))
    app.run(debug=True, host='0.0.0.0', port='5001')
    client.close()
