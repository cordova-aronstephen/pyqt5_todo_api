from flask import Blueprint, request, jsonify
from db import get_db

todo_bp = Blueprint('todo', __name__)

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
TASK_TABLE = 'tasks'

@todo_bp.route('/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    cursor = db.execute(f'SELECT * FROM {TASK_TABLE}')
    tasks = [dict(row) for row in cursor.fetchall()]
    return jsonify(tasks), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    db = get_db()
    task = db.execute(f'SELECT * FROM {TASK_TABLE} WHERE id = ?', 
                      (id,)).fetchone()
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND
    return jsonify(dict(task)), HTTP_OK

@todo_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    title = data.get('title')
    if not title:
        return jsonify({'error': 'Title is required'}), HTTP_BAD_REQUEST

    description = data.get('description', '')

    db = get_db()
    db.execute(
        f'INSERT INTO {TASK_TABLE} (title, description) VALUES (?, ?)',
        (title, description)
    )
    db.commit()

    return jsonify({'message': 'Task created successfully'}), HTTP_CREATED

@todo_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    is_done = data.get('is_done', 0)

    db = get_db()
    task = db.execute(f'SELECT * FROM {TASK_TABLE} WHERE id = ?', 
                      (id,)).fetchone()
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND

    db.execute(f'''
        UPDATE {TASK_TABLE}
        SET title = ?, description = ?, is_done = ?
        WHERE id = ?
    ''', (title, description, is_done, id))
    db.commit()

    return jsonify({'message': 'Task updated successfully'}), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    db = get_db()
    task = db.execute(f'SELECT * FROM {TASK_TABLE} WHERE id = ?', 
                      (id,)).fetchone()
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND

    db.execute(f'DELETE FROM {TASK_TABLE} WHERE id = ?', (id,))
    db.commit()

    return jsonify({'message': 'Task deleted successfully'}), HTTP_OK