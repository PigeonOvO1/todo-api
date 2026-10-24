import logging

from flask import Flask, jsonify, request

from db import get_db, init_db, DB_PATH

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


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
@app.route('/api/tasks/<int:task_id>')
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

# 新增
@app.route('/api/tasks',methods = ['POST'])
def add_task():
    data = request.get_json(silent = True) or {}
    # title = str(data.get('title',"")).strip()
    raw = data.get('title',"")

    if not isinstance(raw,str):
        return jsonify({'error':'title必须是字符串'}),400

    title = raw.strip()

    if not title:
        app.logger.warning(f"title为空，已拒绝")
        return jsonify({"error":"title不能为空"}),400

    if len(title) > 100:
        return jsonify({"error": "title不能超过100个字符"}), 400

    conn = get_db()
    cur = conn.execute(
        "INSERT INTO tasks(title) VALUES(?)",(title,)
    )
    conn.commit()

    new_id = cur.lastrowid

    row = conn.execute(
        "SELECT id ,title,done,created_at FROM tasks where id = ?",
        (new_id,)
    ).fetchone()
    app.logger.info(f"新增任务id={new_id} title={title}")

    conn.close()

    return jsonify(dict(row)),201


# 删除
@app.route('/api/tasks/<int:task_id>',methods = ['DELETE'])
def delete_task(task_id):
    conn = get_db()
    cur = conn.execute(
        "DELETE FROM tasks WHERE id = ?",(task_id,)
    )
    conn.commit()
    conn.close()

    if cur.rowcount == 0:
        app.logger.warning(f"删除失败！任务{task_id}不存在")
        return jsonify({"error":f"任务{task_id}不存在"}),404

    app.logger.info(f"删除任务 id={task_id}")
    return jsonify({"deleted": task_id})

@app.errorhandler(404)
def handle_404(e):
    return jsonify({'error':'接口不存在', 'path':request.path}),404

@app.errorhandler(405)
def handle_405(e):
    return jsonify({'error':'请求方法不允许'}),405

@app.errorhandler(500)
def handle_500(e):
    app.logger.exception("未捕获的异常")
    return jsonify({'error':'服务器内部错误'}),500

if __name__ == "__main__":
    init_db()
    app.logger.info(f"服务启动，数据库{DB_PATH}")
    app.run(debug=True,port=5000)