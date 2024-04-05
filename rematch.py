#rematch
import logging
from tkinter import *
from tkinter.ttk import *

import swdlc
from eventqueue import EventQueueForTkinter
def exit_rem_win():
    global ifplayagain
    rem_Tkqueue.add_event(func=rematch_window.destroy)

def rem_exit():
    global ifplayagain
    if remp<=-10:
        exit_rem_win()
    else:
        swdlc.send(['cancel rematch'])
        ifplayagain='exit'
        exit_rem_win()

def play_again():
    global ifplayagain
    ifplayagain='reconnect'
    rem_exit()
    swdlc.default_addr(ip=ols_ip,port=resport)

def rematch():
    global rem_Tkqueue,remp,ifplayagain
    remp+=1
    swdlc.send(['rematch'])
    if remp==2:
        ifplayagain='restart'
        exit_rem_win()
        return
    rem_Tkqueue.add_event(func=rem_btn.config,args={'state':'disable'
                          ,'text':'Rematch(1/2)'})

def show_oppo():
    global oppo_lab
    rematch_window.geometry('%dx%d'%(225,120))
    oppo_lab=Label(master=rematch_window,text='Your opposite has left')
    oppo_lab.pack(side='top')
    rematch_window.update()

def rem_rec(getten_Obj):
    global ifplayagain,remp
    if type(getten_Obj)!=type([]):
        return
    if getten_Obj==['rematch']:
        remp+=1
        if remp==2:
            ifplayagain='restart'
            exit_rem_win()

            return
        rem_Tkqueue.add_event(func=rem_btn.config,args={'text':'Rematch(1/2)'})
    elif getten_Obj==['cancel rematch']:
        remp-=100
        rem_Tkqueue.add_event(func=rem_btn.config,args={'state':'disable'})
        rem_Tkqueue.add_event(func=show_oppo)

def rematch_win():
    global rematch_window,rem_Tkqueue,remp,rem_btn,ifplayagain
    print(1)
    ifplayagain=0
    remp=0
    rematch_window=Tk()
    rematch_window.title('FallingGo')
    rematch_window.geometry('%dx%d'%(225,100))
    rematch_window.update()
    rem_label=Label(rematch_window,text='游戏结束！')
    rem_btn=Button(rematch_window,text="Rematch(0/2)",command=rematch)
    plag_btn=Button(rematch_window,text="Play Again",command=play_again)
    exit_btn=Button(rematch_window,text="Exit",command=rem_exit)
    #___begin window arrange
    rem_label.pack(side='top')
    rem_btn.pack(side='top')
    plag_btn.pack(side='bottom')
    exit_btn.pack(side='bottom')
    #___end window arrange
    rematch_window.protocol("WM_DELETE_WINDOW",rem_exit)
    rematch_window.update()
    swdlc.receive(rem_rec)
    rem_Tkqueue=EventQueueForTkinter(tk=rematch_window,delay_ms=100)
    rem_Tkqueue()
    rematch_window.mainloop()
    return ifplayagain
    #rematch_window.mainloop()
if __name__ == '__main__':
    rematch_win()
