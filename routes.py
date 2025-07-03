from flask import Blueprint, request, jsonify
from task_db import (
    get_all_tasks,
    get_task_id,
    insert_task,
    update_task_model,
    delete_task_model,
    status_exists, 
    tag_exists, 
    user_exists
)

todo_bp = Blueprint('todo', __name__)

# HTTP status codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404

@todo_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """
    GET /tasks
    Returns a list of all tasks.
    """
    tasks = get_all_tasks()
    return jsonify(tasks), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    """
    GET /tasks/<id>
    Returns a specific task by ID.
    Returns 404 if not found.
    """
    task = get_task_id(id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND
    return jsonify(task), HTTP_OK

@todo_bp.route('/tasks', methods=['POST'])
def create_task():
    """
    POST /tasks
    Creates a new task. Requires:
    - title
    - status_id
    - tag_id
    - user_id

    Returns:
    - 201 on success
    - 400 if required field or FK is missing/invalid
    """
    data = request.get_json()
    required_fields = ['title', 'status_id', 'tag_id', 'user_id']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), HTTP_BAD_REQUEST

    if not status_exists(data['status_id']):
        return jsonify({'error': 'Invalid status_id'}), HTTP_BAD_REQUEST
    if not tag_exists(data['tag_id']):
        return jsonify({'error': 'Invalid tag_id'}), HTTP_BAD_REQUEST
    if not user_exists(data['user_id']):
        return jsonify({'error': 'Invalid user_id'}), HTTP_BAD_REQUEST

    insert_task(data)
    return jsonify({'message': 'Task created successfully'}), HTTP_CREATED

@todo_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """
    PUT /tasks/<id>
    Updates an existing task.
    Optional fields:
    - title, description, due_date, status_id, tag_id

    Returns:
    - 200 on success
    - 400 if invalid FK
    - 404 if task not found
    """
    data = request.get_json()
    task = get_task_id(id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND

    if data.get('status_id') and not status_exists(data['status_id']):
        return jsonify({'error': 'Invalid status_id'}), HTTP_BAD_REQUEST
    if data.get('tag_id') and not tag_exists(data['tag_id']):
        return jsonify({'error': 'Invalid tag_id'}), HTTP_BAD_REQUEST

    update_task_model(id, data)
    return jsonify({'message': 'Task updated successfully'}), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    DELETE /tasks/<id>
    Deletes a task by ID.

    Returns:
    - 200 if successfully deleted
    - 404 if not found
    """
    task = get_task_id(id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND
    delete_task_model(id)
    return jsonify({'message': 'Task deleted successfully'}), HTTP_OK