import os
import rf_config as config
import logging 

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def set_default(app): 
    # set styleSheet 
    styleSheetPath = config.Software.defaultStyleSheet
    if os.path.exists(styleSheetPath) :
        try:
            app.setStyle('plastique')
            data = open(styleSheetPath,'r').read()
            app.setStyleSheet(data+'QLabel { color : white; }')

        except Exception as e:
            logger.info(str(e))