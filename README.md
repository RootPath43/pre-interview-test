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
    Category type performance
    
    ![categoryperformance1](https://github.com/user-attachments/assets/ad2e2080-fb7c-4852-8d4c-17d5af5f996f)
    ![categoryperformance2](https://github.com/user-attachments/assets/6d2c58b3-7c34-42b2-ba41-af632f32223c)
    ![categoryperformance3](https://github.com/user-attachments/assets/5146381a-988e-44a7-9c40-63040d41433b)

    Status Distrubition
    
    ![Screenshot from 2024-08-22 22-39-22](https://github.com/user-attachments/assets/f3076d23-a36c-4ad1-b133-6862b1c3958c)
    
    ![Screenshot from 2024-08-22 22-39-27](https://github.com/user-attachments/assets/35f62c3a-c743-4414-beb3-3afdff785531)

    Conversion Rate
    
    ![Screenshot from 2024-08-22 22-38-14](https://github.com/user-attachments/assets/91a37d80-6904-4258-9ad9-04f028a331b4)

    Filtered Aggregation

    ![Screenshot from 2024-08-22 22-06-24](https://github.com/user-attachments/assets/3eacb030-b9ca-4086-b9d8-2e9f9d5df412)

    ![Screenshot from 2024-08-22 22-06-28](https://github.com/user-attachments/assets/ff69c3b1-d9ba-4d3f-82d1-157361edf195)


    






# Detailed Explanation:

    With Singleton Design pattern, only once reading the csv file,
    You can check that in /endpoint/calculations/calculations.py

    Creating deep copy of dataframe for every single method.


    
