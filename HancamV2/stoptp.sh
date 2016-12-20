#! /bin/bash

PID=$(ps aux | grep -v grep | grep "/home/seydou/Hanicam/FACE_KNOWN/take_tof.py" | awk '{print $2}')
echo "killing $PID"
kill -9 $PID
