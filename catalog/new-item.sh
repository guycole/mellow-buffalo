#!/bin/bash
#
# Title: new-item.sh
# Description: 
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
UUID=$(uuidgen)
UUID_LC=$(echo "$UUID" | tr '[:upper:]' '[:lower:]')
FILE_NAME="${UUID_LC}.json"
#
echo "start"
#cp template.json /tmp/temp.json
echo ${FILE_NAME}
cp template.json ${FILE_NAME}
sed -i "s/FIXME/${UUID_LC}/g" ${FILE_NAME}
echo "end"
#
