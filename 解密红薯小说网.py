import execjs
import os

os.environ["EXECJS_RUNTIME"] = "nodejs"
print(execjs.get().name)
exct = execjs.compile(open("./myjs.js","r",encoding="utf-8").read())
print(exct.call("onView",'100001126326','20191355608','绿地云龙文化旅游城',''))