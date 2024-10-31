import sys
import shutil
import os

PWD = os.path.abspath(os.path.dirname(__file__))


def get_python_version():
    return str(sys.version_info.major) + '-' + str(sys.version_info.minor)


def flood_here(source_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file = os.path.join(root, file)

            relative_path = os.path.relpath(root, source_folder)
            destination_folder = os.path.join(PWD, relative_path)
            destination_file_path = os.path.join(destination_folder, file)

            if destination_file_path.endswith('.py'):
                destination_file_path += 'c'

            os.makedirs(destination_folder, exist_ok=True)
            shutil.copy(source_file, destination_file_path)


flood_here(f'{PWD}/_CB/wizard{get_python_version()}')

from . import second_init

for thing in dir(second_init):
    globals()[thing] = getattr(second_init, thing)
