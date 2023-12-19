## FallingGo 是由SWD Studio以GNU GPL协议于GMT+8 2023-12-15 13:49:18发布的软件

该程序版本号为2.2.7 内部版本号SWDFG-I231214

该应用占用了26256端口  服务器占用了26255端口

### 本程序开发环境：
系统：Windows 10 2016 LTSB

### Python解释器环境：

Python IDLE 3.13.0a02 for Windows（x64）

建议使用CPython 3.8.10及以上环境运行

### 更新日志：
##### 2023.12.16 2.2.8

增加了稳定性

“自由离线训练”增加撤回（键盘左键）恢复（键盘右键）功能

##### 2023.12.14 2.2.7
修复了已知的一些bug

进行了对重复启动的检测

支持键盘下棋进行

新增“自由离线训练”功能，可以在任意大小棋盘上训练

随包同时发布支持按键的swdz最新版

### 游戏规则：

游戏开始后双方在棋盘上交替落子，棋子会自动下落直到碰到棋盘底部或棋子

先连成4子者获胜

### 文件介绍：
运行时请启动FallingGo.py文件

swdz.py是SWD Coding Group开发的Python库，以GNU-GPL协议发布，本程序使用的内部版本号SWDZ-I231201
swdlc.py,onkey.py是SWD Coding Group开发的Python库，以GNU-GPL协议发布，本程序使用的内部版本号SWDLC-I231202-T01
cert.pem,key.pem是swdlc的自签名证书
FallingGo-ols.py是FallingGo的服务器端
fg.his是历史记录
fgolslog.log是服务器的日志文件
fglog.log是主程序的日志文件
