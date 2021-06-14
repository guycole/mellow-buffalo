#! /usr/bin/python
#
# Title:mb_import_sorter.py
# Description:sort raw mellow/import files
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import sys
import time
import yaml

class SortDriver:

    def execute(self, destination_directory, source_directory):
        start_time = time.time()

        candidates = os.listdir(source_directory)
        for candidate in candidates:
            full_path = f"{source_directory}/{candidate}"
            if os.path.isfile(full_path):
                command = f"mv {full_path} {source_directory}"
                os.system(command)

        stop_time = time.time()
        duration = stop_time - start_time

        return duration

print('start')

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        yamlFileName = sys.argv[1]
    else:
        yamlFileName = 'config.yaml'

    with open(yamlFileName, 'r') as stream:
        try:
            configuration = yaml.load(stream, Loader=yaml.FullLoader)
            dest_dir = configuration['destDir']
            src_dir = configuration['srcDir']
        except yaml.YAMLError as exception:
            print(exception)

    driver = SortDriver()
    duration = driver.execute(dest_dir, src_dir)

    print(f"SortDriver end w/duration:{duration}")

print('stop')
