# 待办事项管理 API

一个基于 Flask + SQLite 的待办事项管理接口，支持任务的增删改查。

## 技术栈

- Python 3.13
- Flask 3.1
- SQLite（标准库 `sqlite3`）

## 运行方式

### 1. 创建虚拟环境并安装依赖

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 启动服务

```
python app.py
```

### 3. 访问

浏览器打开 http://127.0.0.1:5000

## 接口说明

| 方法 | 路径 | 说明 | 状态码 |
|---|---|---|---|
| GET | `/` | 健康检查 | 200 |
| GET | `/api/tasks` | 查询所有任务 | 200 |
| GET | `/api/tasks/<id>` | 查询单个任务 | 200 / 404 |
| POST | `/api/tasks` | 新增任务 | 201 / 400 |
| DELETE | `/api/tasks/<id>` | 删除任务 | 200 / 404 |

## 目录结构

```
todo-api/
├── app.py              # 入口，路由定义
├── db.py               # 数据库连接与建表
├── requirements.txt    # 依赖清单
├── data/               # 数据库文件（不提交 git）
└── .gitignore
```

## 开发备注

- 数据库文件是 `data/todo.db`，首次运行自动创建
- 所有写操作都需要 `conn.commit()` 才会真正落盘
- SQL 参数一律用 `?` 占位，不拼接字符串
