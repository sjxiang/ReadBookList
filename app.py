from flask import Flask, render_template

app = Flask(__name__)


name = "Xiangshengjie"
books = [
    {
        "title": "Writing an Interpreter in Go",
        "type": "编译原理"
    },
    {
        "title": "Operating Systems: Three easy pieces",
        "type": "操作系统"
    }
]

@app.route("/")
def index():
    return render_template("index.html", name=name, books=books)



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
    
    

    

"""