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
* [x] Add, commit, and push changes
  * [x] git add .
  * [x] git commit -m "Feature 2 complete"
  * [x] git push

# Feature 3 WORKING IN THE PROJECTS APP ONLY
* [x] Create a Project model in the **PROJECT APP**
  * [x] projects/models.py
    * [x] class Project(models.Model):
* [x] Import User model
    * [x] from django.contrib.auth.models import User
* [x] Criteria for Project model
  *  Name | Type | Constraints
  * [x] name, string, maximum length of 200 characters
    * [x] name = models.CharField(max_length=200)
  * [x] description, string, no maximum length
    * [x] description = models.TextField()
  * [x] members, many-to-many, Refers to the auth.User model, related name "projects"
    * [x] members = models.ManyToManyField(User, related_name="projects")
* [x] Create a method to a convert name into a string using __str__
  * [x] def __str__(self):
        * return self.name
* [x] Stage migration
  * [x] python manage.py makemigrations
* [x] Apply migration
  * [x] python manage.py migrate
* [x] Run test for Feature 3
  * [x] python manage.py test tests.test_feature_03
* [x] Add, commit, and push progress
  * [x] git add .
  * [x] git commit -m "Feature 3 complete"
  * [x] git push

# Feature 4
* [x] Register **Project** model to admin.py in the *projects* app
  * [x] projects/admin.py
    * [x] import the Project model
      * [x] from projects.models import (Project, )
    * [x] register Project model to admin site
      * [x] admin.site.register(Project)
* [x] Run Test for Feature 4
  * [x] python manage.py test tests.test_feature_04
* [ ] Add, commit, and push progress
  * [ ] git add .
  * [ ] git commit -m "Feature 4 complete"
  * [ ] git push
