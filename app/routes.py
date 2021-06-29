from app import app
from app.controller import DosenController
from flask import request

@app.route('/')
def index():
    return "Hello world!"

@app.route('/dosen', methods=['GET', 'POST'])
def lectures():
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.save()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def lectureDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.update(id)
    elif request.method == 'DELETE':
        return DosenController.delete(id)