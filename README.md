# farmster-server

## Setup
The project works with python 3.7
Great!
### Create Python Virtual Environment:
https://docs.python.org/3/library/venv.html

or 

```bash
pip install virtualenv virtualenvwrapper
mkvirtualenv farmster-venv
workon farmster-venv
```

-------
### Install Local DB:
install postgress
```bash
sudo -i -u postgres
createdb farmster_dev
createuser --superuser --pwprompt farmster_admin
```

-------
### Install Dependencies:
```bash
pip install -r requirements.txt
```

-------
### Configuration:
Google could config files:
`app.yaml`
`cron.yaml`

in settings module, create a local_settings_loader.py file, with the following content:

`from .development_gcp import *` 
or
`from .development import *` to work locally

all other project settings are located in `base.py`

-------
### Perform Database Migration:
```bash
python manage.py migrate
```

-------
### Run Development Server:

```bash
python manage.py runserver
```

-------
### Deploy to gcloud:
change `local_settings_loader.py` to development_gcp (in order to migrate prod DB)
```bash
./cloud_sql_proxy -instances=farmster-ee483:us-central1:farmster-prod-db=tcp:5433
./manage.py migrate
gcloud app deploy --project=farmster-ee483
change `local_settings_loader.py` to development
[Optional] gcloud app deploy cron.yaml
[Optional] gcloud components update
```

-------
### Other:
Get more tips at `cheetsheet.txt` & `setup_prod.txt`


sudo service postgresql restart
or 
systemctl start postgresql
