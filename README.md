Runtime requirements/dependencies installed -

ALl the packages are mentioned in lawpilots-project/backend/requirements.txt file

Steps to start the project - 

source lawvenv/bin/activate
python3 manage.py makemigrations
python3 manage.py runserver


How it works - 

@GET API
Endpoint: get_data/
Output: Hostname is surfer-172-30-10-168-hotspot.internet-for-guests.com Current date and time is 2022-01-28 07:26:00.548052 and Uptime is None

To check logging, one has to log in to the Django admin
http:localhost:8000/admin
panel. 
To create credentials for it, run the below command - 

python3 manage.py createsuperuser
And enter the username, mail address and password.

Use these credentials to log in to the admin panel to see the Logging database created. An extra parameter with hostname has been added to the existing logging parameters.

