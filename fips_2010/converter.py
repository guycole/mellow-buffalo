#! /usr/bin/python
#
# Title:converter.py
# Description: import FIPS into mysql
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#

in_file = open('national_county.txt', 'r')
raw_buffer = in_file.readlines()
in_file.close()

for raw_line in raw_buffer:
	tokens = raw_line.split(',')
	postal_code = tokens[0].strip()
	state_fips = tokens[1].strip()
	county_fips = tokens[2].strip()
	county_name = tokens[3].strip()
	fips_class = tokens[4].strip()

	print "insert into fips_2010(state_postal, state_fips, county_fips, county_name, class_code) values(\"%s, %s, %s, %s, %s\");" % (postal_code, state_fips, county_fips, county_name, fips_class)
