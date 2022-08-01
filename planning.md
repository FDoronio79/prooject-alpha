# Setup/Feature 1
* [x] Fork and clone starter project from:
    *  https://gitlab.com/sjp19-public-resources/sjp-2022-april/project-alpha-apr
* [x] Create a new virtual environment in the repository directory for the project
   * [x] Intiate: python -m venv .venv
* [x] Activate virtual environment
   * [x] Activate: source .venv/bin/activate
* [x] upgrade pip (if needed)
  * [x] pip install --upgrade pip
* [x] install django
  * [x] pip install django
* [x] install black
  * [x] pip install black
* [x] install flake8
  * [x] pip install flake8
* [x] install djhtml
  * [x] pip install djhtml
* [x] Deactivate virtual environment
  * [x] deactivate
* [x] Activate virtual environment
  * [x] source .venv/bin/activate
* [x] Use pip freeze to generate a requirements.txt file
  * [x] pip freeze > requirements.txt
* [x] Test Feature 1
  * [x] python -m unittest tests.test_feature_01
* [x] Add, commit, and push changes
  * [x] git add .
  * [x] git commit -m "Feature 1 complete"
  * [x] git push origin main

# Feature 2
* [x] Create a Django project named *tracker* so that the manage.py file is in the top directory (make sure to put the "."!!)
  * [x] terminal - django-admin start project tracker .
* [x] Create a djano app named *accounts*
  * [x] terminal - python manage.py startapp accounts 
* [x] Install *accounts* in the *tracker* Django project in the **INSTALLED_APPS** list
  * [x] tracker/settings.py/INSTALLED_APPS
    * [x] accounts.apps.AccountsConfig
* [x] Create a django app named *projects*
  * [x] terminal - python manage.py startapp projects
* [x] Install *projects* in the *tracker* Django project in the **INSTALLED_APPS** list
  * [x] tracker/settings.py/INSTALLED_APPS
    * [x] projects.apps.ProjectsConfig
* [x] Create a django app named *tasks*
  * [x] terminal - python manage.py startapp tasks
* [x] Install *tasks* in the *tracker* Django project in the **INSTALLED_APPS** list
  * [x] tracker/settings.py/INSTALLED_APPS
    * [x] tasks.apps.TasksConfig
* [x] Stage the migration
  * [x] python manage.py makemigrations
* [x] Apply migration
  * [x] python manage.py migrate
* [x] Create super user
  * [x] python manage.py createsuperuser
* [x] Execute test for Feature 2
  * [x] python manage.py test tests.test_feature_02
* [ ] Add, commit, and push changes
  * [ ] git add .
  * [ ] git commit -m "Feature 2 complete"
  * [ ] git push

