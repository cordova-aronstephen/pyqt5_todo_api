from flask import Blueprint, request, jsonify
from db import get_connection
from task_db import (
    get_all_tasks,
    get_task_id,
    insert_task,
    update_task_model,
    delete_task_model
)

todo_bp = Blueprint('todo', __name__)

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
TASK_TABLE = 'task'

@todo_bp.route('/tasks', methods=['GET'])
def get_tasks():
    task = get_all_tasks()
    return jsonify(task), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = get_task_id(id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND

    return jsonify(dict(task)), HTTP_OK

@todo_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    required_fields = ['title', 'status_id', 'tag_id']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), HTTP_BAD_REQUEST
    insert_task(data)
    return jsonify({'message': 'Task created successfully'}), HTTP_CREATED

@todo_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = get_task_id(id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND
    update_task_model(id, data)
    return jsonify({'message': 'Task updated successfully'}), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = get_task_id(id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND
    delete_task_model(id)
    return jsonify({'message': 'Task deleted successfully'}), HTTP_OK