import threading
from contextlib import closing
import os.path
import csv

from customUtilities.logger import logger

class outputWriter():

    def __init__(self,resultfilename=None,logger=logger('outputWriter.log')):
        if not resultfilename:
            print('Please give a result filename.')
            exit(0)
        self.lock = threading.RLock()
        self.resultfilename = resultfilename
        if os.path.exists(self.resultfilename):
            os.remove(self.resultfilename)
        self.logger=logger

    def resetparams(self):
        if os.path.exists(self.resultfilename):
            os.remove(self.resultfilename)

    def write(self,val,delimiter="|"):
        self.lock.acquire()
        try:
            with closing(open(self.resultfilename, 'a+')) as csvfile:
                writer = csv.writer(csvfile, delimiter=delimiter)
                writer.writerow(val)
        except:
            self.logger.error('Result writer failed!')
            exit(1)
        finally:
            self.lock.release()

    def loadtoDB(self,dbinfo):
        self.lock.acquire()
        try:
            self.logger.info("Pushing "+self.resultfilename+" to DB")
            if os.path.exists(self.resultfilename):
                self.logger.info('Loading to DB not ready yet!')
        except:
            self.logger.error('Loading to DB error.')

        finally:
            self.lock.release()
