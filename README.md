# FallingGo 
## 由[SWD Studio](https://github.com/swdstudio "访问我们的github")以GNU GPLv3协议于CST 2024-4-3 13:55:39发布的软件

该程序版本号为2.3.0 内部版本号SWDFG-I240403

该应用占用了26256端口  服务器占用了26255端口

## 本程序开发环境：
系统：Microsoft Windows 7

编辑器：Microsoft Visual Studio Code 1.70.2 x64
## Python解释器环境：

Python IDLE 3.8.6rc1 for Windows（x64）

## 更新日志：

### 2024.04.03  [v2.3.0](https://github.com/swdstudio/FallingGo/releases/tag/v2.3.0 "前往")

1. 修复了之前关闭就卡死的bug

2. 增加投降等功能

3. 每次游戏结束后改为退回主窗口

4. 联机模式增加rematch功能，对一个对手“持续输出”

5. 修复重新连接服务器卡死的bug

6. 修复此前的Tcl异步处理的错误，以适应较旧版本的Python

注意，由于功能更新，2.3.0版本的客户端与之前版本不相容，最新的个人服务器已经拒绝对之前版本的访问

##### *声明：在此版本发布后计划不再发布除必要的bug修复之外的新功能*

### 2023.12.16 [v2.2.8](https://github.com/swdstudio/FallingGo/releases/tag/v2.2.8 "前往")

1. 增加了稳定性

2. “自由离线训练”增加撤回（键盘左键）恢复（键盘右键）功能

### 2023.12.14 v2.2.7
修复了已知的一些bug

1. 进行了对重复启动的检测

2. 支持键盘下棋进行

3. 新增“自由离线训练”功能，可以在任意大小棋盘上训练

4. 随包同时发布支持按键的swdz最新版

## 游戏规则：

游戏开始后双方在棋盘上交替落子，棋子会自动下落直到碰到棋盘底部或棋子

先连成4子者获胜

## 文件介绍：
运行时请启动FallingGo.py文件

swdz.py,onkey.py是SWD Coding Group开发的Python库，以GNU-GPL v3协议发布，本程序使用的内部版本号SWDZ-I240401

swdlc.py是SWD Coding Group开发的Python库，以GNU-GPL v3协议发布，本程序使用的内部版本号SWDLC-I240401-T01

cert.pem,key.pem是swdlc的自签名证书

FallingGo-ols.py是FallingGo的服务器端

rematch.py是FallingGo的重连接模块

fg.his是历史记录

fgolslog.log是服务器的日志文件

fglog.log是主程序的日志文件

### 支持我们
尝试使用我们的更多产品

欢迎访问[SWD Studio Github](https://github.com/swdstudio "访问我们的github")和[SWD Studio Website](http://swd-go.ysepan.com "访问我们的国内下载站")

We sincerely hope that you can **STAR** the project!

Of course, **Pull requests** and **raise issue** is welcomed,**帮助我们一起把这个开源软件做得更好**

