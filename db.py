import sqlite3

#Connection to the database
def get_connection():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

#Initialize Database, it sets up database so the app works.
def init_db(): 
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS user(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS status (
                status_id INTEGER PRIMARY KEY AUTOINCREMENT,
                status_name VARCHAR(50) NOT NULL UNIQUE,
                status_order INT NOT NULL
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tag (
                tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag_name VARCHAR(50) NOT NULL UNIQUE,
                tag_order INT NOT NULL
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS task (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INT NOT NULL,
                status_id INT NOT NULL,
                tag_id INT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                due_date DATE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(user_id) 
                ON DELETE CASCADE,
                FOREIGN KEY (status_id) REFERENCES status(status_id),
                FOREIGN KEY (tag_id) REFERENCES tag(tag_id)
            )
        """)
        
        conn.execute("""
            INSERT OR IGNORE INTO status (status_name, status_order)
            VALUES
                ('Not Started', 1),
                ('Pending', 2),
                ('In Progress', 3),
                ('Completed', 4)
        """)
        
        conn.execute("""
            INSERT OR IGNORE INTO tag (tag_name, tag_order)
            VALUES
                ('Work', 1),
                ('Personal', 2),
                ('Important', 3),
                ('House Chores', 4),
                ('Study', 5)
        """)
#Execute sql command that modifies data 
def execute_query(query, params=()):
    with get_connection() as conn:
        conn.execute(query, params)
        conn.commit()
        
#Execute a SQL query and return all rows as dictionaries
def fetch_all(query, params=()):
    with get_connection() as conn:
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()
    return [dict(row) for row in rows]

#Execute a SQL query and return a single row as a dictionary
def fetch_one(query, params=()):
    with get_connection() as conn:
        row = conn.execute(query, params).fetchone()
    return dict(row) if row else None