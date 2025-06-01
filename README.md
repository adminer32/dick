# 接龙管家示例

本项目提供一个简单的接龙管家实现，包含前端页面、后端代码以及数据库初始化脚本。

## 目录结构

- `backend/`  后端 Flask 服务
- `frontend/` 前端页面
- `db/`       数据库初始化脚本和文件存放位置

## 使用方法

1. 创建并初始化数据库：

```bash
sqlite3 db/solitaire.db < db/init.sql
```

2. 安装依赖并启动后端：

```bash
cd backend
pip install -r requirements.txt
python app.py
```

后端启动后默认监听在 `http://localhost:5000`。

3. 打开 `frontend/index.html` 即可看到前端页面，通过页面可以提交和查看接龙信息。

该示例仅用于演示，可以根据需要自行扩展功能。
