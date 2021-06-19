#
# Title:database.py
# Description: mellow hound database
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import logging
import sqlite3

class DataBase:
    def __init__(self, logger_level: int):
        logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)
        self.logger = logging.getLogger()

    def create_geoloc(self, observation_file):
        self.logger.info("create geoloc db table")

        create_table = "CREATE TABLE geoloc(fix_time integer PRIMARY KEY, accuracy integer, altitude integer, latitude real, longitude real"

        connection = sqlite3.connect(observation_file)
        connection.execute(create_table)
        connection.close()

    def create_wifi(self, observation_file):
        self.logger.info("create wifi db table")

        create_table = "CREATE TABLE wifi(ssid text, bssid text, capability text, frequency integer, level text"

        connection = sqlite3.connect(observation_file)
        connection.execute(create_table)
        connection.close()

    def write_geoloc(self, geoloc:dict):
        self.logger.info("write geoloc db table")
        print(geoloc)

    def write_wifi(self, wifi:dict):
        self.logger.info("write wifi db table")
        print(wifi)

    def write_observation(self, geoloc:dict, wifi:dict):
        self.write_geoloc(geoloc)
        self.write_wifi(wifi)

    def write_observation2(self, observation_file, observations, band_ndx, sortie_key):
        # self.logger.info("write observation db table")

        connection = sqlite3.connect(observation_file)

        for observation in observations:
            strength = observation['strength']
            frequency = observation['frequency']
            modulation = observation['modulation']
            time_stamp = observation['time_stamp']
            moving_average = observation['moving_average']
            peaker = observation['peaker']

            insert = "INSERT INTO observation(sortie_key, band_ndx, strength, frequency, modulation, time_stamp, moving_average, peaker) VALUES('%s', %d, %d, %d, '%s', %d, %d, %d)" % (sortie_key, band_ndx, strength, frequency, modulation, time_stamp, moving_average, peaker)
            connection.execute(insert)

        connection.commit()
        connection.close()
