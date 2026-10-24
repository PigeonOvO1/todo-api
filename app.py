from flask import Flask, jsonify, request

from db import get_db, init_db

app = Flask(__name__)


@app.route("/")
def index():
    return "Todo API is running!"


@app.route('/api/tasks')
def list_tasks():
    conn = get_db()
    rows = conn.execute(
        "SELECT id,title,done,created_at FROM tasks ORDER by id"
    ).fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])