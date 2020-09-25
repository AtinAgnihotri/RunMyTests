'''
Builds the Gcloud command to be executed
'''

class CommandBuilder(object):
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_variables(self):
        pass

    def __initialise_classes(self):
        self.__type = ''
        self.__app_path = ''
        self.__test_app_path = ''
        self.__devices = []
        self.__env_vars = []
        self.__dirs_to_pull = ''
        self.__set_env_vars = False
        self.__pull_dirs = False

    def __get_environment_variables(self):
        env_vars_str = '--environment-variables '
        # TODO put env var loop here
        return env_vars_str

    def __get_dirs_to_pull(self):
        return '--directories-to-pull ' + self.__dirs_to_pull

    def __get_devices(self):
        device_str = ''
        # TODO put devices loop here
        return device_str

    def build_command(self):
        cmd_str = 'gcloud firebase test android run \\\n'
        cmd_str += '--type ' + self.__type + '\\\n'
        cmd_str += '--app ' + self.__app_path + '\\\n'
        cmd_str += '--test ' + self.__test_app_path + '\\\n'
        cmd_str += self.__get_devices()
        if self.__env_vars:
            cmd_str += self.__get_environment_variables()
        if self.__pull_dirs:
            cmd_str += self.__get_dirs_to_pull()
        return cmd_str
