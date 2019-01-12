# Web_Application_Priya
# This is my first web application using django
Note : This is built  on Django 1.11 version



Run Instructions
------------------
steps to running the project by other users :

Clone the project

git clone https://github.com/priyarao1995/Web_Application_Priya.git


#Install virtualenvironment 
Activate virtual environment

. venv/bin/activate

#Testing
Install the project dependencies:

pip install -r requirements.txt  (ignore other errors regarding matching distributions for other packages, Django and six are mandatory)

#Make sure you are in the folder that contains manage.py

#run the server
python manage.py runserver

#Need not run migrations as i already applied them. If asked , run python manage.py migrate and re run the server

You can create admin account by using 

  python manage.py createsuperuser

I have created four users according to the access levels and following are the login credentials

ORGANIZATION:- username: organization
               password: user11111
SUPERADMIN:-   username: super_admin
               password: user22222
PROCESS_ADMIN:-username: process_admin
               password: user33333
USER :-        username: user
               password: user44444              

#Open localhost:8000 on your browser to view the app , Login using the login link 


## Errors:

 As Sqlite3 database is used here
 
 If error: No module named _sqlite3
 
 Use :
  sudo apt-get install libsqlite3-dev libsqlite3
  
 
## Thank you  ##

    

