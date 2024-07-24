#!/bin/bash
# This script runs a command for 12 hours with start and end time of the command
# The command to run is stored in a variable called cmd
cmd="<write the command>"

now=$(date +%s)
end=$((now + 12 * 3600))
echo "The script will run from $(date -d @$now) to $(date -d @$end)"
while [ $(date +%s) -lt $end ]; do
 log_file=logs_$(date +"%H%M%S")
 $cmd >> $log_file
 count_error=$(grep -c ERROR $log_file)
 if [ "$count_error" -ge 1 ]; then
 echo "ERROR found in $log_file"
                exit;
        else
        echo "No ERROR found in $log_file"
        fi
 sleep 1h
done
echo "The script has finished running"
