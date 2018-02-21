import logging
import os, sys
from datetime import datetime

# logRoot = '%s/logs' % os.environ.get('RFSCRIPT', 'P:/rftool')
# logExt = 'log'
logRoot = '%s/logs' % os.environ.get('RFSCRIPT')
# logRoot = '//riff-data/Data/Data/logs'
logExt = 'log'

def name(toolName, user, createDir=True):
	date = str(datetime.now()).split(' ')[0]
	# userName = mc.optionVar(q='PTuser')
	userName = user
	logDir = '%s/%s/%s/%s' % (logRoot, date, toolName, userName)
	logName = '%s_%s_%s.%s' % (toolName, userName, date, logExt)

	if createDir:
		if not os.path.exists(logDir):
			os.makedirs(logDir)

	return '%s/%s' % (logDir, logName)

def init_logger(logFile, name=''):
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	remove_logger(name)

	# create file handler which logs even debug messages
	fh = logging.FileHandler(logFile)
	fh.setLevel(logging.DEBUG)
	fh.set_name('%s_FH' % name)
	
	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)
	ch.set_name('%s_CH' % name)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)

	return logger


def remove_logger(name=''): 
	logger = logging.getLogger()

	for handler in logger.handlers[::-1] :
		remove = False
		if handler.name: 
			if name in handler.name: 
				remove = True 
		if not name: 
			remove = True 

		if remove: 
			if type(handler).__name__ == 'StreamHandler':
				logger.removeHandler(handler)
				# print 'removed', handler

			if type(handler).__name__== 'FileHandler':
				logger.removeHandler(handler)
				handler.flush()
				handler.close()
				# print 'removed', handler

