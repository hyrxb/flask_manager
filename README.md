# flask_manager

基于flask的web管理框架

## 简介

flask_manager是一个基于[flask-adminlte-scaffold](https://github.com/xiiiblue/flask-adminlte-scaffold) 改进而来的简单后台管理系统。

主要将flask-adminlte-scaffold中的orm由peewe替换为sqlalchemy并精简了一些代码。

## 安装方式

```sh
git clone https://github.com/block-cat/flask_manager.git
```

然后安装依赖:

```sh
pip install -r requirements.txt
```

# 配置文件

config.ini

# 自动生成表结构

```sh
python3 manager shell

db.create_all()
```

# 启动

```python
python __init__.py
```
