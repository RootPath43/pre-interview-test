# pre-interview-test
# Installation:
    You choose either to run it with docker or to create virtualenv by own.

    If you want to run the code with docker:
    
    Create docker image 

    $ docker image build -t interview:0.0.1 .

    Then run:

    $ docker container run -p 8000:8000 -d interview:0.0.1

    If you want to create virtualenv:

    Create virtualenv python 3.8

    $ virtualenv --path="python3.8 path"  venv

    Activate virtualenv

    $ source venv/bin/activate

    Install dependencies

    $ pip install requirements.txt

    Then run:
    
    gunicorn --bind 0.0.0.0:8000 interview.wsgi:application


# API Responses:



# Detailed Explanation:

    With Singleton Design pattern, only once reading the csv file,
    You can check that in /endpoint/calculations/calculations.py

    Creating deep copy of dataframe for every single method.


    