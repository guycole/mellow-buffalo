#! /usr/bin/python
#
# Title:mb_import_sorter.py
# Description:sort raw mellow/import files
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import os
import sys
import time
import yaml

class SortDriver:

    def sorting_hat(self, directories, full_path):
        destination_directory = ''

        with open(full_path, "r") as infile:
            try:
                parsed = json.load(infile)
                print(parsed)
                if 'project' in parsed:
                    target = parsed['project']

                    if target == 'elephant':
                        destination_directory = directories['elephantDir']
                    elif target == 'hound':
                        destination_directory = directories['houndDir']
                    else:
                        print(f"missing target:{target}")
                else:
                    print(f"missing project in:{full_path}")
            except Exception as exception:
                print(exception)

        if len(destination_directory) > 0:
            command = f"mv {full_path} {destination_directory}"
            print(command)
#            os.system(command)

    def execute(self, directories):
        start_time = time.time()

        source_directory = directories['srcDir']

        candidates = os.listdir(source_directory)

        for candidate in candidates:
            full_path = f"{source_directory}/{candidate}"
            if os.path.isfile(full_path):
                self.sorting_hat(directories, full_path)

        stop_time = time.time()
        duration = stop_time - start_time

        return duration

print('start')

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        yaml_file_name = sys.argv[1]
    else:
        yaml_file_name = 'config.yaml'

    directories = {}

    with open(yaml_file_name, 'r') as stream:
        try:
            configuration = yaml.load(stream, Loader=yaml.FullLoader)
            directories['srcDir'] = configuration['srcDir']
            directories['elephantDir'] = configuration['elephantDir']
            directories['houndDir'] = configuration['houndDir']
        except yaml.YAMLError as exception:
            print(exception)

    driver = SortDriver()
    duration = driver.execute(directories)

    print(f"SortDriver end w/duration:{duration}")

print('stop')
