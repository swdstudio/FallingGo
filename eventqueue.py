from queue import Queue
#20240306
#support for tkinter
class EventQueue(object):
    def __init__(self,loop=False):
        self.loop=loop
        self.flag=True
        self._q=Queue()
    def add_event(self,func,args=tuple()):
        self._q.put((func,args),)
    def _call_func(self,target,args):
        try:
            if type(args)==type(()):
                target(*args)
            elif type(args)==type(dict()):
                target(**args)
            else:
                raise SyntaxError('Invalid arguments type.')
        except Exception as e:
            print(e)
            pass
    def __call__(self,after=None,args=tuple()):
        if self.loop:
            while self.flag:
                if not self._q.empty():
                    t=self._q.get()
                    self._call_func(t[0],t[1])
                    self._call_func(after,args) if after!=None else ...
        elif not self._q.empty():
            t=self._q.get()
            self._call_func(t[0],t[1])
class EventQueueForTkinter(object):
    def __init__(self,tk,delay_ms=1000):
        self._e=EventQueue(loop=False)
        self.tk=tk
        self.delay_ms=delay_ms
    def __setattr__(self,name,val):
        if name in ('loop','flag'):
            self._e.__setattr__(name,val)
        object.__setattr__(self,name,val)
    def add_event(self,func,args=tuple()):
        self._e.add_event(func,args)
    def __call__(self):
        self._e()
        self.tk.after(self.delay_ms,self.__call__)
if __name__=='__main__':
    from threading import Thread
    def testf():
        from time import sleep
        while 1:
            sleep(1)
            e.add_event(lambda x:print(x**2),args=(14,))
    tt=Thread(target=testf,daemon=True)
    def t(x,y):
        print(x+y)
    e=EventQueue(True)
    e.add_event(t,args=(7,7,))
    tt.start()
    e(after=lambda:print('The after function was called.'))
