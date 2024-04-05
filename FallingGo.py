#coding=utf-8
#    Copyright (C) 2020-2024  SWD Studio

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#     any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    You can contact us on <swd_studio@outlook.com>
#20240118
#program=FallingGo
#filename=FallingGo.py

import threading
import logging
import os
import sys
from tkinter import messagebox,simpledialog
from tkinter import *
from tkinter.ttk import *
from time import sleep

import swdz
import swdlc
from eventqueue import EventQueueForTkinter
from rematch import *
debug=False #Debuging

if debug:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s'
                    ,filename='fglog.log',level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s'
                    ,filename='fglog.log',level=logging.INFO)
    sys.stderr=open('fgerrlog.log','a+')
logging.debug('begins')
map_length=7+1 #begin at 1
map_wedth=5+1
_map_wedth,_map_length=5+1,7+1
win_num=4 #winning
gomap=[[[False for i in range(2)]
for j in range(map_wedth+1)]for k in range(map_length+1)]
maptop=[1 for i in range(map_length)] #the record of top
history=[]
his_pos=0
t=1 #1 black 0 white
onlinemode='offline'
myedition='2.3.0'
mycstd="FGcstd231218"
myside=0

def NULL(*args):
    logging.debug('an empty function is executed.')

def force_exit():
    os._exit(0)

def nexgame():
    "Begin next game初始化"
    global gomap,maptop,t,history,his_pos
    swdz.init(sd=50,sn=[map_length-1,map_wedth-1],psize=2,show_line_no=True)
    gomap=[[[False for i in range(2)]
    for j in range(map_wedth+1)]for k in range(map_length+1)]
    maptop=[1 for i in range(map_length)]
    f=open('fg.his','a+')
    f.write(str(history)+'\n')
    f.close()
    history=[]
    his_pos=0
    t=1
    swdz.left_click(add_point)
    swdz.color('black')
    swdz.clear()
    return

def mesbox(title_,info_,*args):

    global temp
    logging.debug('89')
    temp=Tk()
    temp.geometry('%dx%d'%(200,100))
    temp.title(title_)
    temp.update()
    tmes=Label(temp,text=info_)
    main_btn=Button(temp,text='Confirmed',width=10,command=temp.destroy)
    #___begin window arrange
    tmes.pack()
    main_btn.pack()
    #___end window arrange
    rubbish.append(temp)
    temp.mainloop()
    '''
    print(123)
    temp=Tk()
    print(temp)
    #temp.withdraw()
    a=messagebox.showinfo(title_,info_,*args)
    print(343425432)
    #temp.destroy()'''

def win_show():
    "show somebody is winning"
    global showmes
    swdz.notice(zhcnpoint()+"方胜利！","red")
    swdz.update()
    showmes=threading.Thread(target=mesbox,
                    name='showmas',
                    args=('游戏提示','游戏结束！\n'+zhcnpoint()+"方胜利！"),
                    daemon=True)
    showmes.start()

def win_judge_point(gx,gy):
    "胜利判定（前面有几行历史纪录处理）"
    global history,his_pos
    num=0
    if onlinemode=='offlinetest':
        while(len(history)!=his_pos):
            history.pop()
    history.append(0)
    history[his_pos]=gx
    his_pos+=1
    if maptop[gx]>=4:
        for i in range(1,map_wedth):
            if gomap[gx][i][t%2]:
                coti=True
                num+=1
                if num==win_num:
                    win_show()
                    return True
            else:
                coti=False
                num=0
    num=0
    for i in range(1,map_length):
        if gomap[i][gy][t%2]:
            coti=True
            num+=1
            if num==win_num:
                win_show()
                return True
        else:
            coti=False
            num=0
    #倾斜判定
    num=0;x=gx;y=gy
    side=t%2
    while gomap[x][y][side] and 0<=y<=map_wedth-1 and 0<=x<=map_length-1:
        num=num+1
        x+=1
        y+=1
    x=gx-1;y=gy-1
    while gomap[x][y][side] and 0<=y<=map_wedth-1 and 0<=x<=map_length-1:
        num=num+1
        x-=1
        y-=1
        if num>=win_num:
            win_show()
            return True
    if gx+gy<4:
        return
    num=0
    x=gx
    y=gy
    side=t%2
    while gomap[x][y][side] and 0<=y<=map_wedth-1 and 0<=x<=map_length-1:
        num=num+1
        x-=1;y+=1
    x=gx+1
    y=gy-1
    while gomap[x][y][side] and 0<=y<=map_wedth-1 and 0<=x<=map_length-1:
        num+=1
        x+=1;y-=1
        if num>=win_num:
            win_show()
            return True
    if t==(map_length-1)*(map_wedth-1):
        swdz.notice("和棋！","red")
        messagebox.showinfo('游戏提示','游戏结束\n和棋！')
        swdz.left_click(NULL)
        return True
    return 0

