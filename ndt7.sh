#!/bin/sh
JSON_DIR="/mnt/Web/ndt7"
if [ ! -d ${JSON_DIR} ]; then exit 1; fi

CLIENT_BIN=/root/go/bin/ndt7-client
CLIENT_OPT="--format json"
FILENAME=`date --iso-8601=minute`.json

${CLIENT_BIN} ${CLIENT_OPT} > ${JSON_DIR}/${FILENAME}
cp ${JSON_DIR}/${FILENAME} ${JSON_DIR}/latest.json

rm -f ${JSON_DIR}/latest.jsonv
echo -n "var speed=" >>${JSON_DIR}/latest-speed.js
tail -n 1 ${JSON_DIR}/latest.json | jq -s -R . >>${JSON_DIR}/latest-speed.js
echo -n ";" >>${JSON_DIR}/latest-speed.js

echo -n "var filename=\"${FILENAME}\";" >${JSON_DIR}/latest-filename.js

