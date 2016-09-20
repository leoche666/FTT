# -*- coding=utf-8 -*-
import time
import threading
import gevent
from functools import wraps
CONCURRENCY = 1000
'''
Created on Sept 20, 2016
@author: v-leoche
@summary:pressure test with gevent
'''
def GvtStress(count=1,increment=100):
    def outter_deco(func):
        from gevent import monkey
        monkey.patch_all()
        from gevent.pool import Pool
        pool = Pool(CONCURRENCY)

        def run(i,target,*args,**kwargs):
            for i in xrange(count):
                pool.spawn(target, *args, **kwargs)
            pool.join(timeout=60)

        def switch(count,pool,target,*args,**kwargs):
            i = count / CONCURRENCY
            j = count % CONCURRENCY

            if i == 0:
                run(count,target,*args,**kwargs)

            if i > 0 and j == 0:
                for k in xrange(i):
                    run(CONCURRENCY,target,*args,**kwargs)


            if i > 0 and j > 0 :
                for k in xrange(i):
                    run(CONCURRENCY,target,*args,**kwargs)
                run(j,target,*args,**kwargs)

            print "当前并发数:%d" % count

        @wraps(func)
        def inner_deco(*args, **kwargs):
            current = 0
            while True:
                if current >= count:
                    break
                else:
                    current = current + increment
                    switch(current,pool,func,*args, **kwargs)
        return inner_deco
    return outter_deco


'''
Created on Jan 4, 2016
@author: v-leoche
@summary:stress demo
'''
class TdStress(object):
    def __init__(self):
        self._pool = []
        self._res_queue = []
        self._error_count = 0
        self.lock = threading.Lock()


    def _target(self,*args):
        try:
            s_time = time.time()
            eval("args[0]%s" % str(args[1]))
            e_time = time.time()
            try:
                self.lock.acquire()
                self._res_queue.append(e_time - s_time)
            finally:
                self.lock.release()
        except Exception:
            try:
                self.lock.acquire()
                self._error_count += 1
            finally:
                self.lock.release()

    def run(self,target=None,args=None,count=1):
        #prapare
        for i in range(count):
            _thread = threading.Thread(target=self._target,args=(target,args))
            self._pool.append(_thread)

    def start(self):
        for _thread in self._pool:
            _thread.start()

    def wait(self):
        for _thread in self._pool:
            _thread.join()
        self._pool = []


    def control(self,count=1,increment=100,target=None,args=()):
        current = 0
        while True:
            if current >= count:
                break
            else:
                current = current + increment
                self.run(target=target,args=args,count=current)
                self.start()
                self.wait()
                self.printer(current)

    #you can defined your function for printing something you want
    def printer(self,current):
        tAgv = 0
        _count = len(self._res_queue)
        for i in range(_count):
            tAgv = self._res_queue[i] + tAgv
        print "当前并发数:%d" % current
        print "平均响应时间:%f" % (tAgv / _count)
        print "失败请求次数:%d" % self._error_count
        print "请求失败率%f" %   (float(self._error_count) / float(current))
        self._pool=[]
        self._res_queue=[]
        self._error_count = 0