def char_point():
    return '●' if t%2 else  '○'

def zhcnpoint():
    return '黑' if t%2 else  '白'


def end_onkey(getkey):
    getkey=getkey.keysym
    if getkey=='t':
        nexgame()
        swdz.setonkey(key_res)
        swdz.left_click(add_point)
        swdz.bye()
        return
    elif getkey=='c':
        swdz.notice('回放模式,按左右箭头键控制回放','blue')
    elif getkey=='e':
        nexgame()
        swdz.setonkey(key_res)
        swdz.left_click(add_point)
        swdz.bye()
        return 'End'
        #swdz.notice('回放模式,按左右箭头键控制回放','blue')
    swdz.left_click(add_point)
    swdz.setonkey(key_res)
    swdz.listen()
    return

#@swdz.setonkey
def key_res(getkey):
    "处理键盘事件"
    global his_pos,history,t,maptop
    swdz.setonkey(NULL)
    getkey=getkey.keysym
    logging.debug(str(getkey))
    if getkey=='r':
        t+=1
        if onlinemode=='online':
            t=myside+1
            swdlc.send(['resign'])
        win_show()
        nexgame()
        swdz.update()
        swdz.listen()
        swdz.setonkey(key_res)
        return
    if onlinemode=='offlinetest':
        if getkey=='t':
            nexgame()
            swdz.setonkey(key_res)
            swdz.left_click(add_point)
            swdz.bye()
            return
        if getkey=='Left':#撤回
            from turtle import color
            if t==1:
                swdz.setonkey(key_res)
                return
            t-=1
            his_pos-=1
            maptop[history[his_pos]]-=1
            gomap[history[his_pos]][maptop[history[his_pos]]][t%2]=False
            swdz.block_fill(history[his_pos],maptop[history[his_pos]],'white')
            color('black')
            swdz.init(sd=50,sn=[map_length-1,map_wedth-1],psize=2,show_line_no=True)
            swdz.notice("请"+zhcnpoint()+"方落子...","black")
            swdz.update()
            swdz.listen()
            swdz.setonkey(key_res)
            return
        elif getkey=='Right':#取消
            if his_pos!=len(history):
                gomap[history[his_pos]][maptop[history[his_pos]]][t%2]=False
                swdz.draw(history[his_pos],maptop[history[his_pos]],char_point(),'black',50)
                maptop[history[his_pos]]+=1
                t+=1
                his_pos+=1
                swdz.notice("请"+zhcnpoint()+"方落子...","black")
                swdz.update()
                swdz.listen()
                swdz.setonkey(key_res)
                return
    try:
        getkey=int(getkey)
    except Exception as Er:
        swdz.setonkey(key_res)
        logging.debug(Er)
        return
    if add_point(tx=getkey,tmode=False)=='End':
        return
    swdz.setonkey(key_res)
    swdz.listen()

#@swdz.left_click
def add_point(tx,ty=None,tmode=True):
    "处理我方玩家落子"
    global gomap,t,maptop,if_win
    if t%2!=myside and onlinemode=='online':
        return
    if tmode:
        gx=swdz.t2g(tx)
    else:
        gx=tx
    if gx<=0 or gx>=map_length or maptop[gx]==map_wedth:
        return 0
    swdz.left_click(NULL)
    if onlinemode=='online':
        swdlc.send(['g',tx])
    gomap[gx][maptop[gx]][t%2]=True
    swdz.draw(gx,maptop[gx],char_point(),'black',50)
    swdz.update()
    if_win=win_judge_point(gx,maptop[gx])
    maptop[gx]+=1
    t+=1
    if if_win:
        if onlinemode=='offlinetest':
            swdz.setonkey(end_onkey)
            swdz.notice('游戏结束！按下T返回,按下C回放','blue')
            swdz.listen()
            swdz.update()
            return 'End'
        else:
            swdz.setonkey(key_res)
            swdz.left_click(add_point)
            swdz.bye()
            return 'End'
    swdz.left_click(add_point)
    swdz.notice("请"+zhcnpoint()+"方落子...","black")
    swdz.update()

