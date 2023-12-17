#    Copyright (C) 2020-2023  SWD Studio

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
#    You can contact us on swd-go.ysepan.com
#20231211
import turtle as t
import onkey
import logging
d=20
n=32
free=True
blist=[]#functions
bmap={}
Debug=False
def NULL():
    pass
def home():
    try:
        t.home()
    except t.Terminator:
        t.home()

def bye():
    t.bye()

def NULL1():
    return "SHIT!"
def setwtitle(s='swdz(20231212)'):
    '''
用于修改窗口标题
setwtitle(s)
s:窗口标题
'''
    t.title(s)

def setbtndic():
    "初始化bmap"
    global blist,bmap
    for i in range(-n,2*n):
        for j in range(-n,2*n):
            bmap[(i,j)]=0
    blist=[NULL1]
    return 0

def setonkey(keyfun):#@
    "设置键盘单击事件"
    onkey.resonkey=keyfun
    onkey.upload()
    return keyfun
def setonclosing(delfun): #@
    '用于绑定窗口关闭时间触发的函数'
    root = t.getcanvas().winfo_toplevel()
    root.protocol("WM_DELETE_WINDOW",delfun)
    return delfun
def listen():
    '监听键盘（不阻塞线程）'
    t.listen()

def init(sd=20,sn=32,psize=1,show_line_no=True,background='white'):
    '''
init是初始化函数，在调用其他函数前先调用
init(sd=20,sn=32,psize=1)
sd:每个小方格的宽度，必须是偶数
sn:每边方格个数
或列表：(wedth,length)宽度，长度，要求宽度大于长度
psize:方格边线宽度
show_line_no:是否绘制行号和列号
'''
    global d,n,bmap,backgd,outrangeclick,orcfunc,nosqflag
    outrangeclick=NULL
    backgd=background
    d=sd
    
    t.hideturtle()
    t.pensize(1)
    t.speed(0)
    t.pu()
    t.bgcolor(backgd)
    if type(sn)==type([]):
        nosqflag=True
        if Debug:
            print('flagnosq')
        n=sn[0]
        sn[1]+=1
    else:
        nosqflag=False
        n=sn
    setbtndic()
    t.pensize(psize)
    drawmap(show_line_no)
    if nosqflag:
        if Debug:
            print(int(g2t(0)),int(g2t(sn[1])),int(g2t(sn[0]+1)),int(g2t(sn[0]+1)),'green')
        orcfunc=create_btn(0,sn[1],sn[0]+1,sn[0]+1,backgd,outrangeclick)
    liney=sn[1] if nosqflag else n
    for c in range(1,n+1):
        if show_line_no and c<=n:
            draw(c+0.4,liney,str(c),color='black',charsize=d//2)
    update()
        
    
def drawmap(show_line_no=True):
    '''
绘图函数，内部调用，不应由用户调用
drawmap(show_line_no=Ture)
show_line_no:是否绘制行号和列号
'''
    t.tracer(False)
    t.pu()
    c=1
    for i in range(-d//2*n,d//2*n+1,d):
        t.goto(i,-d/2*n)
        t.pd()
        t.goto(i,d/2*n)
        #if show_line_no and c<=n:
        #    t.write(str(c),font=('Arial',d//2,'normal'))
        t.pu()
        t.goto(-d/2*n,i)
        t.pd()
        t.goto(d/2*n,i)
        if show_line_no and c<=n:
            t.write(str(c),font=('Arial',d//2,'normal'))
        t.pu()
        c+=1
    t.update()

def t2g(tinput):
    return int((tinput+d/2*n)//d+1)

def g2t(ginput):
    return d*(ginput-1)-d/2*n
def draw (gx,gy,s,color,charsize=d//2):
    '''
draw用于在指定G坐标位置绘制字符
draw(gx,gy,s,color)
gx:x坐标
gy:y坐标
s:要显示的字符
color:颜色
'''
    tx,ty=g2t(gx),g2t(gy)
    t.color(color)
    t.goto(tx,ty)
    t.write(s,font=('Arial',charsize,'normal'))
def notice (s,color):
    '''
用于显示提示信息，显示位置在G坐标(1,0)处
s:要显示的信息
color:颜色
'''
    t.goto(g2t(1),g2t(0))
    t.color('white')
    t.write('▇'*50,font=('Arial',d//2+1,'normal'))
    t.color(color)
    t.write(s,font=('Arial',d//2,'normal'))
def click_not_free(tx,ty):
    gx,gy=map(t2g,(tx,ty))
    bv=bmap[(gx,gy)]
    if blist[bmap[(gx,gy)]]()=='SHIT!':
        if not (1<=gx<=n and 1<=gy<=n) and outrangeclick!=NULL:
            raise IndexError('点击位置错误')
        else:
            cf(tx,ty)
def update():
    t.update()
def left_click(f):
    '''
left_click装饰器函数，用法如下:
@left_click
def click(x,y):
    ...
当鼠标左键单击时，会调用click函数，传入参数为T坐标
'''
    global cf
    if not free:
        t.onscreenclick(click_not_free,1)
        cf=f
        return
    t.onscreenclick(f,1)
    return f
def mainloop():
    '''
主循环函数
'''
    t.mainloop()

def block_fill(gx,gy,color):
    '''
方块填充函数
'''
    tx,ty=g2t(gx),g2t(gy)
    t.color(color)
    k=d
    t.goto(tx,ty)
    t.begin_fill()
    t.goto(tx+k,ty)
    t.goto(tx+k,ty+k)
    t.goto(tx,ty+k)
    t.goto(tx,ty)
    t.end_fill()
def free_mode(f=None):
    global free
    if f==None:
        return free
    else:
        free=f
def create_btn(x1,y1,x2,y2,color,func):
    r=len(blist)#rank
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            block_fill(i,j,color)
            bmap[(i,j)]=r
    blist.append(func)
    return (x1,y1,x2,y2,r)
def remove_btn(h):
    blist[h[4]]=None
    x1=h[0];y1=h[1];x2=h[2];y2=h[3]
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            block_fill(i,j,'white')
            bmap[(i,j)]=0

def out_range_click(outrf):   #@
    outrangeclick=outrf
    if nosqflag:
        #orcfunc=create_btn(g2t(0),g2t(sn[1]),g2t(sn[0]+1),g2t(sn[0]+1),backgd,outrangeclick)
        remove_btn(orcfunc)
    
    return outrf
def demo():
    '''
演示函数
'''
    t.home
    setwtitle()
    init(20,[7,5],1,background='blue')
    block_fill(5,5,'grey')
    free_mode(0)
    h=create_btn(33,33,34,34,'black',lambda:print('clicked!'))
    #remove_btn(h)
    @left_click
    def click(x,y):
        gx,gy=t2g(x),t2g(y)
        notice(str(gx)+' '+str(gy),'dark green')
        block_fill(gx,gy,'green')
        draw(gx,gy,'A','white')
    @setonkey
    def res(onchr):
        print(onchr)
        return
    listen()
    mainloop()
if __name__=='__main__':
    demo()
