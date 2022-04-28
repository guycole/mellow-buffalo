#!/bin/bash
#
# Title:runner.sh
#
# Description: drive mellow buffalo load cycle
#
# Development Environment: OS X 10.13.6
#
# Author: G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
/mellow-buffalo/mellow_buffalo_py/mb_import_sorter.py
/mellow-buffalo/mellow_buffalo_py/mb_hound_loader.py
#