def game_main():
    "游戏主函数"
    global add_point,map_wedth,map_length#,swdzq
    sleep(0.1)
    swdz.home()
    #swdzq=EventQueueForTkinter(swdz.gettkobj(),100)
    nexgame()
    if onlinemode=='online':
        map_length=7+1;map_wedth=5+1
    swdz.setonclosing(force_exit)
    swdz.free_mode(False)
    swdz.init(sd=50,sn=[map_length-1,map_wedth-1],psize=2,show_line_no=True)
    if onlinemode=='online':
        logging.debug('flag CONTOMAS')
        swdlc.receive(rece_mas)
        swdz.notice('连接成功！您执'+('黑' if myside else '白'),'blue')
    swdz.setonkey(key_res)
    swdz.listen()
    swdz.left_click(add_point)
    swdz.setwtitle(s='FallingGo')
    swdz.update()
    #swdzq()
    swdz.mainloop()
#Network mode
wait=True
ipnum=20
waitforres=threading.Lock()
resip="172.16.88.20"
resport="26255"
myip=swdlc.getip()
execfun=''
execflag=False

rubbish=[]

def wait_response(getten_Obj:list):
    "用于回应等待服务器发送的请求,\n个人水平有限,只想到了用主线程exec的方法解决该线程没有Tk对象mainloop的问题"
    global myside,execflag,execfun,wait
    if type(getten_Obj)!=type([]):
        logging.debug('P244'+str(getten_Obj))
        return
    logging.debug("wait_response"+str(getten_Obj))
    if getten_Obj[0]=='c':
        getten_Obj=getten_Obj[1]
        for i in range(len(getten_Obj)):
            if getten_Obj[i]==myip:
                wait=False
                execfun='''messagebox.showinfo('连接成功提示',"连接成功,您执"+ '''+('''"黑"''' if i else  '''"白"''')+')'
                #print("连接成功,您执"+ ('黑' if i else  '白'))
                myside=i
                #wait_window.destroy()
                swdlc.default_addr(ip=getten_Obj[not myside],port="26256")
                waitforres.release()
                return
    elif getten_Obj[0]=='m':
        #聊天信息
        execflag=True
        execfun='messagebox.showinfo('+getten_Obj[1]+','+getten_Obj[2]+')'
        waitforres.release()
    elif getten_Obj[0]=='e':
        execflag=True
        logging.debug("P268服务器终止连接")
        execfun='''messagebox.showerror('服务器错误',"错误：服务器摆大烂了")\nos._exit(0)'''
        waitforres.release()
        #os._exit(0)
    elif getten_Obj[0]=='u':
        if getten_Obj[1][:5]>myedition[:5]:
            execflag=True
            #print('更新提示',"新版本"+getten_Obj[1]+"已发布,可以更新")
            execfun='''messagebox.showinfo('更新提示',"新版本"+"'''+getten_Obj[1]+'''"+"已发布,可以更新")'''
            waitforres.release()
    elif getten_Obj[0]=='s':
        execflag=True
        logging.warning("服务器已停止对当前版本的支持,请求更新")
        execfun='''messagebox.showerror('ERROR',"服务器已停止对您当前版本的支持,请更新至最新版本")\nos._exit(0)'''
        waitforres.release()
    else:
        logging.info("服务器信息异常")

def cancel_connect():
    "取消连接"
    global execflag,execfun,wait
    wait_window.destroy()
    execflag=True
    execfun='main_win()'
    waitforres.release()
    swdlc.receive(NULL)
    swdlc.send([mycstd,myip,'cancel'])

