'''
Help Module for the tool
'''
class Help:
    def __init__(self):
        pass

    def print_help(self):
        print('Printing Help')

    def __error_resolver(self, err_code):
        # TODO build a better error resolver
        if err_code == '001':
            return 'ERR 001 :: INVALID RUN CONFIGURATION'


    def error_handler(self, err_code):
        # TODO find a way to index error codes
        # TODO For now 001 is Invalid Run Configuration
        err_str = self.__error_resolver(err_code)
        print(err_str)
        self.print_help()