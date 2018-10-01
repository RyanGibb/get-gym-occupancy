#!/usr/bin/env bash
( python3 get-gym-occupancy.py "occupancy.csv" ) || { echo "`date "+%Y-%m-%dT%H:%M:%S"`" >> "occupancy.csv"; exit 1; }
echo $0 | at -M now + 1 minutes