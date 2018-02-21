# use path to for contex info
import sys 
import os 
import logging 
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

import rf_config as config 
from rf_utils import project_info
from rf_utils import file_utils

RFPROJECT = config.Env.projectVar
RFPUBL = config.Env.publVar
moduleDir = os.path.dirname(sys.modules[__name__].__file__)
configFile = 'context_config.yml'

if config.isMaya: 
    import maya.cmds as mc 

# Project/asset/work/type/assetParent/assetName/step/process/app/workfile.ext
# Project/scene/work/episode/seq/shotName/step/process/app/workfile.ext

''' 
name: 
project = 'Two_Heroes'
entityType = 'asset' or 'scene'
workspaceArea 

entityGrp (type/episode)
entityParent
entityName 
step 
process 
app 
workfile 

path: 
entityPath 
stepPath 
processPath 
workspacePath 

publishPath
cachePath
outputPath
heroPath 
''' 
# context format 
# doublemonkey:ep1:sq001:sh001:anim:main:v001
# doublemonkey:chr:sunny:sunnyBase:rig:main:v001

class PathToConText(object):
    """Convert path input args to context"""
    def __init__(self, project=None, inputPath=None, task=str()):
        super(PathToConText, self).__init__()
        self.inputPath = inputPath
        
        # get path 
        if config.isMaya and not self.inputPath: 
            self.inputPath = mc.file(q=True, loc=True) if not mc.file(q=True, loc=True) == 'unknown' else (mc.file(q=True, sn=True) or str())
        
        # project information 
        if not project: 
            project = self.guess_project()
            logger.info('Guessing project -> %s' % project)

        self.projectInfo = project_info.ProjectInfo(project)
        self.configData = self.projectInfo.config_data()

        projectEnv = self.projectInfo.env()
        self.rootwork = projectEnv.get(RFPROJECT)
        self.rootpubl = projectEnv.get(RFPUBL)

        self.task = task
        self.path = self.strip_root()
        self.configStructure = self.configData.get('structure')

        self.asset = self.configStructure.get('asset').get('name')
        self.scene = self.configStructure.get('scene').get('name')
        self.elems = self.path.split('/')
        self.elemCount = len(self.elems) - 1
        self.versionKey = self.configData.get('version').get('key', 'v')
        self.versionPadding = self.configData.get('version').get('padding', 3)
        self.versionSep = self.configData.get('version').get('separation')
        self.noContext = read_config().get('noContext')


    def __str__(self):
        return self.context()

    def __repr__(self):
        return self.context()

    def guess_project(self): 
        if self.inputPath: 
            allProjects = project_info.ProjectInfo().list_all(asObject=False)
            result = [a for a in self.inputPath.split('/') if a in allProjects]

            if result: 
                project = result[0]
                return project

    def valid_root(self): 
        """ check if root on the path """ 
        return True if self.rootwork in self.inputPath or self.rootpubl in self.inputPath else False 

    def strip_root(self): 
        # strip rootwork first if not found strip rootpubl 
        if self.valid_root(): 
            replaceRoot = self.rootwork if self.rootwork in self.inputPath else self.rootpubl if self.rootpubl in self.inputPath else ''
            replaceRoot = '%s/' % replaceRoot if not replaceRoot[-1] == '/' else replaceRoot
            return self.inputPath.replace(replaceRoot, '')
        return str()

    def entity_type(self): 
        """ return entity type if result matched config """ 
        entityType = self.get_value('entityType')
        return entityType if entityType in [self.asset, self.scene] else self.noContext

    def project(self): 
        """ return project """ 
        return self.get_value('project')

    def workspace(self): 
        """ return work or publ """ 
        return self.get_value('workspace')

    def entity_group(self): 
        """ return assetType or episode """ 
        return self.get_value('entityGrp')

    def entity_parent(self): 
        """ return asset parent or sequence """
        return self.get_value('entityParent')

    def entity_name(self): 
        """ return assetName or shotName """ 
        return self.get_value('entity')

    def step(self): 
        """ return department """ 
        return self.get_value('step')

    def process(self): 
        """ return process name """ 
        return self.get_value('process')

    def app(self): 
        """ return app name """ 
        return self.get_value('app')

    def workfile(self): 
        """ return workfile name """ 
        return self.get_value('workfile')

    def version(self): 
        """ get file version """ 
        workfile = self.workfile()
        if workfile: 
            # find element that begin with "v" and follow by digits 
            result = [a for a in workfile.split(self.versionSep) if a[0] == self.versionKey and a[1:].isdigit()]
            if result: 
                version = result[0]
                return version

        return self.noContext


    def context(self): 
        """ return context """
        result = context_format(project=self.project(), entityType=self.entity_type(), entityGrp=self.entity_group(), entityParent=self.entity_parent(), entity=self.entity_name(), step=self.step(), process=self.process(), version=self.version(), workspace=self.workspace(), task=self.task)
        return result if result else str()

    
    def get_value(self, key): 
        level = self.configStructure.get(key).get('level') if self.configStructure.get(key).get('enable') else 100
        return self.elems[level] if self.elemCount >= level else self.noContext

    def set_task(self, task): 
        """ set task information to context if not supply """ 
        self.task = task 
        return task 


class Info(object):
    """Receive context to process path"""
    def __init__(self, context=None):
        super(Info, self).__init__()
        self.context = context
        if not context: 
            self.context = PathToConText()

        if self.context: 
            pass
            # continue 


        
def read_config(): 
    """ read context config """ 
    config = '%s/%s' % (moduleDir, configFile)
    data = file_utils.ymlLoader(config)
    return data 


def context_format(project=str(), entityType=str(), entityGrp=str(), entityParent=str(), entity=str(), step=str(), process=str(), version=str(), workspace=str(), task=str()): 
    """ project::entity::entityGrp::entityParent::entity::step::process::version::workspace """
    context = str()
    data = read_config()
    key = {
            'project': project, 
            'entityType': entityType, 
            'entityGrp': entityGrp, 
            'entityParent': entityParent, 
            'entity': entity, 
            'step': step, 
            'process': process, 
            'version': version, 
            'workspace': workspace, 
            'task': task
            }

    contextFormat = data.get('format')
    sepkey = data.get('separator')
    elems = contextFormat.split(sepkey)
    keyElems = [key.get(a, str()) for a in elems if key.get(a)]
    
    if keyElems: 
        context = sepkey.join(keyElems)
    else: 
        logger.error('No context found')
    
    return context 
