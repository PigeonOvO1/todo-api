from flask import Flask, jsonify, request

from db import get_db, init_db

app = Flask(__name__)


@app.route("/")
def index():
    return "Todo API is running!"

# 查所有
@app.route('/api/tasks')
def list_tasks():
    conn = get_db()
    rows = conn.execute(
        "SELECT id,title,done,created_at FROM tasks ORDER by id"
    ).fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])

# 查单个
@app.route('/api/task/<int:task_id>')
def get_task(task_id):
    conn = get_db()
    row = conn.execute(
        "SELECT id ,title,done,created_at FROM tasks where id = ?",
        (task_id,)
    ).fetchone()
    conn.close()

    if row is None:
        return jsonify({"error":f"任务{task_id}不存在"}), 404

    return jsonify(dict(row))