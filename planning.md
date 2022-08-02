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
* [x] Add, commit, and push progress
  * [x] git add .
  * [x] git commit -m "Feature 4 complete"
  * [x] git push

# Feature 5 
* Creating List View, registering the view for a path, registering the projects paths with the tracker project, creating a template for the view
* [x] Create a view that will get **all** of the instances of the Project model and puts them in the context for the template
  * [x] projects/views.py
    * [x] import Project model
      * [x] from projects.models import (Project, )
    * [x] create the list view function
      * [x] def show_projects(request):
    * [x] create the attributes of the view function
      * [x] projects = Project.objects.all()
      * [x] context = { "projects": projects }
      * [x] return render(request, 'projects/list.html', context)
* [x] create a new file in the **projects** app called *urls.py*
  * [x] projects/new file
    * [x] urls.py
* [x] Register the view in the **projects** app for the path **""** and the name **list_projects**
  * [x] Import path from django.urls
    * [x] from django.urls import path
  * [x] Import view from projects.views
    * [x] from projects.views import ( show_projects, )
  * [x] Create urlpatters variable with a list value
    * [x] urlpatterns = [ ]
  * [x] register path to urlpatterns
    * [x] path("", show_projects, name="list_projects")
* [x] Include the URL patterns from **projects** *app* in the **tracker** *project* with the prefix "projects/"
  * [x] tracker/urls.py
    * [x] import include
    * [x] from djang.urls import path, include
  * [x] register path to urlpatterns
    * [x] path('projects/', include(projects.urls)), *don't forget your commas*
* [x] Create templates folder in **projects app**
  * [x] projects/new folder
    * [x] templates
* [x] Create a **projects** folder in the **templates** folder
  * [x] projects/templates/new folder
    * [x] projects
* [x] Create a base.html in the templates folder
  * [x] templates/new file
    * [x] base.html
* [x] In the base.html put the fundamental 5 and block content for the body
  * [x] open main tag {% block content %} {% endblock %} close main tag
* [x] Create list.html file in projects folder
  * [x] templates/projects/new file
    * [x] list.html
* [x] Template specifications
  * [x] extend base (so the template inherits the fundamental 5 from base.html)
    * [x] {% exntends 'base.html' %}
  * [x] **main** tag that contains
    * [x] **div** tag that contains
      * [x] **h1** tag with the content **My Projects**
      * [x] *if there are no projects created, then*
        * [x] a **p** tag with the content **"You are not assigned to any projects"**
      * [x] *else*
        * [x] a **table** that has **two** columns,
          * [x] first colum with a **header** **"Name"**
            * [x] row with **names** of the projects
          * [x] second column with the **header "Number of tasks"**
            * [x] nothing here yet because we don't have any yet
* [x] Run Test for Feature 5
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 5 complete"
  * [x] git push

# Feature 6
* This Feature focuses on redirecting an empty url to the projects list view. This path will be registered as home in the **tracker** project *urls.py*
* [x] Access the urls.py in the **tracker** project
  * [x] tracker/urls.py
* [x] Import RedirectView
  * [x] from django.views.generic.base import RedirectView
* [x] Import reverse_lazy
  * [x] from djangos.urls import reverse_lazy
* [x] register "" path to projects/ and assign the name to "home"
  * [x] path("", RedirectView.as_view(url=reverse_lazy("list_projects")), name="home")
* [x] Run test for Feature 6
  * [x] python manage.py test tests.test_feature_06
* [x] Add, commit, and push progress
  * [x] git add .
  * [x] git commit -m "Feature 6 complete"
  * [x] git push

# Feature 7
* [x] Create a urls.py in the **accounts app**
  * [x] accounts/new file
    * [x] urls.py
* [x] Import LoginView to urls.py
  * [x] accounts/urls.py
    * [x] from django.contrib.auth.views import LoginView
* [x] Register the LoginView in the **accounts app's** *urls.py* 
  * [x] path("login/", LoginView.as_view(), name="login")
* [x] Include the URL patterns from **accounts** app to **tracker** project with the prefix "accounts/"
  * [x] tracker/urls.py
    * [x] path("accounts/", include('accounts.urls')),
* [x] Create **templates** directory in **accounts** app
  * [x] accounts/new folder
    * [x] templates
* [x] Create **registration** directory under **templates** directory
  * [x] templates/new folder
    * [x] registration
* [x] Create an HTML template named **login.html** in the ***registration*** directory
  * [x] templates/registration/new file
    * [x] login.html
* [x] Template specifications:
  * [x] fundamental five
    * [x] {% extends 'base.html %}
    * [x] a **div** tag containing
      * [x] an **h1** tag with the content "Login"
      * [x] a **form** tag with the method ***"POST"*** that contains
        * [x] an input for username
        * [x] input for password
        * [x] a button with the conten "Login"
* [x] create and set the variable **LOGIN_REDIRECT_URL** to the value **home** in ***tracker*** *settings.py*
  * [x] tracker/settings.py
    * [x] LOGIN_REDIRECT_URL = "home"
* [x] Run test for Feature 7
  * [x] python manage.py test tests.test_feature_07
* [x] Add, commit, and push progress
  * [x] git add .
  * [x] git commit -m "Feature 7 complete"
  * [x] git push origin main

# Feature 8
* [x] Protect the list view for the **Project** model so that only *logged in* users can acces it
  * [x] projects/views.py
    * [x] import login_required decorator
      * [x] from django.contrib.auth.deocrators import login_required
    * [x] apply decorator to list view
      * [x] @login_required to show_projects
* [x] Change the queryset of the view to filter the **Project** objects where **members** equals the ***logged in user***
  * [x] projects = request.user.projects.all()
* [x] Run test for Feature 8
  * [x] python manage.py test tests.test_feature_08
* [x] Add, commit, and push progress
  * [x] git add .
  * [x] git commit -m "Feature 8 complete"
  * [x] git push


# Feature 9
* [x] Import the **LogoutView** into the *accounts/urls.py* file
  * [x] from django.contrib.auth.views import LoginView, LogoutView
* [x] Register the view in the urlpatterns with the path "logout/" and the name "logout"
  * [x] path('logout/', LogoutView.as_view(), name="logout")
* [x] Create and set the variable **LOGOUT_REDIRECT_URL** to the value ***"login"*** in the **tracker** project's *settings.py*
  * [x] tracker/settings.py
    * [x] LOGOUT_REDIRECT_URL = "login"
* [ ] Run test for Feature 9
  * [ ] python manage.py test tests.test_feature_09
* Add, commit, push progress
  * git add .
  * git commit -m "Feature 9 complete"
  * git push