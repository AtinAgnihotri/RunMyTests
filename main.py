# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
'''
Main File of RunMyTests. 
'''
import sys
import os
from GlobalUtils import Help
from GlobalUtils import InitProject
from pathlib import Path

class Main:
    def __init__(self):
        self.__initialise_classes()
        self.__initialise_variables()

    def __initialise_classes(self):
        self.__help = Help.Help()
        self.__init_proj = InitProject.InitialiseProject()

    def __initialise_variables(self):
        pass


    def __config_actions(self, action):
        act_str = ''
        if action == 'run':
            act_str = 'Running'
        elif action == 'configure':
            act_str = 'Configuring'
        else:
            self.__help.error_handler('001') # TODO make it to 002 and resolve it in Help for Invalid Config actions
            return

        self.__action_handler(act_str, action)

    def __action_handler(self, act_str, action):
        if sys.argv[2] == 'local':
            print(act_str + ' Local Tests')
        elif sys.argv[2] == 'gcloud':
            print(act_str + ' Tests on Gcloud')
        else:
            self.__help.error_handler('001')
        self.__pull_artifiacts_handler(action)

    def __pull_artifiacts_handler(self, action):
        if len(sys.argv) > 3:
            if action == 'run' and sys.argv[3] == '--pull-artifacts':
                path_specified = False
                if len(sys.argv) > 4:
                    if Path(sys.argv[4]).is_dir():
                        print('Pulling Artifacts to ' + sys.argv[4])
                        path_specified = True
                    else:
                        print('Artifact Directory not found.')
                else:
                    print('Artifact Directory not specified')
                if not path_specified:
                    print('Pulling Artifacts to ' + self.__init_proj.get_project_path() + '/Artifacts')
            else:
                self.__help.error_handler(
                    '001')  # TODO make it to 005 and resolve it in Help for Spurious Arguments

    def main(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == 'init':
                print('Initialising project')
            elif sys.argv[1] in ['run', 'configure']:
                if len(sys.argv) > 2:
                    self.__config_actions(sys.argv[1])
                else:
                    self.__help.error_handler('001') # TODO make it to 004 and resolve it in Help for No Config Specified
            elif sys.argv[1] == 'help':
                self.__help.print_help()
            else:
                self.__help.error_handler('001') # TODO make it to 003 and resolve it in Help for Invalid Command
        else:
            self.__help.print_help()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    inst = Main()
    inst.main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
