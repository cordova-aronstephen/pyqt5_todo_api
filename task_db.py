from db import get_connection
from db import fetch_one, fetch_all, execute_query

TASK_TABLE = "task"

def get_all_tasks():
    query = f"SELECT * FROM {TASK_TABLE}"
    return fetch_all(query)

def get_task_id(task_id):
    query = f"SELECT * FROM {TASK_TABLE} WHERE task_id = ?"
    return fetch_one(query, (task_id,))

def insert_task(data):
    params = (
        data['title'],
        data.get('description', ''),
        data.get('due_date'),
        data['status_id'],
        data['tag_id'],
        data.get('user_id')
        )
    query = f"""
            INSERT INTO {TASK_TABLE}
            (title, description, due_date, status_id, tag_id, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
    execute_query(query, params)

def update_task_model(task_id, data):
    params = (
        data.get('title'),
        data.get('description', ''),
        data.get('due_date'),
        data.get('status_id'),
        data.get('tag_id'),
        task_id
        )

    query = f"""
            UPDATE {TASK_TABLE}
            SET title = ?, description = ?, due_date = ?,
                status_id = ?, tag_id = ?
            WHERE task_id = ?
        """
    execute_query(query, params)

def delete_task_model(task_id):
    query = f"DELETE FROM {TASK_TABLE} WHERE task_id = ?"
    execute_query(query, (task_id,))     