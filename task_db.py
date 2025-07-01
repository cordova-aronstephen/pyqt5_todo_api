from db import get_connection

TASK_TABLE = "task"

def get_all_tasks():
    with get_connection() as conn:
        cursor = conn.execute(f"SELECT * FROM {TASK_TABLE}")
        tasks = [dict(row) for row in cursor.fetchall()]
    return tasks

def get_task_id(task_id):
    with get_connection() as conn:
        row = conn.execute(
            f"SELECT * FROM {TASK_TABLE} WHERE task_id = ?",
            (task_id,)
        ).fetchone()
    return dict(row) if row else None

def insert_task(data):
    title = data['title']
    description = data.get('description', '')
    due_date = data.get('due_date')
    status_id = data['status_id']
    tag_id = data['tag_id']
    user_id = data.get('user_id')

    with get_connection() as conn:
        conn.execute(f"""
            INSERT INTO {TASK_TABLE}
            (title, description, due_date, status_id, tag_id, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, description, due_date, status_id, tag_id, user_id))
        conn.commit()

def update_task_model(task_id, data):
    title = data.get('title')
    description = data.get('description', '')
    due_date = data.get('due_date')
    status_id = data.get('status_id')
    tag_id = data.get('tag_id')

    with get_connection() as conn:
        conn.execute(f"""
            UPDATE {TASK_TABLE}
            SET title = ?, description = ?, due_date = ?,
                status_id = ?, tag_id = ?
            WHERE task_id = ?
        """, (title, description, due_date, status_id, tag_id, task_id))
        conn.commit()

def delete_task_model(task_id):
    with get_connection() as conn:
        conn.execute(
            f"DELETE FROM {TASK_TABLE} WHERE task_id = ?",
            (task_id,)
        )
        conn.commit()        