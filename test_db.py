from db import init_db, get_db

init_db()                                   # 建表

conn = get_db()
tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type = 'table'"
).fetchall()
print("表:", [t["name"] for t in tables])
conn.close()