def wait_win():
    "启动连接等待窗口"
    global wait_window,wait_win_que
    wait_window=Tk()
    wait_window.title('FallingGo')
    wait_window.geometry('%dx%d'%(225,100))
    wait_window.update()
    wel=Label(wait_window,text='连接成功！\n我们正在为您寻找对手\n正在等待服务器'+resip+'提供连接')
    wait_btn=Button(wait_window,text="取消",command=cancel_connect)
    #___begin window arrange
    wel.pack()
    wait_btn.pack()
    #___end window arrange
    wait_window.protocol("WM_DELETE_WINDOW",cancel_connect)
    wait_win_que=EventQueueForTkinter(tk=wait_window,delay_ms=100)
    rubbish.append(wait_window)
    wait_win_que()
    wait_window.mainloop()

def connect():
    "处理连接等待"
    global wait,ipnum,myside,wait_window,olsip,olsport
    swdlc.default_addr(ip=resip,port=resport)
    try:
        swdlc.send([mycstd,myip])
    except Exception as Er:
        logging.warning(Er)
        messagebox.showerror('连接错误',"错误：服务器未正确启动,请检查IP地址")
        return
    swdlc.init(26256)
    swdlc.receive(wait_response)
    main_window.destroy()
    wait_win_handle=threading.Thread(target=wait_win,daemon=True,name='wait_win')
    wait_win_handle.start()
    while True:
        waitforres.acquire()
        if execflag:
            logging.debug('P332:execute:\n'+execfun)
            if 'main_win' in execfun:
                wait_win_que.add_event(func=lambda :exec('wait_window.destroy()\ndel wait_window,wait_win_que'))
                #os.system('start /min python Fallinggo.py')
                #os._exit(0)
                return
            exec(execfun)
        if not wait:
            wait_win_que.add_event(func=lambda :exec('wait_window.destroy()'))
            #wait_window.destroy()
            logging.debug('P336:execute:\n'+execfun)
            break
    while True:
        swdlc.receive(rece_mas)
        game_main()#Next:rematch or leave
        result=rematch_win()
        logging.debug('P447'+result)
        if result=='reconnect':
            connect()
        elif result=='restart':
            myside=1-myside
            continue
        elif result=='exit':
            break

def ots_add_point(tx):
    "处理联机模式中对方玩家落子"
    global gomap,t,maptop
    gx=swdz.t2g(tx)
    gomap[gx][maptop[gx]][t%2]=True
    swdz.draw(gx,maptop[gx],char_point(),'black',50)
    if win_judge_point(gx,maptop[gx]):
        nexgame()
        #swdzq.add_event(func=swdz.bye)
        swdz.bye()
        return
    maptop[gx]+=1
    t+=1
    swdz.notice("请"+zhcnpoint()+"方落子...","black")
    swdz.update()

def rece_mas(gotten_Obj):
    "处理联机模式中对方发送信息"
    global t
    logging.debug("rec()\n"+str(gotten_Obj))
    if type(gotten_Obj)!=type([]):
        return
    if gotten_Obj[0]=='resign':
        t=myside
        win_show()
        nexgame()
        return
    elif gotten_Obj[0]=='g':
        gotten_Obj=gotten_Obj[1]
        ots_add_point(gotten_Obj)
        return

