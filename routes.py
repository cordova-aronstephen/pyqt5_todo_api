from flask import Blueprint, request, jsonify

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/tasks', methods=['GET'])
def get_tasks():
    pass

@todo_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    pass

@todo_bp.route('/tasks', methods=['POST'])
def create_task():
    pass

@todo_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    pass

@todo_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    pass