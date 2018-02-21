import sys
import os
import logging

logger = logging.getLogger(__name__)

import rf_config as config
from shotgun_api3 import Shotgun

# connection to server
server = config.Shotgun.server
script = config.Shotgun.script
id = config.Shotgun.id
sg = Shotgun(server, script, id)
# sg = None

def init_key(inputKey): 
	script, id = config.Shotgun.getKey(inputKey)
	global sg
	sg = Shotgun(server, script, id)

