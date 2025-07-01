from flask import Blueprint, request, jsonify
from db import get_connection

todo_bp = Blueprint('todo', __name__)

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
TASK_TABLE = 'task'

@todo_bp.route('/tasks', methods=['GET'])
def get_tasks():
    with get_connection() as conn:
        cursor = conn.execute(f"SELECT * FROM {TASK_TABLE}")
        tasks = [dict(row) for row in cursor.fetchall()]
    return jsonify(tasks), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    with get_connection() as conn:
        task = conn.execute(
            f"SELECT * FROM {TASK_TABLE} WHERE task_id = ?", (id,)
        ).fetchone()

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

    title = data['title']
    description = data.get('description', '')
    due_date = data.get('due_date') 
    status_id = data['status_id']
    tag_id = data['tag_id']
    user_id = data.get('user_id')  

    with get_connection() as conn:
        conn.execute(f"""
            INSERT INTO {TASK_TABLE} (title, description, due_date, status_id, 
            tag_id, user_id) VALUES (?, ?, ?, ?, ?, ?)""", 
            (title, description, due_date, status_id, tag_id, user_id))
        conn.commit()

    return jsonify({'message': 'Task created successfully'}), HTTP_CREATED

@todo_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()

    title = data.get('title')
    description = data.get('description', '')
    due_date = data.get('due_date')
    status_id = data.get('status_id')
    tag_id = data.get('tag_id')

    with get_connection() as conn:
        task = conn.execute(f"SELECT * FROM {TASK_TABLE} WHERE task_id = ?",
                             (id,)).fetchone()
        if task is None:
            return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND

        conn.execute(f"""
            UPDATE {TASK_TABLE}
            SET title = ?, description = ?, due_date = ?, status_id = ?, 
            tag_id = ? WHERE task_id = ?""", 
            (title, description, due_date, status_id, tag_id, id))
        conn.commit()

    return jsonify({'message': 'Task updated successfully'}), HTTP_OK

@todo_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    with get_connection() as conn:
        task = conn.execute(f"SELECT * FROM {TASK_TABLE} WHERE task_id = ?", 
                            (id,)).fetchone()
        if task is None:
            return jsonify({'error': 'Task not found'}), HTTP_NOT_FOUND

        conn.execute(f"DELETE FROM {TASK_TABLE} WHERE task_id = ?", (id,))
        conn.commit()

    return jsonify({'message': 'Task deleted successfully'}), HTTP_OK