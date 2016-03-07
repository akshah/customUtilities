from multiprocessing import Pool
from multiprocessing import cpu_count
from customUtilities.logger import logger
import traceback
import time


class processPool(object):
    '''
    Thread Pools that are meant to be used only once as they will be cleaned up
    '''
    numberOfCPUs = cpu_count()
    numThreads=None

    def __init__(self,numThreads):
        '''
        Constructor
        '''
        if numThreads is not None:
            self.numThreads = numThreads
        else:
            self.numThreads = self.numberOfCPUs
            
        self.pool = self._setUpP()
    
    '''
    Threading pieces
    '''
    # Creates the thread pool
    def _setUpP(self):
        pool = Pool(processes=self.numThreads)
        return pool
    
    # Will run the function with the arguments
    def runParallelWithPool(self, functionCall, args, logger=logger("processPool.log")):
        try:
            result = self.pool.map_async(functionCall, args) 
   
            loopCounter=0
            while not result.ready():
                loopCounter+=1
                if loopCounter == 600:
                    logger.info("ProcessPool: %s task(s) left in queue." % result._number_left)
                    loopCounter = 0
                time.sleep(1)
                
            toReturn=result.get()
            self.pool.close()
            self.pool.join()
            toReturnFinal=[]
            for value in toReturn:
                if value != None:
                    toReturnFinal.append(value)
            return toReturnFinal
        except:
            traceback.print_exc()
            print('Error in Pool run.')
            exit(1)
