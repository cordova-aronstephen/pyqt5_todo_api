# TODO API
A simple RESTful API built with **Flask** for managing a TODO list.

## Description
The **TODO API** is a simple and lightweight RESTful API built with **Flask** for managing tasks in a **TODO list**. Designed and developed by Team PyQt5, this project supports full CRUD (Create, Read, Update, Delete) operations on tasks.

## Getting Started

### 📦 Prerequisites
Make sure you have the following installed:
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Python 3.13+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

### 📁 Installation

#### Clone the repository:
1.  Open `Visual Studio Code`
2.  Open a new terminal
3.  Run the command in your Terminal.

    ```
    git clone git@github.com:cordova-aronstephen/pyqt5_todo_api.git
    ```

#### Navigate into the project directory
1.  Click `File` → `Open Folder`
2.  Select the cloned `pyqt5_todo_api` folder

#### Create and activate virtual environment:
1.  Open a new Terminal
2.  Run the command in your Terminal.

    ##### For Windows

    ```
    py -m venv .venv
    cd .venv\Scripts
    activate
    ```

    ##### For Mac/Linux

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

#### Install dependencies:
Run the command in your Terminal.

```
pip install -r requirements.txt
```

### 🕹️ How to run
After doing the installation, you can choose an option how to run the TODO API.

#### Option 1: Run via VS Code Run/Debug
1.  Locate the `app.py`
2.  Click the `Run ▶️` button.

#### Option 2: Run via Terminal
1.  Open a new Terminal
2.  Run the command in your Terminal.

    ```
    flask --app app run
    ```

## HTTP Status Code

| Code | Status                | Description                                                                      |
|------|-----------------------|----------------------------------------------------------------------------------|
| 200  | OK                    | The request has succeeded.                                                       |
| 201  | Created               | The request has been fulfilled, and a new resource has been created.             |
| 400  | Bad Request           | The server could not understand the request due to invalid syntax.               |
| 404  | Not Found             | The server can't find the requested resource.                                    |
| 500  | Internal Server Error | The server encountered an internal error and was unable to complete the request. |

## Task Endpoints (CRUD)

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/tasks`         | Get all tasks          |
| GET    | `/tasks/<id>`    | Get a task by ID       |
| POST   | `/tasks`         | Create a new task      |
| PUT    | `/tasks/<id>`    | Update task by ID      |
| DELETE | `/tasks/<id>`    | Delete task by ID      |

> All endpoints return JSON and appropriate status codes (200, 201, 400, 404).

## API Endpoints

| Endpoint                                       | Description            |
|------------------------------------------------|------------------------|
| https://pyqt5-todo-api.onrender.com/           | Welcome route          |
| https://pyqt5-todo-api.onrender.com/tasks      | Returns all task       |
| https://pyqt5-todo-api.onrender.com/tasks/{id} | Returns task by its ID |

## Deployed TODO API link
- [🌐 TODO API on Render](https://pyqt5-todo-api.onrender.com/)
