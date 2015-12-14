# HelpingHands1.9

To start the server:

- create a directory for a virtual environment after installing virtualenv. In my case, I had to do

`virtualenv swe_env_1.9`

- cd into the folder of the environment and clone this repo.

- call 

`source bin/activate`

and then install django (the default version that will install is 1.9)

After these steps, you can cd into helping_hands and see if you can

`python manage.py migrate`

and then

`python manage.py runserver`

If you aren't able to run these commands, you should at least get a pretty informative error message. 1.9 is nice that way.
