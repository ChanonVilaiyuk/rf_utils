# project utils 
import os
import sys 
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

import rf_config as config 
from rf_utils import file_utils
RFSCRIPT_VAR = config.Env.scriptVar


class Path: 
	projectConfig = 'core/rf_config/project'
	configFile = 'project_config.yml'

class ProjectInfo(object):
	"""docstring for ProjectInfo"""
	def __init__(self, project=None):
		super(ProjectInfo, self).__init__()
		self.project = project

	def exists(self): 
		""" if input project valid """
		return True if self.project in self.list_all(False) else False 

	def list_all(self, asObject=True): 
		""" list all project in db """
		if asObject: 
			projects = self.list_all(False)
			return [ProjectInfo(a) for a in projects]
		else: 
			return ['Two_Heroes', 'project', 'projectName']

	def name(self): 
		""" name of a project """
		return self.project 

	def config_file(self): 
		""" get config file based on project. If project not exists, use default project config """ 
		projectSpecificConfig = '%s/%s/%s/%s' % (os.environ.get(RFSCRIPT_VAR), Path.projectConfig, self.project, Path.configFile)
		defaultProjectConfig = '%s/%s/%s' % (os.environ.get(RFSCRIPT_VAR), Path.projectConfig, Path.configFile)
		configFile = projectSpecificConfig if os.path.exists(projectSpecificConfig) else defaultProjectConfig
		return configFile 

	def config_data(self): 
		logger.debug('reading config -> %s' % self.config_file())
		return file_utils.ymlLoader(self.config_file()) if os.path.exists(self.config_file()) else dict()
	
	def env(self): 
		data = self.config_data()
		return data.get('env')

		
