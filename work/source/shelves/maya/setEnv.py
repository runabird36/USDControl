


import sys, os

path_list = [
                os.environ["HGWEAVER_USD_ROOT"]+"/module",
                os.environ["HGWEAVER_USD_ROOT"]+"/code"
            ]


pxr_PYTHONPATH = [
						""
					]


            
for _path in path_list:
    if _path in sys.path:
        continue
    sys.path.append(_path)






os.chdir(os.environ["HGWEAVER_USD_ROOT"]+"/../research")
usd_research_dir = os.getcwd()
os.environ['HGWEAVER_USD_RESEARCH'] = usd_research_dir

