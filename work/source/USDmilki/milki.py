from importlib import reload
from . import milki_controller
reload (milki_controller)


import traceback

def main(app_name):
    try:
        m_controller = milki_controller.MilkiController(app_name)
        m_controller.start_view()
        m_controller.setting_items()
    except:
        traceback.print_exc()
