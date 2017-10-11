## 项目说明
该项目是对 `chatterbot` 的一些使用和试验，**不成熟项目，不可用于线上环境**。

## 外部依赖
pip依赖：见 `requirements.txt`
## 功能
### 基于脚本的chatterbot
#### 脚本
`main.py`
#### 运行
```bash
python3 ./main.py
```

### 基于Django的chatterbot
项目位于 `django_app／` ，下面的操作都是在这个目录中进行的。

#### 准备
##### 安装Django
```bash
pip install django
```

##### 同步数据库
```bash
python manage.py migrate
```

##### 创建超级用户
```bash
python manage.py createsuperuser
```

##### 训练chatterbot
```bash
python manage.py train
```

##### 运行server
```bash
python manage.py runserver
```

web服务器默认监听5000端口，访问[http://127.0.0.0.1:5000](http://127.0.0.0.1:5000)就能访问页面了


## Python 2/3 兼容性说明
只能保证对python3的兼容性