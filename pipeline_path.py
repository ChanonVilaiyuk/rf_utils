# call path 
import os
import sys 

def tmpPath(toolname): 
	""" temp dir for tool """
	return '%s/%s' % (os.environ.get('temp'), toolname)