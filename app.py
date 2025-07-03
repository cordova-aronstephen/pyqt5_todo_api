from flask import Flask, jsonify
from routes import todo_bp
from db import init_db

HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_NOT_FOUND = 400

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(todo_bp)
    
    init_db()
    
    @app.route("/")
    def index():
        return jsonify({
        'message': 'Welcome! This TODO API is developed by Team PyQt5.'
    })
    
    @app.errorhandler(404)
    def handle_not_found_error(e):
        return jsonify({'error': 'Not Found'}), HTTP_NOT_FOUND

    @app.errorhandler(Exception)
    def handle_internal_server_error(e):
        return jsonify({
            'error': 'Internal Server Error'
        }), HTTP_INTERNAL_SERVER_ERROR
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)