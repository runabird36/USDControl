import maya.cmds as cmds

import os
import sys
import subprocess



def open_usdview():
    result = cmds.promptDialog(
                    title='USD view',
                    message='usd 파일 전체 경로를 입력해주십시오 :',
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')

    if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)



        mayaVer = 2023
        os.environ['MAYA_LOCATION'] = "/usr/autodesk/maya2023"
        os.environ['USD_LOCATION'] = "/usr/autodesk/mayausd/maya2023/0.19.0_202208181606-508c93f/mayausd/USD"
        target = text
        mayapyBinPath = os.path.join(os.environ['MAYA_LOCATION'], 'bin')
        if mayaVer == 2022:
            mayapyPath = os.path.join(mayapyBinPath, 'mayapy{ver}'.format(ver='' if sys.version_info.major == 3 else '2'))
        else:
            mayapyPath = os.path.join(mayapyBinPath, 'mayapy')  
        usdRootPath = os.environ['USD_LOCATION']
        
        # sanitise the path separators - slightly inefficient
        mayapyPath = mayapyPath.replace('\\', os.path.sep).replace('/', os.path.sep)
        usdRootPath = usdRootPath.replace('\\', os.path.sep).replace('/', os.path.sep)
        
        # finally build out the nice pathing
        usdToolsPath = os.path.join(usdRootPath, "bin")
        usdLibPath = os.path.join(usdRootPath, "lib")
        usdViewPath = os.path.join(usdToolsPath, 'usdview')
        
        # Install OpenGL module, if needed
        try:
            import OpenGL
        except:
            subprocess.check_call([mayapy, '-m', 'pip', 'install', 'PyOpenGL==3.1.0'])
        if sys.platform in ('win32'): 
            creationflags = 0x08000000 # CREATE_NO_WINDOW only for win32, not MacOS or Linux
        else:
            creationflags = 0
        
        print([mayapyPath, usdViewPath, target])
        subprocess.Popen([mayapyPath, usdViewPath, target], creationflags=creationflags)