# author:杨森
# date: 2019/11/12 11:13
# file_name: execjs的操作
import execjs
import os

if __name__ == "__main__":
    # 执行js代码 使用execjs.eval
    print(execjs.eval("new Date"))
    # 获取当前execjs的路径
    print(execjs.get().name)
    # 切换js的路径
    os.environ["EXECJS_RUNTIME"] = "PhantomJS"
    print(execjs.get().name)
    # 执行js代码获取当前时间的时间戳
    print(execjs.eval("Date.now()"))

    # 使用execjs的预编译功能
    node = execjs.get()
    # 也可以直接采用execjs.compile()
    exct = node.compile("""
    function add(x,y){
    return x+y;
    }  
    """)
    print(exct.call("add", 1, 2))
    # 直接执行的代码
    print(execjs.exec_("var a=100;var b=200;return a+b;"))