def mode_switch(ans):
    "函数工厂,用来回应按钮对应的函数"
    def btn1_offline():
        global onlinemode,map_wedth,map_length
        map_wedth,map_length=_map_wedth,_map_length
        onlinemode='offline'
        main_window.destroy()
        game_main()

    def btn2_autoonline():
        global onlinemode,resip,resport,map_wedth,map_length,ols_ip
        map_wedth,map_length=_map_wedth,_map_length
        onlinemode='online'
        resip="172.16.88.20"
        ols_ip=resip
        resport="26255"
        ip_manager()
        connect()
    def btn3_peronline():
        global onlinemode,resip,resport,map_wedth,map_length,ols_ip
        resip=simpledialog.askstring('连接到指定服务器','请指定服务器IP地址：')
        if type(resip)==type(None):
            return '1145141919810'
        if '.' not in resip:
            resip='.'.join(myip.split('.')[:3])+'.'+resip
        ols_ip=resip
        map_wedth,map_length=_map_wedth,_map_length
        #resip=input('请指定服务器IP地址：')
        resport="26255"
        onlinemode='online'
        ip_manager()
        connect()
    def btn4_olson():
        global onlinemode,resip,resport,map_wedth,map_length
        try:
            os.system('start /min python Fallinggo-ols.py')
            sleep(1.5)
            resip=myip
            resport="26255"
            onlinemode='online'
            ip_manager()
        except Exception as Er:
            logging.warning(Er)
            messagebox.showerror('异常','服务器启动失败')
        map_wedth,map_length=_map_wedth,_map_length
        connect()
    def btn5_setting():
        global map_wedth,map_length,gomap,onlinemode
        try:
            simans=simpledialog.askstring('棋盘大小设置','您希望离线模式下期盼长宽是(长大于宽,长宽在0-9之间,空格隔开)\n'+
                                          '(目前长宽%d,%d)'%(map_length-1,map_wedth-1))
            logging.debug(simans)
            if simans==None:
                return
            map_length1,map_wedth1=map(int,simans.split(' '))
            map_wedth,map_length=map_wedth1+1,map_length1+1
            gomap=[[[False for i in range(2)]for j in range(map_wedth+1)]for k in range(map_length+1)]
            if not(4<=map_wedth<=map_length<=10):
                logging.debug('Not Allowed Input')
                raise IndexError('UnExpect input')
        except Exception as Er:
            logging.debug(Er)
            messagebox.showerror('错误','你输入的是个啥？')
            os._exit(0)
        onlinemode='offlinetest'
        main_window.destroy()
        game_main()
    ans+=1
    if ans==1:
        return btn1_offline
    elif ans==2:
        return btn2_autoonline
    elif ans==3:
        return btn3_peronline
    elif ans==4:
        return btn4_olson
    elif ans==5:
        return btn5_setting
    elif ans==6:
        return copyrig
    else:
        return NULL

def copyrig():
    messagebox.showinfo('About Us',f'''
SWD FallingGo{myedition}版,
版权所有(c)2020-2023 SWD Studio
    本程序在适用法律范围内不提供品质担保。除非另作书面声明,版权持有人及其他程序提供者“概”不提供任何显式或隐式的品质担保,品质担保所指包括而不仅限于有经济价值和适合特定用途的保证。全部风险,如程序的质量和性能问题,皆由你承担。若程序出现缺陷,你将承担所有必要的修复和更正服务的费用。
    除非适用法律或书面协议要求,任何版权持有人或本程序按本协议可能存在的第三方修改和再发布者,都不对你的损失负有责任,包括由于使用或者不能使用本程序造成的任何一般的、特殊的、偶发的或重大的损失（包括而不仅限于数据丢失、数据失真、你或第三方的后续损失、其他程序无法与本程序协同运作）,即使那些人声称会对此负责
See the GNU General Public License for more details.
Go to swd-go.ysepan.com to download latest edition and other useful apps
''')
    return

def hide_window():
    "隐藏窗口"
    import ctypes
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        #ctypes.windll.kernel32.CloseHandle(whnd)
#MainWindow AREA

def main_win():
    "启动主窗口"
    global main_window

    main_window=Tk()
    main_window.title('FallingGo')
    main_window.geometry('%dx%d'%(225,190))
    main_window.update()
    wel=Label(main_window,text='Welcome to use FallingGo'+myedition)
    btn_text=('离线模式','默认服务器连接','连接指定服务器','启动本地服务器','自由离线训练','关于我们和免责声明')
    main_btns=[Button(main_window,text=btn_text[i],width=20,command=mode_switch(i)) for i in range(6)]
    #msl=Label(main_window,text='Info')
    #mst=ScrolledText(main_window,state='disabled')
    #___begin window arrange
    wel.pack()
    for i in main_btns:
        i.pack()
    #msl.pack()
    #mst.pack()
    #___end window arrange
    main_window.protocol("WM_DELETE_WINDOW",force_exit)
    main_window.attributes('-topmost',1)
    main_window.mainloop()


def ip_manager():
    "检查IP,网络连接及相关"
    global ip_manager
    if myip=='127.0.0.1':
        messagebox.showerror('网络错误','检测到您未连接到局域网')
        os._exit(0)
    if swdlc.init(26256):
        messagebox.showerror('端口错误','检测到您的端口已经被占用\n您是不是启动了多个FallingGo联机窗口？')
        os._exit(0)
    swdlc.receive(NULL)
    ip_manager=NULL

if __name__=="__main__" :
    waitforres.acquire()
    '''
    def startz():
        swdz.mainloop()
        swdz.bye()
    threading.Thread(target=startz,daemon=True,name='swdz')'''
    if not debug:
        hide_window()
    while True:
        main_win()
