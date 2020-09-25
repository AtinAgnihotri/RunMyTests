'''
Initialises Local Settings in the Project folder
'''
from GlobalUtils import YamlUtils
import os
import shutil
import sys
from pathlib import Path
import re

class InitLocalSettings:
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_classes(self):
        self.__yaml_writer = YamlUtils.YamlUtils()

    def __initialise_variables(self):
        self.__proj_path = '' # TODO Get Current Project Path

    def __build_base_local_dict(self):
        local_dict = {}
        return local_dict

    def __get_sdk_tools(self):
        try:
            sdk_path = (self.__retrive_sdk_path_from_multiple_paths(
                os.environ['ANDROID_HOME']
            ))
        except KeyError:
            print('ANDROID_HOME not set up. Please do so to use RunMyTests')
            sys.exit(-1)

        return sdk_path

    def __retrive_sdk_path_from_multiple_paths(self, sdk_path):
        if ';' in sdk_path:
            sdk_path_split = sdk_path.split(';')
            for each_split in sdk_path_split:
                each_path = Path(each_split)
                if each_path.is_dir():
                    each_subdirs_list = [str(each.stem) for each in each_path.iterdir()]
                    build_tools_present = 'build-tools' in each_subdirs_list
                    platform_tools_present = 'platform-tools' in each_subdirs_list
                    tools_present = 'tools' in each_subdirs_list
                    if build_tools_present and platform_tools_present and tools_present:
                        sdk_path = each_split
                        break
        return sdk_path

    def __create_new_avd(self):
        pass

    def __check_for_avd(self):
        yes_condition = False
        no_condition = False
        while not (yes_condition or no_condition):
            gcloud_init = input('Have you created avd for your emulator? Would you\n'
                                'like to do so right now?your gcloud ([Y]es/[N]o):')
            yes_condition = True if (gcloud_init.lower() == 'y') or (gcloud_init.lower() == 'yes') else False
            no_condition = True if (gcloud_init.lower() == 'n') or (gcloud_init.lower() == 'no') else False

        if yes_condition:
            avd_name = input('Name of AVD:')
            correct_sdk_id = False
            while not correct_sdk_id:
                sdk_id = input('Android SDK Version:')
                if re.search(r'\d{2}', sdk_id):
                    pass
            # TODO
            avd_man_cmd = 'avdmanager create avd -n ' + avd_name + ' -k "system-images'




    def init_local_settings(self, proj_path):
        self.__yaml_writer.create_yaml(proj_path / 'Configurations' / 'Local.yml',
                                       self.__build_base_local_dict())