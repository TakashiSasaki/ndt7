#!/bin/sh

CLIENT_BIN=/root/go/bin/ndt7-client
CLIENT_OPT="--format json"
FILENAME=`date --iso-8601=minute`.json

${CLIENT_BIN} ${CLIENT_OPT} > ${FILENAME}
cp ${FILENAME} latest.json

