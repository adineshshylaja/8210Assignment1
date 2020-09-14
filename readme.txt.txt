Ensure that Python is already installed from python.org and Pycharm an integrated development environment is installed.
To use and setup this application, first it has to be downloaded. A new Pycharm Django Project is created after downloading the code from this github folder.
Goto the dropdown 'Code' and select open with github desktop. Answer 'Yes' when prompted to use the files from this folder for the new project.

Once the project is downloaded, open the project using Pycharm and as part of settings:
--Set up the project interpreter and 
--add and activate a new virtual environment.

In the terminal Window-

Install the required packages using the command:
   pip install -r requirements.txt


Make the migrations for the database model:
   python manage.py migrate


Create a superuser:
   python manage.py createsuperuser ##name of the superuser