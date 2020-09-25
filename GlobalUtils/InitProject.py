'''
Initialises a RunMyTest project
'''
# from importlib import reload
# import LocalUtils
# import GcloudUtils
# reload(LocalUtils)
# reload(GcloudUtils)
from LocalUtils import InitLocalSettings
from GcloudUtils import InitGcloudSettings
from pathlib import Path



class InitialiseProject:
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_classes(self):
        self.__local_init = InitLocalSettings.InitLocalSettings()
        self.__gcloud_init = InitGcloudSettings.InitGcloudSettings()

    def __initialise_variables(self):
        self.__proj_path = (Path().absolute()  / 'RunMyTests').replace('\\','/')

    def __create_settings_folder(self):
        Path(self.__proj_path).mkdir(parents=True, exist_ok=True)

    def init_project(self):
        self.__create_settings_folder()
        self.__local_init.init_local_settings(self.__proj_path)
        self.__gcloud_init.init_gcloud_settings(self.__proj_path)

    def get_project_path(self):
        proj_path = ''
        # TODO get project path
        return proj_path
