import sqlite3

conn = sqlite3.connect("data/todo.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER DEFAULT 0
)
""")

cur.execute("INSERT INTO tasks (title) VALUES (?)", ("买牛奶",))
cur.execute("INSERT INTO tasks (title) VALUES (?)", ("写代码",))
conn.commit()

cur.execute("SELECT id, title, done FROM tasks")
for row in cur.fetchall():            # fetchall 返回元组列表
    print(row)

print("总条数:", cur.execute("SELECT COUNT(*) FROM tasks").fetchone()[0])
conn.close()