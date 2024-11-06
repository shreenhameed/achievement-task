###  Create a Virtual Environment

Set up a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate

### Install the requirements

pip install -r requirements.txt

### Run project
python manage.py runserver

### Open in browser to see the admin panel and the achievements and milestones
http://127.0.0.1:8000/admin/

### Login
Username : admin
Password : admin#123

### Add users achievements milestones and update the milestones orders
http://127.0.0.1:8000/achievements/add/
