from flask import Flask
from routes import todo_bp
from db import init_db

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(todo_bp)
    
    init_db()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)