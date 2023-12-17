import turtle
def NULL():
    pass
resonkey=NULL
def upload():
    def keya():
        resonkey("a")
    turtle.onkey(keya,"a")
    def keyb():
        resonkey("b")
    turtle.onkey(keyb,"b")
    def keyc():
        resonkey("c")
    turtle.onkey(keyc,"c")
    def keyd():
        resonkey("d")
    turtle.onkey(keyd,"d")
    def keye():
        resonkey("e")
    turtle.onkey(keye,"e")
    def keyf():
        resonkey("f")
    turtle.onkey(keyf,"f")
    def keyg():
        resonkey("g")
    turtle.onkey(keyg,"g")
    def keyh():
        resonkey("h")
    turtle.onkey(keyh,"h")
    def keyi():
        resonkey("i")
    turtle.onkey(keyi,"i")
    def keyj():
        resonkey("j")
    turtle.onkey(keyj,"j")
    def keyk():
        resonkey("k")
    turtle.onkey(keyk,"k")
    def keyl():
        resonkey("l")
    turtle.onkey(keyl,"l")
    def keym():
        resonkey("m")
    turtle.onkey(keym,"m")
    def keyn():
        resonkey("n")
    turtle.onkey(keyn,"n")
    def keyo():
        resonkey("o")
    turtle.onkey(keyo,"o")
    def keyp():
        resonkey("p")
    turtle.onkey(keyp,"p")
    def keyq():
        resonkey("q")
    turtle.onkey(keyq,"q")
    def keyr():
        resonkey("r")
    turtle.onkey(keyr,"r")
    def keys():
        resonkey("s")
    turtle.onkey(keys,"s")
    def keyt():
        resonkey("t")
    turtle.onkey(keyt,"t")
    def keyu():
        resonkey("u")
    turtle.onkey(keyu,"u")
    def keyv():
        resonkey("v")
    turtle.onkey(keyv,"v")
    def keyw():
        resonkey("w")
    turtle.onkey(keyw,"w")
    def keyx():
        resonkey("x")
    turtle.onkey(keyx,"x")
    def keyy():
        resonkey("y")
    turtle.onkey(keyy,"y")
    def keyz():
        resonkey("z")
    turtle.onkey(keyz,"z")
    def key0():
        resonkey("0")
    turtle.onkey(key0,"0")
    def key1():
        resonkey("1")
    turtle.onkey(key1,"1")
    def key2():
        resonkey("2")
    turtle.onkey(key2,"2")
    def key3():
        resonkey("3")
    turtle.onkey(key3,"3")
    def key4():
        resonkey("4")
    turtle.onkey(key4,"4")
    def key5():
        resonkey("5")
    turtle.onkey(key5,"5")
    def key6():
        resonkey("6")
    turtle.onkey(key6,"6")
    def key7():
        resonkey("7")
    turtle.onkey(key7,"7")
    def key8():
        resonkey("8")
    turtle.onkey(key8,"8")
    def key9():
        resonkey("9")
    turtle.onkey(key9,"9")
    def keyUp():
        resonkey("Up")
    turtle.onkey(keyUp,"Up")
    def keyDown():
        resonkey("Down")
    turtle.onkey(keyDown,"Down")
    def keyLeft():
        resonkey("Left")
    turtle.onkey(keyLeft,"Left")
    def keyRight():
        resonkey("Right")
    turtle.onkey(keyRight,"Right")
    def keyspace():
        resonkey("space")
    turtle.onkey(keyspace,"space")
    '''
    def keyesc():
        resonkey('esc')
    turtle.onkey(keyesc,'Esc')
    
    #def key128():
    #    print('114515')
    #    resonkey("-")
    #turtle.onkey(key128,"-")
    def key129():
        resonkey("=")
    turtle.onkey(key129,"=")
    def key130():
        print('114514')
        resonkey("]")
    turtle.onkey(key130,"]")
    def key131():
        resonkey("[")
    turtle.onkey(key131,"[")
    def key132():
        resonkey(",")
    turtle.onkey(key132,",")
    def key133():
        resonkey(".")
    turtle.onkey(key133,".")
    def key134():
        resonkey("/")
    turtle.onkey(key134,"/")
    def key136():
        resonkey(";")
    turtle.onkey(key136,";")'''

def demo():
    "演示"
    global resonkey
    def res(onchr):
        print(onchr)
        return
    resonkey=res
    upload()
    turtle.home()
    turtle.listen()
    turtle.mainloop()

if __name__=='__main__':
    demo()
