

from general_md_3x import LUCY
from importlib import reload
from re import search
from socket import gethostname

class ItemSupply():
    item_dic = {}
    m_sg_tk = None
    p_dialog = None
    def __init__(self, m_sg_tk, progress_dialog, app_name):
        self.m_sg_tk = m_sg_tk
        self.p_dialog = progress_dialog
        self._IS_SHOT_MDL = False
        self.app_name = app_name


    def get_items(self, part):

        entity = LUCY.get_category()

        if part == 'modeling' and entity =='sequence':
            self._IS_SHOT_MDL = True


        if part == 'modeling' and self._IS_SHOT_MDL == False:
            from ..selectors.target_selector import TargetSelector

            from ..checkers.name_checker import NameChekcer
            
            from ..checkers.history_checker import HistoryChekcer

            from ..checkers.freeze_checker import FreezeChecker

            from ..selectors.freeze_selector import FreezeSelector

            from ..checkers.uvSet_checker import UVsetChecker

            from ..selectors.mdl_selector import MdlSelector

            from ..exporters.mdl_exporter_03 import MdlExporter

            return [TargetSelector(), FreezeSelector(), HistoryChekcer(), NameChekcer(), FreezeChecker(), UVsetChecker(), MdlSelector(), MdlExporter(self.m_sg_tk, self.p_dialog)]
            
            
        elif part == "shotsculpt" or (part == 'modeling' and self._IS_SHOT_MDL == True):
            from ..selectors.target_selector import TargetSelector

            from ..selectors.shotMDL_selector import ShotMDLSelector
            shot_mdl_option_selector = ShotMDLSelector()
            shot_mdl_option_selector.refresh()
            
            from ..exporters.anim_exporter import AnimExporter
            
            return [TargetSelector(), shot_mdl_option_selector, AnimExporter(self.m_sg_tk, self.p_dialog)]



        elif part == 'lookdev':
            from ..selectors.target_selector import TargetSelector

            from ..checkers.geo_checker import GeoChecker

            from ..selectors.ldv_selector import LdvSelector

            from ..checkers.node_name_checker import NodeNameChecker

            from ..exporters.ldv_exporter import LdvExporter
            
            return [TargetSelector(), LdvSelector(), LdvExporter(self.m_sg_tk, self.p_dialog)]

        elif part == 'rigging':
            from ..selectors.target_selector import TargetSelector

            from ..exporters.rig_exporter import RigExporter
            
            return [TargetSelector(), RigExporter(self.m_sg_tk, self.p_dialog)]

        elif part in ['cloth'] and entity =='sequence':
            from ..selectors.target_selector import TargetSelector

            from ..checkers.frame_range_checker import FrameRangeChecker

            from ..selectors.anim_selector import AnimSelector

            from ..exporters.anim_exporter import AnimExporter
            ani_option_selector = AnimSelector()
            ani_option_selector.refresh()
            
            return [TargetSelector(), FrameRangeChecker(self.m_sg_tk), ani_option_selector, AnimExporter(self.m_sg_tk, self.p_dialog)]

        elif part in ['cloth'] and entity != 'sequence':
            from ..selectors.target_selector import TargetSelector
            
            from ..exporters.rig_exporter import RigExporter

            return [TargetSelector(), RigExporter(self.m_sg_tk, self.p_dialog)]

        elif part in ['layout', 'animation', 'matchmove', 'previz', 'cloth']:
            from ..selectors.target_selector import TargetSelector
            
            from ..checkers.ani_ns_latest_checker import ANINsLatestChekcer

            from ..checkers.frame_range_checker import FrameRangeChecker

            from ..selectors.anim_selector_v03 import AnimSelector
            
            from ..exporters.anim_exporter_v03 import AnimExporter
            ani_option_selector = AnimSelector()
            ani_option_selector.refresh()
            
            if part == 'animation' and LUCY.get_category() == 'asset':
                from ..exporters.rig_exporter import RigExporter

                return [TargetSelector(), RigExporter(self.m_sg_tk, self.p_dialog)]

            elif part == "animation":
                return [TargetSelector(),  ANINsLatestChekcer(), FrameRangeChecker(self.m_sg_tk), ani_option_selector, AnimExporter(self.m_sg_tk, self.p_dialog)]
            else:
                return [TargetSelector(),  FrameRangeChecker(self.m_sg_tk),ani_option_selector, AnimExporter(self.m_sg_tk, self.p_dialog)]

        elif part in ['lighting']:
            from ..selectors.target_selector import TargetSelector

            from ..checkers.lgt_name_checker import LGTNameChecker
            
            from ..exporters.lgt_exporter_02 import LgtExporter
            
            return [TargetSelector(), LGTNameChecker(), LgtExporter(self.m_sg_tk, self.p_dialog)]

        elif part in ['characterfx', 'hair']:
            if search("set", LUCY.get_task()):
                from ..selectors.target_selector import TargetSelector

                from ..exporters.hairSet_exporter import HairSetExporter
                
                return [TargetSelector(), HairSetExporter(self.m_sg_tk, self.p_dialog)]
            else:
                from ..selectors.target_selector import TargetSelector

                from ..checkers.cfx_geo_checker import CFXGeoChecker
                
                from ..checkers.cfx_tex_checker import CFXTexChekcer
                
                from ..checkers.cfx_name_checker import CFXNameChekcer
            
                from ..selectors.hair_selector import HairSelector

                from ..exporters.cfx_exporter import CFXExporter
                
                return [TargetSelector(), CFXNameChekcer(), CFXTexChekcer(), HairSelector(), CFXExporter(self.m_sg_tk, self.p_dialog)]

        elif part in ['simulation']:
        
            from ..selectors.target_selector import TargetSelector

            from ..checkers.frame_range_checker import FrameRangeChecker
            
            from ..selectors.anim_selector_v03 import AnimSelector
            
            from ..exporters.anim_exporter_v03 import AnimExporter        
            ani_option_selector = AnimSelector()
            ani_option_selector.refresh()

            return [TargetSelector(), FrameRangeChecker(self.m_sg_tk), ani_option_selector, AnimExporter(self.m_sg_tk, self.p_dialog)]
        
        else:
            return []
