#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

export DJANGO_SETTINGS_MODULE=src.settings

echo "<<<<<<<< Database Setup >>>>>>>>>"

python3 manage.py migrate

echo "<<<<<<<< Database Setup Successfully >>>>>>>>>>>>>>>>>>"

echo "<<<<<<<< API Streaming Starting >>>>>>>>>>>>>>>>>>"

python3 -m utilities.stream &

echo "<<<<<<<< Load Data into Database Starting >>>>>>>>>>>>>>>>>>"

python3 -m utilities.load_data &

echo "<<<<<<<< Start API >>>>>>>>>>>>>>>>>>"
python3 manage.py runserver 