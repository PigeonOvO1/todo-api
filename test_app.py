from app import app, init_db
from db import get_db

conn = get_db()
conn.execute("DELETE FROM tasks")     # 清空，让每次测试从干净状态开始
conn.commit()
conn.close()

init_db()
c = app.test_client()

print("=== 查全部（空）===")
r = c.get("/api/tasks")
print(r.status_code, r.get_json())

print()
print("=== 新增两条 ===")
r = c.post("/api/tasks", json={"title": "买牛奶"})
print(r.status_code, r.get_json())
r = c.post("/api/tasks", json={"title": "写代码"})
print(r.status_code, r.get_json())

print()
print("=== 查全部 ===")
r = c.get("/api/tasks")
print(r.status_code, r.get_json())

print()
print("=== 查单个 ===")
r = c.get("/api/tasks/1")
print(r.status_code, r.get_json())
r = c.get("/api/tasks/999")
print(r.status_code, r.get_json())

print()
print("=== 新增失败：title 为空 ===")
r = c.post("/api/tasks", json={"title": "   "})
print(r.status_code, r.get_json())

print()
print("=== 删除 ===")
r = c.delete("/api/tasks/19")
print(r.status_code, r.get_json())
r = c.delete("/api/tasks/1")
print(r.status_code, r.get_json())