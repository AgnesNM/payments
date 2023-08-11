# The Payments Project
The goal of this project is to attempt to automate recurring payments that you are likely to forget about. We'll attempt to implement this using M-Pesa payments, before attempting other platforms. 

#### July 2023

## Setup/Installation Requirements

<!-- We shall use a [Product Requirements Document on Confluence](https://webscrape.atlassian.net/l/cp/vqeHskyJ) to layout project requirements, and map out details like the roadmap, and supportive diagrams -->

### Set up your coding environment
- You can refer to [requirements.txt](/requirements.txt) for the dependencies/libraries we have used in this project. Most of them can be installed via pip.
- You also need to run this project in a virtual environment. You can use [Anaconda](https://www.anaconda.com/) or [venv](https://docs.python.org/3/library/venv.html)
- Install Django and Python
- Run the Django development server via this command:`python manage.py runserver`. Ensure that this in the same directory as manage.py.
- Run the celery worker using this command: `python -m celery -A payments worker -l info`
- The Django developement server and celery worker need to run concurrently.

#### Technologies 

- Note the Django version(we used v3.2) 
- Note the Python version (we used v3.10.2)
- We used [Render](https://render.com/), [gunicorn](https://pypi.org/project/gunicorn/), [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) for deployment
- Postgres database --> [how to set up](https://dev.to/ndutared/setting-up-postgresql-on-a-djangopython-project-2pi9)
- [Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) for scheduling tasks
- We used Redis as a broker to work with Celery. You can also use it as a backend and not have to set up Postgres. Create a Redis instance on Render.

#### Backend set up
- Create a virtual environment with Conda or venv and activate it
- Install Python, Django, celery, gunicorn, psycopg2-binary, and their dependencies. Check [requirements.txt](/requirements.txt)

##### Django set up
- Create a virtual environment 
- Install Django via pip or conda (use `python -m django --version` or `django-admin --version` to check if it's already installed)

### Further Documentation and Project Management

- We are using **Jira** to track progress. We can share access as required.

- This question and answer on 
[Quora](https://www.quora.com/How-can-Python-be-used-to-implement-payment-reminder-systems-in-a-paywall-setup) can also shed light on the steps we'll take to implement the project.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 