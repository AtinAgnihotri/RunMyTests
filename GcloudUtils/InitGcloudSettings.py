'''
Initialises Gcloud Settings in the Project folder
'''
from GlobalUtils import YamlUtils
import subprocess

class InitGcloudSettings:
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_classes(self):
        self.yaml_writer = YamlUtils.YamlUtils()

    def __initialise_variables(self):
        self.__proj_path = '' # TODO Get Current Project Path

    def __build_base_gcloud_dict(self):
        gcloud_dict = {}
        gcloud_dict['Type'] = 'instrumentation # (instrumentation/robo)'
        gcloud_dict['App'] = ' # Put App Path/ App Dir Path Here'
        gcloud_dict['Test_App'] = ' # Put Test App Path/ Test App Dir Path Here'
        gcloud_dict['Devices'] = [' # Put Device Info Here', ' # For Example ',
                                  'model=Nexus6, version=21, locale=en, orientation=potrait']
        gcloud_dict['ENV_VARS'] = 'False # (True/False)'
        gcloud_dict['ENV_VAR_ARGS'] = 'coverage=true,coverageFile="/sdcard/coverage.ec" # Put Env Var Args here'
        gcloud_dict['PULL_DIRS'] = 'False # (True/False)'
        gcloud_dict['DIRS_TO_PULL'] = '/sdcard # Put dirs to pull here'
        return gcloud_dict

    def __init_gcloud_cli(self):
        '''
        (Re)Initialise GCloud CLI based on user input
        :return: None
        '''
        yes_condition = False
        no_condition = False
        while not (yes_condition or no_condition):
            gcloud_init = input('Have you initialised this project in your \n'
                  'gcloud cli? Would you like to (re)initialise\n'
                  'your gcloud ([Y]es/[N]o):')
            yes_condition = True if (gcloud_init.lower() == 'y') or (gcloud_init.lower() == 'yes') else False
            no_condition = True if (gcloud_init.lower() == 'n') or (gcloud_init.lower() == 'no') else False

        if yes_condition:
            subprocess.call('gcloud init', shell=True)

    def init_gcloud_settings(self, proj_path):
        self.__init_gcloud_cli()
        self.yaml_writer.create_yaml(proj_path / 'Configurations' / 'Gcloud.yml',
                                     self.__build_base_gcloud_dict())