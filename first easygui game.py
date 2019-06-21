import easygui as g
import sys

while 1:
    g.msgbox("hello,欢迎进入第一个界面小游戏")

    msg = "选择你想学习的内容"
    tittle = "小游戏互动"
    choices = ["谈恋爱","编程","琴棋书画","武术"]

    choice = g.choicebox(msg,tittle,choices)

    g.msgbox("你选择了："+ str(choice),"结果")

    msg = "你是否想要重新开始游戏？"
    tittle = "请选择"

    if g.ccbox(msg,tittle):
        pass
    else:
        sys.exit(0)