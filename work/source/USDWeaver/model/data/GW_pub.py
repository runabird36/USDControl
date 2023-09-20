from dataclasses import dataclass
from USD_path_module import (is_windows, is_linux)
from re import sub
from os.path import dirname, join
@dataclass
class PubItem():
    pipe_step   :str
    file_name   :str # code
    full_path   :str
    pub_id      :str
    pub_type    :str
    created_by  :str
    date        :str
    description :str

    def get_full_path(self) -> str:
        def cur_path_os(check_path :str) -> str:
            if check_path.startswith("/") == True:
                return "linux"
            else:
                return "windows"
        
        fullpath_dir = dirname(self.full_path)
        if is_windows() == True:
            if cur_path_os(self.full_path) == "windows":
                return join(fullpath_dir, self.file_name)
            elif cur_path_os(self.full_path) == "linux":
                return "X:" + join(fullpath_dir, self.file_name)
        elif is_linux() == True:
            if cur_path_os(self.full_path) == "windows":
                return sub(r"^[a-zA-Z]\:", "", join(fullpath_dir, self.file_name))
            elif cur_path_os(self.full_path) == "linux":
                return join(fullpath_dir, self.file_name)


