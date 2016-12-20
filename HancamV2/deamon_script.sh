#! /bin/bash
set -xv
can="oui"
while true
do
	while read line  
	do   
	   echo "Read : $line"
   	if [ $line == "on" ]
   	then
   		if [ $can == "oui" ]
   		then
   		   python /home/seydou/Hanicam/FACE_KNOWN/example1.py &
   		   can="non"
   		fi
   		echo "On Find"
   	elif [ $line == "off" ]
   	then 
   		echo "Off Find"
   		PID=$(ps aux | grep -v grep | grep "/home/seydou/Hanicam/FACE_KNOWN/example1.py" | awk '{print $2}')
			echo "killing $PID"
			kill -9 $PID
			can="oui"
   	fi	 
	done < ressources/jeton.txt
done
