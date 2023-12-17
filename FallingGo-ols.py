#20231213
from threading import Lock
from swdlc import *
from swdlc import getip
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askokcancel
from tkinter import messagebox
import ctypes
import logging
from time import sleep
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s'
                    ,filename='fgolslog.log',level=logging.DEBUG)
#以下是服务器参数，请自行修改
supported=["FGcstd231113"]#str类型列表，每一项表示一个支持的游戏名及版本号，名称要与客户端一致
serverport=26255#int类型，服务器使用的端口号
userport=26256#int类型,客户端使用的端口号
n=2#int类型，每一局的玩家数
#服务器参数定义结束
edition='2.2.8'
#sys.stderr=open('errlog.txt','a+')
win=Tk()
win.title('FallingGo Online Server')
win.update()
win.geometry('%dx%d'%(400,400))
ent=Frame(win)
le=Label(ent,text='服务器IP:')
ie=Entry(ent,state='disabled')
mtext=ScrolledText(win,state='disabled')
le.pack(side='left')
ie.pack(side='right')
ent.pack()
mtext.pack()
a={i:[] for i in supported}
lock=Lock()
t=[]
ie.config(state='normal')
ie.insert(1,getip())
ie.config(state='disabled')
#out=sys.stdout

whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)
class InsertText():
    @staticmethod
    def write(a):
        #print(a,file=out)
        mtext.config(state='normal')
        mtext.insert('end',a+'\n')
        mtext.config(state='disabled')
    flush=0
fileout=InsertText()
#print(1)
def rece(obj):
    global t
    if not obj[0] in a:
        send(['s'],str(obj[1]),str(userport))
        return
    if obj[-1]=='cancel':
        fileout.write(str(obj[0:2])+"is canceling connection")
        t=a[obj[0]]
        for i,j in enumerate(t):
            if j==obj[1]:
                a[obj[0]].pop(i)
                return
        else:
            logging.info('UNFIND USER:'+str(obj))
            return
    fileout.write(str(obj)+"is connecting")
    sleep(1)
    send(['u',edition],str(obj[1]),str(userport))
    lock.acquire()
    t=a[obj[0]]
    t.append(obj[1])
    logging.debug(str(t))
    if len(t)==n:
        sleep(1)
        fileout.write("boost users "+str(t))
        for i in t:
            send(['c',t],str(i),str(userport))
        a[obj[0]]=[]
    lock.release()


def ip_manager():
    "检查IP，网络连接及相关"
    if myip=='127.0.0.1':
        messagebox.showerror('网络错误','检测到您未连接到局域网')
        os._exit(0)
    if init(serverport):
        messagebox.showerror('端口错误','检测到您的端口已经被占用\n您是不是启动了多个FallingGo服务器窗口？')
        os._exit(0)
    receive(rece)
ip_manager()
def on_closing():
    if askokcancel('OLS提示','真的要退出吗？'):
        win.destroy()
        logging.debug("DESTORY!")
        for j in a:
            for i in a[j]:
                logging.debug(i)
                send(['e',i],str(i),str(userport))
            
win.protocol("WM_DELETE_WINDOW",on_closing)
win.mainloop()
