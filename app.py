import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类  SB bug

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.root_path, "data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)


class User(db.Model):     # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 书名
    type = db.Column(db.String(20))   # 类型


@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)

@app.route("/")
def index():
    # user = User.query.first()
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.errorhandler(404) # 传入要处理的错误代码
def page_not_found(e): # 接受异常对象作为参数
    # user = User.query.first()
    return render_template('404.html'), 404 # 返回模板和状态码



if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)

"""
Flask 微框架
    请求响应处理 Werkzeug
    模板渲染     Jinja
    
    flask run 内置服务器运行 
        比如，司马 "from werkzeug.serving import run_simple" 
        
        
     
    app = Flask(__name__)
        实例化 Flask 这个类，创建一个程序对象 app
        
        
    @app.route("/")    
    def hello():      
        return "welcome to My ReadBookList"
        
        视图函数
            解析 url
            对应的处理函数
            
        修改 url 规则
            3 种
            
        修改视图函数名
            url_for("hello", name=1)  /?name=2 
        


模板渲染：
    {{ 变量|过滤器 }}
    
    render_template()
    

  
静态文件：
    生成静态文件 url
    添加 Favicon
    

数据库：
    Pychar有个小 bug
    
模板优化：
    自定义错误页面
    模板上下文处理函数
    模板继承    

    

"""
