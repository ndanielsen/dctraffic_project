# DC Traffic Data

Install vagrant

On commandline:

`cd into dctraffic_project`

Launch vagrant
`vagrant up`

SSH into vagrant
`vagrant ssh`

cd into project dir:
`cd dctraffic_project/`

activate virtualenv
`source venv/bin/activate`

Sync Your Database
`python manage.py makemigrations`
`python manage.py migrate`

Create superuser to log into admin
'python manage.py createsuperuser'

Run developer server
`python manage.py runserver 0.0.0.0:8000`

Load initial dataset of 10,000 rows
`python manage.py initial_load`

Checkout Admin In your local browser
`http://localhost:8000/admin/`


## Testing and Viewing Test Coverage

`py.test`
