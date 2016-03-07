import time
import sys


def currentTime():
    return int(time.time()), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def checkPythonVersion(minRequired=3,minSubRequired=0):
    if sys.version_info < (minRequired,minSubRequired):
        print("ERROR: Please use python version {0}.{1}+".format(minRequired,minSubRequired))
        exit(0)
    else:
        return True
