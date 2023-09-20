from dataclasses import dataclass

@dataclass
class SGentity():
    entity_category :str = ""       # Asset / Shot
    entity_type     :str = ""       # Asset - character, enviroment... / Shot - sequence
    link_name       :str = ""       # asset name / shot name
    entity_id       :int = 0
    link_step       :str = ""       # pipeline step

