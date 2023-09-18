

import subprocess
import os
from path_module import data_03_04_variant_asset


# for i, j in os.environ.items():
#     if "PXR" in i:
#         print(j)

# USD_ROOT = "/opt/USD"
# AUSD_ROOT = "/opt/arnold_usd"
# A_SDK_ROOT = "/opt/arnold_sdk"


USD_ROOT = "/usersetup/linux/usd/OpenUSD"
AUSD_ROOT = "/usersetup/linux/usd/arnoldUSD"
A_SDK_ROOT = "/usersetup/linux/installFiles/Apps_Plugin/arnold/sdk"

if "PYTHONPATH" in os.environ:
    os.environ["PYTHONPATH"] = os.environ["PYTHONPATH"] + ":" + f"{USD_ROOT}/lib/python"
else:
    os.environ["PYTHONPATH"] = f"{USD_ROOT}/lib/python"
os.environ["ARNOLD_PLUGIN_PATH"] = f"{AUSD_ROOT}/procedural"
os.environ["PXR_PLUGINPATH_NAME"] = f"{AUSD_ROOT}/plugin:{USD_ROOT}/lib/usd"
os.environ["LD_LIBRARY_PATH"] = f"{USD_ROOT}/lib:{A_SDK_ROOT}/Arnold-7.1.3.2-linux/bin"
os.environ['solidangle_LICENSE'] = '9053@10.0.2.15'

mayapy_path = "/usr/autodesk/maya2023/bin/mayapy"
mayausd_version = "0.19.0_202208181606-508c93f"
mayausd_version = "0.20.0_202211021008-b68700b"

tar_usd = "/gstepasset/WorkLibrary/8.FX_team/Test/changjin/Test/Test_USD_Pipe/_houdini/cache/usd/smoke_with_arnold_shader_v002.usd"
os.system(f"{mayapy_path} /usr/autodesk/mayausd/maya2023/{mayausd_version}/mayausd/USD/bin/usdview {data_03_04_variant_asset}")