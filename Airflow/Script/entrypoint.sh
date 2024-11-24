#!/bin/bash
set -e   #script exit immediately if any command fails
 
if [ -e "/opt/airflow/requirements.txt" ]; then
  $(command python) pip install --upgrade pip
  $(command -v pip) install --user -r requirements.txt
fi
 
if [ ! -f "/opt/airflow/airflow.db" ]; then
  airflow db init && \
  airflow users create \
    --username TiphaineGodet \
    --firstname Tiphaine \
    --lastname Godet \
    --role Admin \
    --email tiphaine.godet@supdevinci-edu.fr \
    --password iMjCwYJ74F5rh23c
fi
 
$(command -v airflow) db upgrade
 
exec airflow webserver  #start command for airflow webserver