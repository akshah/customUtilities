#!/usr/bin/python

from Logger.logger import logger

logger=logger('Test.log')

msg='This is test.'
logger.info(msg)
logger.error(msg)
logger.warn(msg)