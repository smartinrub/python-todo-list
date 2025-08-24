# python-todo-list

## Getting Started

Activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -e .
```

## Run locally

```bash
flask --app flaskr run --debug
```

### Create task

```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"name": "test"}'
```

### Get all tasks

```bash
curl http://127.0.0.1:5000/tasks
```

### Update task

```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d '{"name": "updated"}'
```

### Delete task

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/2
```
# python-todo-list
