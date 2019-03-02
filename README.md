clone the project

git clone 

Create Virtual Environment Using Below command

virtualenv env

activate the evironment 

source env/bina activate

install packeges

pip install -r requirement.txt

cd django_assignment

create super user for accessing admin dashboard

python manage.py createsuperuser

makemigrations to create the neccessary table

python manage.py makemigrations
python manage.py migrate

Run the server

python manage.py runserver


Api list avaliable at 

http://{{Base url}}/api/task/list

Deatail View 

http://{{Base url}}/api/taskview/{{pk}}

Application at Base url

http://{{ Base url }}

Admin Dashboard available at

http://{{ Base url }}/admin

