#! /bin/bash

PID=$(ps aux | grep -v grep | grep "/opt/lampp/htdocs/www/Hancam/launch.sh" | awk '{print $2}')
echo "killing $PID"
kill -9 $PID
