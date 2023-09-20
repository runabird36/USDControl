from dataclasses import dataclass
from pprint import pprint


@dataclass
class SGpkg():
    """
    {
        "Master" : [
                        {"DEPARTMENT" : str, "PKG_VERSION" : list
                                                            [{
                                                                "VERSION_NUM" : str,
                                                                "PUBS" : list
                                                            }] 
                                                    }
                    ]
    }
    """
    info            :dict
    

    def init_data(self, *args) -> None:
        self.top_layer_name = "Master"
        self.layer_list = self.info.get(self.top_layer_name)

    def get_last_pkg_version(self, selected_department :str) -> str:
        last_ver = ""
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                if _lyr.get("PKG_VERSION")[-1].get("VERSION_NUM") == "v001":
                    return ""
                last_ver = _lyr.get("PKG_VERSION")[-1].get("VERSION_NUM")
                break
        return last_ver

    def add_pkg_version(self, selected_department :str) -> str:
        def version_up(cur_vernum :str) -> str:
            temp_cur_int = int(cur_vernum.replace("v", ""))
            temp_cur_int += 1
            return "v" + str(temp_cur_int).zfill(3)

        next_vernum = ""
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                last_ver_pkg_dict   = _lyr.get("PKG_VERSION")[-1]
                last_vernum         = last_ver_pkg_dict.get("VERSION_NUM")
                next_vernum         = version_up(last_vernum)

                _lyr.get("PKG_VERSION").append({"VERSION_NUM":next_vernum, "PUBS":[]})
                break

        return next_vernum
    



    def add_pkg_version_from_previous_ver(self, selected_department :str, selected_previous_ver :str) -> str:
        def version_up(cur_vernum :str) -> str:
            temp_cur_int = int(cur_vernum.replace("v", ""))
            temp_cur_int += 1
            return "v" + str(temp_cur_int).zfill(3)
        
        def get_pubs_of_selected_version(all_pkg_list :list, vernum :str) -> list:
            for pkg_info in all_pkg_list:
                if pkg_info.get('VERSION_NUM') == vernum:
                    return pkg_info.get('PUBS')
                
            return []

        next_vernum = ""
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                last_ver_pkg_dict   = _lyr.get("PKG_VERSION")[-1]
                last_vernum         = last_ver_pkg_dict.get("VERSION_NUM")
                next_vernum         = version_up(last_vernum)

                selected_pkg_pubs       = get_pubs_of_selected_version(_lyr.get("PKG_VERSION"), selected_previous_ver)

                _lyr.get("PKG_VERSION").append({"VERSION_NUM":next_vernum, "PUBS":selected_pkg_pubs})
                break


        return next_vernum
    


    def pop_pkg_version(self, selected_department :str) -> str:
        popped_vernum = ""
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                if _lyr.get("PKG_VERSION")[-1].get("VERSION_NUM") == "v001":
                    return None
                popped_vernum = _lyr.get("PKG_VERSION").pop()
                break
        return popped_vernum

    def get_versions(self, selected_department :str):
        version_list = []
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    pkg_ver = _version.get("VERSION_NUM")
                    version_list.append(pkg_ver)
        return version_list


    def get_pubs(self, selected_department :str, selected_version :str) -> list:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        return _version.get("PUBS")
        return []
    
    def add_pubs(self, selected_department :str, selected_version :str, pub_paths :list) -> None:
        self.clear_pubs(selected_department, selected_version)
        for pub_path in pub_paths:
            if not isinstance(pub_path, str):
                pub_path  = pub_path.get_full_path()
            self.add_pub(selected_department, selected_version, pub_path)

    def add_pub(self, selected_department :str, selected_version :str, pub_path :str) -> None:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        if pub_path in _version.get("PUBS"):
                            continue
                        _version.get("PUBS").append(pub_path)

    def remove_pub(self, selected_department :str, selected_version :str, pub_path :str) -> str:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        if pub_path in _version.get("PUBS"):
                            _version.get("PUBS").remove(pub_path)

    def clear_pubs(self, selected_department :str, selected_version :str) -> None:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        _version["PUBS"] = []

    def add_versions(self, selected_department :str, selected_version :str, input_text :str) -> None:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        _version["VERSIONS"] = input_text

    def add_progress(self, selected_department :str, selected_version :str, input_text :str) -> None:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        _version["PROGRESS"] = input_text

    def add_note(self, selected_department :str, selected_version :str, input_text :str) -> None:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        _version["DESCRIPTION"] = input_text


    def get_pkg_infos(self, selected_department :str, selected_version :str) -> None:
        pkg_versions_path = None
        pkg_progress      = None
        pkg_note          = None
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        pkg_versions_path   = _version.get("VERSIONS")
                        pkg_progress        = _version.get("PROGRESS")
                        pkg_note            = _version.get("DESCRIPTION")
        if pkg_versions_path == None:
            pkg_versions_path = ""
        if pkg_progress == None:
            pkg_progress = "0"
        if pkg_note == None:
            pkg_note = ""
        return pkg_versions_path, pkg_progress.replace("%", ""), pkg_note



    def add_pkg_status(self, selected_department :str, selected_version :str, status_type :str, path_status_list :list) -> None:
        for _lyr in self.layer_list:
            if _lyr.get("DEPARTMENT") == selected_department:
                for _version in _lyr.get("PKG_VERSION"):
                    if _version.get("VERSION_NUM") == selected_version:
                        _version[status_type] = path_status_list
                        # pprint()

    def to_view_dict(self) -> list:
        all_layer_and_versions = []
        if self.info != {}:
            for _lyr in self.layer_list:
                department = _lyr.get("DEPARTMENT")
                for _vers in _lyr.get("PKG_VERSION"):
                    vernum = _vers.get("VERSION_NUM")
                    pub_list = _vers.get("PUBS")
                    all_layer_and_versions.append(
                                                    {
                                                        "VIEW_DEPARTMENT"  : department,
                                                        "VIEW_PKG_VERSION" : vernum,
                                                        "VIEW_PUBS"        : pub_list 
                                                    }
                    )
        return all_layer_and_versions