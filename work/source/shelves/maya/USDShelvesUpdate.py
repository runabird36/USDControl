

from pprint import pprint
from shutil import copy2
import os
from general_md_3x import platforms

from_local_path = ""
to_server_path  = ""
if platforms.is_linux():
    from_local_path = os.path.join(os.environ["HOME"], "maya/2023/prefs/shelves/shelf_G_USD.mel")
    to_server_path = os.path.join(os.environ["HGWEAVER_USD_ROOT"], "shelves")
elif platforms.is_windows():
    from_local_path = os.path.join(os.environ["HOMEPATH"], '문서', "maya/2023/prefs/shelves/shelf_G_USD.mel")
    if os.path.exists(from_local_path) == False:
        from_local_path = os.path.join(os.environ["HOMEPATH"], 'Documents', "maya/2023/prefs/shelves/shelf_G_USD.mel")
    to_server_path = os.path.join(os.environ["HGWEAVER_USD_ROOT"], "shelves")
    

if from_local_path != "" and to_server_path != "":
    print(from_local_path)
    print(to_server_path)
    copy2(from_local_path, to_server_path)