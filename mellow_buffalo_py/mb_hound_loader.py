#! /usr/bin/python
#
# Title:mb_hound_loader.py
# Description:import mellow hound observations
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import os
import sys
import time
import yaml

class HoundLoader:

    def loader(parsed):
        print(parsed)

    def reader(self, full_path):
        with open(full_path, "r") as infile:
            try:
                self.loader(json.load(infile))
            except Exception as exception:
                print(exception)

    def execute(self, source_directory):
        start_time = time.time()

        candidates = os.listdir(source_directory)

        for candidate in candidates:
            full_path = f"{source_directory}/{candidate}"
            if os.path.isfile(full_path):
                self.reader(full_path)

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

    with open(yaml_file_name, 'r') as stream:
        try:
            configuration = yaml.load(stream, Loader=yaml.FullLoader)
            src_dir = configuration['houndDir']
        except yaml.YAMLError as exception:
            print(exception)

    driver = HoundLoader()
    duration = driver.execute(src_dir)

    print(f"HoundLoader end w/duration:{duration}")

print('stop')
