from __future__ import print_function
from customUtilities.helperFunction import *
import threading


class logger(object):

    def __init__(self,logfilename):
        self.lock = threading.RLock()
        self.logfilename = logfilename

    def _print_log(self,mtype,msg):
        self.lock.acquire()
        try:      
            #Log file
            logfile = open(self.logfilename,'a')

            _,localtime=self.currentTime()
            time='['+localtime+']  '
            print(time,'['+mtype+']',msg,file=logfile)
            logfile.close()

        finally:
            self.lock.release()
    
    def info(self,msg):
        self._print_log('INFO', msg)
            
    def warn(self,msg):
        self._print_log('WARN', msg)
    
    def error(self,msg):
        self._print_log('ERR', msg)