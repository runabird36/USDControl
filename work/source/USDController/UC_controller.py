
from importlib import reload
import sys
from PySide2.QtWidgets import (
                                    QWidget, QVBoxLayout, QGridLayout,
                                    QPushButton, QMainWindow, QDesktopWidget
                            )
from PySide2.QtCore import (QEvent, QObject)

from maya_md import hgweaverUSD
reload(hgweaverUSD)

from qt_material import apply_stylesheet
from functools import partial


def _maya_main_window():
   '''
   Get the maya main window as a QMainWindow instance
   '''
   import maya.cmds as cmds
   import maya.OpenMayaUI as mui
   from shiboken2 import wrapInstance
   ptr = mui.MQtUtil.mainWindow()
   if ptr is not None:
        return wrapInstance(int(ptr),QWidget)



class Main(QMainWindow):
    def __init__(self, _parent :object=None) -> None:
        super(Main, self).__init__(_parent)
        
        self.setupUi()
        
    def setupUi(self) -> None:
        def move_center(main_win):
            qr = main_win.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            main_win.move(qr.topLeft())
        
        
        self.save_btn           = QPushButton("Save")
        self.add_payload_btn    = QPushButton("Add by Payload")
        self.load_btn           = QPushButton("Load Prim")
        self.unload_btn         = QPushButton("Unload Prim")
        
        self.save_btn.clicked.connect(partial(self.cliked_control, self.save_btn.text()))
        self.add_payload_btn.clicked.connect(partial(self.cliked_control, self.add_payload_btn.text()))
        self.load_btn.clicked.connect(partial(self.cliked_control, self.load_btn.text()))
        self.unload_btn.clicked.connect(partial(self.cliked_control, self.unload_btn.text()))
        
        
        self.main_gl = QGridLayout()
        self.main_gl.addWidget(self.save_btn, 0, 0)
        self.main_gl.addWidget(self.add_payload_btn, 0, 1)
        self.main_gl.addWidget(self.load_btn, 1, 0)
        self.main_gl.addWidget(self.unload_btn, 1, 1)
        
        
        self.dummy_wg = QWidget()
        self.dummy_wg.setLayout(self.main_gl)
        self.setCentralWidget(self.dummy_wg)
        
        apply_stylesheet(self, "dark_cyan.xml")
        move_center(self)
        
        
    
    def cliked_control(self, btn_text :str) -> None:
        if btn_text == self.save_btn.text():
            tar_stage = hgweaverUSD.save_stage_from_selection()
            tar_stage.Save()
            print(f"Info : Save Stage {tar_stage}", file=sys.stdout)
        elif btn_text == self.add_payload_btn.text():
            pass
        elif btn_text == self.load_btn.text():
            pass
        elif btn_text == self.unload_btn.text():
            pass
        
    
if __name__ == "__main__":
    _engine = Main(_maya_main_window())
    _engine.show()