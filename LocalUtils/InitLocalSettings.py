'''
Initialises Local Settings in the Project folder
'''
from GlobalUtils import CreateSettingsYaml

class InitLocalSettings:
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_classes(self):
        self.yaml_writer = CreateSettingsYaml.CreateSettingsYaml()

    def __initialise_variables(self):
        self.__proj_path = '' # TODO Get Current Project Path

    def __build_base_local_dict(self):
        local_dict = {}
        return local_dict

    def init_gcloud_settings(self):
        self.yaml_writer.create_yaml(self.__proj_path, self.__build_base_local_dict())