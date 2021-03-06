import sys
import os

moduleDir = sys.modules[__name__].__file__
iconPath = '%s' % os.environ['RFSCRIPT']

ok = '%s/icons/%s' % (iconPath, 'OK_icon.png')
no = '%s/icons/%s' % (iconPath, 'X_icon.png')
dir = '%s/icons/%s' % (iconPath, 'dir_icon.png')
nodir = '%s/icons/%s' % (iconPath, 'nodir_icon.png')
maya = '%s/icons/%s' % (iconPath, 'maya_icon.png')
camera = '%s/icons/%s' % (iconPath, 'camera_icon.png')
cameraNa = '%s/icons/%s' % (iconPath, 'cameraNa_icon.png')
noimg = '%s/icons/%s' % (iconPath, 'tmp_thumbnail.jpg')
nopreview = '%s/icons/%s' % (iconPath, 'nopreview_icon.png')
gear = '%s/icons/%s' % (iconPath, 'gear_icon.gif')
success = '%s/icons/%s' % (iconPath, 'success_icon.gif')
failed = '%s/icons/%s' % (iconPath, 'failed_icon.gif')

# sg
sgWtg = '%s/icons/%s' % (iconPath, 'wtg_icon.png')
sgAprv = '%s/icons/%s' % (iconPath, 'aprv_icon.png')
sgPndgAprv = '%s/icons/%s' % (iconPath, 'p_aprv_icon.png')
sgPndgPub = '%s/icons/%s' % (iconPath, 'pub_icon.png')
sgFix = '%s/icons/%s' % (iconPath, 'fix_icon.png')
sgHold = '%s/icons/%s' % (iconPath, 'hld_icon.png')
sgIp = '%s/icons/%s' % (iconPath, 'ip_icon.png')
sgLate = '%s/icons/%s' % (iconPath, 'late_icon.png')
sgRevise = '%s/icons/%s' % (iconPath, 'rev_icon.png')
sgRdy = '%s/icons/%s' % (iconPath, 'rdy_icon.png')
sgNa = '%s/icons/%s' % (iconPath, 'sgna_icon.png')

# general 
logo = '%s/icons/%s' % (iconPath, 'riff_logo.png')