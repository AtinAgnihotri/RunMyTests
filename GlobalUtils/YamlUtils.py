'''
Creates a Settings YAML file at the give location with the give keywords
'''
import yaml

class YamlUtils:
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_classes(self):
        pass

    def __initialise_variables(self):
        pass

    def create_yaml(self, path, yaml_dict):
        with open(path, 'w') as file:
            yaml.dump(yaml_dict, file)

    def load_yaml(self, path):
        loaded_dict = {}
        with open(path, 'r') as file:
            loaded_dict = yaml.load(file, Loader=yaml.FullLoader)
        return loaded_dict