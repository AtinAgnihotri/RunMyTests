import pathlib
import os
import sys
from pathlib import Path
import subprocess
# abc = (pathlib.Path().absolute())
# print(abc / 'gcloud' / 'init')
try:
    sdk_path = (os.environ['ANDROID_HOME'])
except KeyError:
    print('ANDROID_HOME not set up. Please do so to use RunMyTests')
    sys.exit(-1)

if ';' in sdk_path:
    sdk_path_split = sdk_path.split(';')
    for each_split in sdk_path_split:
        each_path = Path(each_split)
        if each_path.is_dir():
            each_subdirs_list = [str(each.stem) for each in each_path.iterdir()]
            # print(each_subdirs_list)
            build_tools_present = 'build-tools' in each_subdirs_list
            platform_tools_present = 'platform-tools' in each_subdirs_list
            tools_present = 'tools' in each_subdirs_list
            if build_tools_present and platform_tools_present and tools_present:
                sdk_path = each_split
                break
            else:
                print('Nope')

lst1 = ['.downloadIntermediates', '.knownPackages', '.temp', 'build-tools', 'emulator', 'emulator', 'extras', 'fonts', 'licenses', 'ndk', 'patcher', 'platform-tools', 'platforms', 'skiaparser', 'skins', 'sources', 'system-images', 'tools']
lst2 = ['build-tools', 'platform-tools', 'tools']

print(lst2 in lst1)

if __name__ == '__main__':
    path = str(Path(sdk_path) / 'tools' / 'bin' / 'avdmanager')
    print(path)
    subprocess.call(path + ' list avd', shell=True)
