import os, sys
if __name__ == "__main__":
    try:
        cur_filepath    = os.path.realpath(__file__)
        check_path      = os.path.dirname(cur_filepath)
        if check_path not in sys.path:
            sys.path.append(check_path)
    except:
        print("DCC debug mode")

import LUCY, platforms

class Path():
    def __init__(self, prj :str="") -> None:
        
        self.root_prefix    = ""
        self.prj_name       = ""
        
        
        if platforms.is_windows():
            self.root_prefix = "X:/projects"
        elif platforms.is_linux():
            self.root_prefix = "/projects"
        
        if prj != "":
            self.set_project_name(prj)
        else:
            prj_name = LUCY.get_project()
            if prj_name:
                self.set_project_name(prj_name)
            
    def _deco_check_path(decorated_func):
        def check_path(self, *args, **kwargs):
            try:
                _path = decorated_func(self, *args, **kwargs)
                
                if self.prj_name == "" and kwargs.get("prj") != None:
                    input_prj = kwargs.get("prj")
                    self.set_project_name(input_prj)
                    _path = decorated_func(self, *args, **kwargs)
                if _path != None and os.path.exists(_path) == False:
                    os.makedirs(_path)
                return _path
            except Exception as e:
                print(str(e), file=sys.stderr)
                print("Error : Use wrong argument ! Use prj, assetname, shotname", file=sys.stderr)
                return None
                
        return check_path
            
            
    def set_project_name(self, prj :str="") -> None:
        self.prj_name = prj
        
        
        
    # ========================================================================
    #               Assets
    # ========================================================================
    @_deco_check_path
    def get_asset_root_path(self, prj :str="") -> str:
        '''
            return asset dir path
        '''
        return f"{self.root_prefix}/{self.prj_name}/usd/assets"
    
    def get_asset_type_list(self, prj :str="") -> list:
        '''
            return asset type list
        '''
        return os.listdir(self.get_asset_root_path())
    
    def get_asset_type_path(self, prj :str="", assettype :str="") -> str:
        if assettype == "":
            assettype = LUCY.get_assettype()
            if assettype == None:
                return None
        return self.get_asset_root_path() + f"/{assettype}"
    
    def get_asset_list(self, prj :str="") -> list:
        '''
            return asset list which are in assets dir path
        '''
        whole_assets = []
        for asset_type in self.get_asset_type_list():
            assettype_dirpath = self.get_asset_type_path(assettype=asset_type)
            whole_assets.extend(os.listdir(assettype_dirpath))
        return whole_assets
    
    @_deco_check_path
    def get_asset_path(self, prj :str="", assettype :str="", assetname :str="") -> str:
        '''
            return asset folder path
        '''
        if assettype == "":
            assettype = LUCY.get_assettype()
            if assettype == None:
                return None
        if assetname == "":
            assetname = LUCY.get_assetname()
            if assetname == None:
                return None
        return self.get_asset_type_path(assettype=assettype) + f"/{assetname}"
    
    def get_asset_dirpath(self, assettype :str="", assetname :str="") -> str:
        '''
            return asset dir path
        '''
        return os.path.dirname(self.get_asset_path(assettype=assettype, assetname=assetname))
    
    
    
    
    # ========================================================================
    #               Shots
    # ========================================================================
    @_deco_check_path
    def get_shot_root_path(self, prj :str="") -> str:
        '''
            return shot dir path
        '''
        return f"{self.root_prefix}/{self.prj_name}/usd/sequence"
    
    def get_sequence_list(self, prj :str="") -> list:
        '''
            return sequence list
        '''
        return os.listdir(self.get_shot_root_path())
    
    def get_sequence_path(self, prj :str="", seq :str="") -> str:
        if seq == "":
            seq = LUCY.get_sequence()
            if seq == None:
                return None
        return self.get_shot_root_path() + f"/{seq}"
    
    def get_shot_list(self, prj :str="") -> list:
        '''
            return shot list which are in assets dir path
        '''
        whole_seq = []
        for seq_name in self.get_sequence_list():
            seq_dirpath = self.get_sequence_path(seq=seq_name)
            whole_seq.extend(os.listdir(seq_dirpath))
        return whole_seq
    
    @_deco_check_path
    def get_shot_path(self, prj :str="", seq :str="", shotname :str="") -> str:
        '''
            return shot folder path
        '''
        if seq == "":
            seq = LUCY.get_sequence()
            if seq == None:
                return None
        if shotname == "":
            shotname = LUCY.get_shot()
            if shotname == None:
                return None
        return self.get_sequence_path(seq=seq) + f"/{shotname}"
    
    def get_shot_dirpath(self, seq :str="", shotname :str="") -> str:
        '''
            return shot dir path
        '''
        return os.path.dirname(self.get_shot_path(seq=seq, shotname=shotname))
    
    
    
    
    
if __name__ == "__main__":
    _prj_name = "2022_09_pipelineEDU2"
    
    
    _engine = Path(prj=_prj_name)
    res = _engine.get_asset_root_path()
    print(f"생성자에서 프로젝트 이름 지정방식   : {res}")
    
    _engine = Path()
    res = _engine.get_asset_root_path(prj=_prj_name)
    print(f"함수를 통한 프로젝트 이름 지정방식  : {res}")
    
    try:
        _engine = Path()
        res = _engine.get_asset_root_path()
        print(f"DCC 툴 안에서 LUCY를 통한 프로젝트 이름 지정방식  : {res}")
    except Exception as e:
        print(str(e))
    
    res = _engine.get_asset_path(assettype="character", assetname="ryan")
    print(res)
    
    
    res = _engine.get_shot_dirpath(seq="EDU", shotname="EDU_0010")
    print(res)