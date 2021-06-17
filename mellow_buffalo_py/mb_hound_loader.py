#! /usr/bin/python
#
# Title:mb_hound_loader.py
# Description:import mellow hound observations
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import json
import logging
import os
import sys
import time
import yaml

from database import DataBase

class HoundLoader:

    def __init__(self, logger_level, database):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

        self.logger = logging.getLogger()
        self.db = database

    def loader(self, parsed):
        print(parsed)

        project = parsed['project'] 
        version = parsed['version']

        if project == 'hound':
            if version == 1:
                geoloc = parsed['geoLoc']
                wifi = parsed['wiFi']
                self.db.write_observation(geoloc, wifi)
                return True
            else:
                print(f"ignoring bad version:{version}")
                return False
        else:
            print(f"ignoring bad project:{parsed['project']}")
            return False

    def reader(self, full_path):
        with open(full_path, "r") as infile:
            try:
                flag = self.loader(json.load(infile))
                if flag:
                    print('success')
#                    os.unlink(full_path)
                else:
                    print('failure')
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


    logging_level = logging.INFO
    logging_level = logging.DEBUG

    database = DataBase(logging_level)

    driver = HoundLoader(logging_level, database)
    duration = driver.execute(src_dir)

    print(f"HoundLoader end w/duration:{duration}")

print('stop')
