from app import app

c = app.test_client()

print("=" * 50)
print("Day 9 验收测试")
print("=" * 50)

print("\n【1】查全部")
r = c.get("/api/tasks")
print(f"  {r.status_code}  {r.content_type.split(';')[0]}  共 {len(r.get_json())} 条")

print("\n【2】新增一条正常任务")
r = c.post("/api/tasks", json={"title": "验收测试任务"})
print(f"  {r.status_code}  {r.get_json()}")
new_id = r.get_json()["id"]

print("\n【3】查这条任务")
r = c.get(f"/api/tasks/{new_id}")
print(f"  {r.status_code}  {r.get_json()}")

print("\n【4】参数校验：空字符串")
r = c.post("/api/tasks", json={"title": "   "})
print(f"  {r.status_code}  {r.get_json()}")

print("\n【5】参数校验：数字")
r = c.post("/api/tasks", json={"title": 123})
print(f"  {r.status_code}  {r.get_json()}")

print("\n【6】参数校验：超长")
r = c.post("/api/tasks", json={"title": "a" * 101})
print(f"  {r.status_code}  {r.get_json()}")

print("\n【7】参数校验：没传 JSON")
r = c.post("/api/tasks", data="not json", content_type="text/plain")
print(f"  {r.status_code}  {r.get_json()}")

print("\n【8】删除这条任务")
r = c.delete(f"/api/tasks/{new_id}")
print(f"  {r.status_code}  {r.get_json()}")

print("\n【9】再删一次（已不存在）")
r = c.delete(f"/api/tasks/{new_id}")
print(f"  {r.status_code}  {r.get_json()}")

print("\n【10】访问不存在的路径")
r = c.get("/api/nonexist")
print(f"  {r.status_code}  {r.content_type.split(';')[0]}  {r.get_json()}")

print("\n【11】方法不对")
r = c.put("/api/tasks")
print(f"  {r.status_code}  {r.content_type.split(';')[0]}  {r.get_json()}")

print("\n" + "=" * 50)
print("以上每行都应该是 JSON，没有 text/html")
print("=" * 50)
