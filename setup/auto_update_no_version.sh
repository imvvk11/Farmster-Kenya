#!/usr/bin/env bash

cd $(dirname ${BASH_SOURCE})

echo "Are you sure you want to update?"
read -rsp $'Press any key to continue...\n' -n1 key

echo "updating code"
git checkout auto_update.sh
git checkout auto_update_no_version.sh
git pull
sudo chmod +x auto_update.sh
sudo chmod +x auto_update_no_version.sh

cd ..

echo "updating python libs"
workon farmster-venv
pip install -r requirements.txt
deactivate

echo "give permissions to log folder"
sudo chmod -R 777 logs/

echo "running migrate"
./manage.py migrate

echo "compile translations"
django-admin compilemessages

sudo systemctl restart uwsgi
sudo systemctl restart nginx

echo "Update finished!"
