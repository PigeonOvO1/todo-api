from app import app          # 把上面那个 app 导入进来

client = app.test_client()   # 测试客户端，不需要真的开服务器

r1 = client.get("/")                                  # 模拟 GET
print("GET /          ->", r1.status_code, r1.get_data(as_text=True))

r2 = client.post("/api/echo", json={"name": "小明"})    # 模拟 POST，传 JSON
print("POST /api/echo ->", r2.status_code, r2.get_json())

r3 = client.get("/nope")                              # 不存在的路径
print("GET /nope      ->", r3.status_code)