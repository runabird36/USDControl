
from PyQt5.QtWidgets import (
                                QApplication, QDialog, QHBoxLayout, QVBoxLayout,
                                QLabel, QPushButton, QCheckBox, QFrame, QSpacerItem,
                                QSizePolicy, QRadioButton, QButtonGroup, QMessageBox
                            )
from PyQt5.QtCore import Qt

from functools import partial
from qt_material import apply_stylesheet
from traceback import print_exc


class TypeChoiceDialog(QDialog):
    def __init__(self, _parent=None) -> None:
        super(TypeChoiceDialog, self).__init__(_parent)

        self.selected_type = ""


        self.setupUi()

    def setupUi(self) -> None:
        
        self.title_lb = QLabel("Category 선택")
        self.title_lb.setStyleSheet(f'''
                                        QLabel{{
                                               font             : 20px;
                                               font-weight      : bold;
                                        }}
                                    ''')
        self.desc_lb = QLabel()
        self.desc_lb.setText("USD weaver 로 edit할 category를 선택해주십시오")
        self.desc_lb.setStyleSheet(f'''
                                        QLabel{{
                                               font             : 13px;
                                        }}
                                    ''')

        self.check_type_title       = QLabel("Category")
        self.check_type_title.setStyleSheet(f'''
                                        QLabel{{
                                               font             : 15px;
                                               font-weight      : bold;
                                        }}
                                    ''')
        self.check_split_line_fm    = QFrame()
        self.check_split_line_fm.setFrameShape(QFrame.HLine)
        self.asset_rb               = QRadioButton("Asset")
        self.shot_rb                = QRadioButton("Shot")

        self.btn_groups             = QButtonGroup()
        self.btn_groups.addButton(self.asset_rb)
        self.btn_groups.addButton(self.shot_rb)
        self.btn_groups.buttonClicked.connect(self.set_choice)
        

        checkbox_margin = 40
        self.check_vl = QVBoxLayout()
        self.check_vl.addWidget(self.check_type_title)
        self.check_vl.addWidget(self.check_split_line_fm)
        self.check_vl.addWidget(self.asset_rb)
        self.check_vl.addWidget(self.shot_rb)
        self.check_vl.setContentsMargins(10,checkbox_margin,0,0)

        self.main_v_spacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.btn_h_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.select_btn   = QPushButton("선택")
        self.cancel_btn   = QPushButton("닫기")
        self.select_btn.clicked.connect(partial(self.make_decision, "선택"))
        self.cancel_btn.clicked.connect(partial(self.make_decision, "닫기"))

        self.btn_hl      = QHBoxLayout()
        self.btn_hl.addItem(self.btn_h_spacer)
        self.btn_hl.addWidget(self.select_btn)
        self.btn_hl.addWidget(self.cancel_btn)


        self.main_vl = QVBoxLayout()
        self.main_vl.addWidget(self.title_lb)
        self.main_vl.addWidget(self.desc_lb)
        self.main_vl.addLayout(self.check_vl)
        self.main_vl.addItem(self.main_v_spacer)
        self.main_vl.addLayout(self.btn_hl)
        


        self.setLayout(self.main_vl)
        main_margin = 15
        self.setContentsMargins(main_margin,main_margin,main_margin,main_margin)
        self.resize(500, 400)
        self.setWindowTitle("USD Weaver")

    def set_choice(self, button) -> None:
        self.selected_type = button.text()
        print(self.selected_type)


    def get_choice(self) -> str:
        return self.selected_type

    def make_decision(self, decision_type :str) -> bool:
        if decision_type == "선택":
            if self.selected_type == "":
                info_box = QMessageBox()
                info_box.setWindowTitle("안내창")
                info_box.setText("선택된 category가 없습니다. 다시 선택해주십시오")
                info_box.setStandardButtons(QMessageBox.Ok)
                info_box.exec_()
                return
            self.accept()
            
        elif decision_type == "닫기":
            self.reject()
            
        
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml')



    ui = TypeChoiceDialog()
    if ui.exec_():
        view_type = ui.get_choice()
        # if view_type == "Asset":
        #     sys.path.append("/usersetup/linux/scripts/general_sc/gweaverasset")
        #     try:
        #         from GW_controller import GPController
        #         tool = GPController()
        #         tool.run()
        #     except:
        #         print_exc()
        # elif view_type == "Shot":
        #     sys.path.append("/usersetup/linux/scripts/general_sc/GWeaver")
        #     try:
        #         from GW_controller import GPController
        #         tool = GPController()
        #         tool.run()
        #     except:
        #         print_exc()
        # else:
        #     pass


    sys.exit(app.exec_())
