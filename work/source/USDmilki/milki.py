
if __name__ == "__main__":
    import sys
    _path = "/usersetup/pipeline/playground/projects/2023_02_usdPipeline/work/source"
    if _path not in sys.path:
        sys.path.append(_path)
    from importlib import reload
    from USDmilki import milki_controller
    reload (milki_controller)
else:
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


if __name__ == "__main__":
    main("MAYA")