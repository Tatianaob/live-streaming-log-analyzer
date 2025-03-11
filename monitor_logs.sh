#!/bin/bash

LOG_FILE="streaming_logs.txt"

echo "📡 Monitoring log file for issues..."
tail -f $LOG_FILE | while read LINE
do
    if echo "$LINE" | grep -E "ERROR|WARNING"; then
        echo "🚨 Alert: Issue detected! $LINE"
    fi
done

