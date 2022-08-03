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
* [x] Run test for Feature 9
  * [x] python manage.py test tests.test_feature_09
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 9 complete"
  * [x] git push

# Feature 10
* [x] Import UserCreationForm
* [x] You'll need to use the special create_user  method to create a new user account from their username and password
* [x] You'll need to use the login  function that logs an account in
* [x] After you have created the user, redirect the browser to the path registered with the name "home"
* [x] Create an HTML template named signup.html in the registration directory
* [x] Put a post form in the signup.html and any other required HTML or template inheritance stuff that you need to make it a valid Web page with the fundamental five (see specifications below)
* [x] Run Test for Feature 10
  * [x] python manage.py test tests.test_feature_10
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 10 complete"
  * [x] git push

# Feature 11
* [x] Import the ***Project*** model from **projects** app
  * [x] from projects.models import Project
* [x] Import User model
  * [x] from django.contrib.auth.models import User
* [x] Create a Task model in the **task** app
  * [x] class Task(models.Model):
* [x] Create and set attributes
  * [x] Name | Type | Constraints
    * [x] name, string, maximum length of 200 characters
      * [x] name = models.CharField(max_length=200)
    * [x] start_datem, date-time, none
      * [x] start_date = models.DateTimeField()
    * [x] due_date, date-time, none
      * [x] due_date = models.DateTimeField()
    * [x] is_completed, Boolean, default value should be false
      * [x] is_completed = models.BooleanField(default = False)
    * [x] project, foreign key, Refers to **projects.Project** model, related name "tasks", on delete cascade
      * [x] project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    * [x] assignee, foreign key, Refers to the auth.User model, null is True, related name "tasks", on delete set null
      * [x] assignee = models.ForeignKey(User, related_name="tasks", on_delete=models.SET_NULL)
* [x] Task should convert **name** property to string using __str__ method
  * [x] def __str__(self):
          * return self.name
* [x] Stage migration
  * [x] python manage.py makemigrations
* [x] Apply migration
  * [x] python manage.py migrate
* [x] Run Test for Feature 11
  *  [x] python manage.py test tests.test_feature_11
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 11 complete"
  * [x] git push

# Feature 12
* [x] Register the Task model with the Django admin site
  * [x] tasks/admin.py
  * [x] Import Task model
    * [x] from tasks.models import Task
  * [x] register Task model
    * [x] admin.site.register(Task)
* [x] Stage migration
  * [x] python manage.py makemigrations
* [x] Apply migration
  * [x] pyhton manage.py migrate
* [x] Run Test for Feature 12
  * [x] python manage.py test tests.test_feature_12
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 12 complete"
  * [x] git push

# Feature 13 Deatail View
* [x] Create a view that shows the details of a particular project
  * [x] projects/views.py
    * [x] def project_details(request, pk):
        project = Project.objects.get(pk=pk)
        context = {
            "project": project
        }
        return render(request, "projects/detail.html", context)
* [x] Add login decorator to the detail view function, to limit access to logged in users
  * [x] @login_required
* [x] Register path to the project details in the **projects** *urls.py* with the path "< int:pk >/" and name "show_project"
* [x] Create a template to show the details of the project and a table of its tasks
  *  Template details
     *  [x] fundamental 5
     *  [x] a **main** tag containing
        *  [x] a **div** tag containing
           *  [x] a **h1** tag with the project's name as its content
              *  [x] < h1 > {{project.name}} < /h1 >
           *  [x] a **p** tag with the project's description
              *  [x] < p > {{project.description}} < /p >
           *  [x] an **h2** tag that has the contents "Tasks"
           *  [x] *if the project has tasks*
              *  [x] a **table** that contains
                 *  [x] **5** columns with the headers
                    *  [x] "Name",
                    *  [x] "Assignee",
                    *  [x] "Start date",
                    *  [x] "Due date",
                    *  [x] "Is completed"
                 *  [x] Rows for each task in the project
           *  [x] *else*
              *  [x] a **p** tag with the content "This project has no tasks"
  *  [x] Update the list template to show the number of tasks for a project
  *  [x] Update the list templpate to have a **link** from the **project name** to the **detail view** for that project
  *  [x] Run Test for Feature 13
     *  [x] python manage.py test tests.test_feature_13
  *  [x] Add, commit, push your progress
     *  [x] git add .
     *  [x] git commit -m "Feature 13 complete"
     *  [x] git push

# Feature 14 Create a Project (create view)
* [x] Create a modelform for Project
  * [x] Create a forms.py in projects
    * [x] projects/new file
      * [x] forms.py
    * [x] crate ProjectForm in forms.py that displays all fields
      * [x] class ProjectForm(models.Form)
                class Meta:
                    model = Project
                    fields = "__all__"
* [x] Import ProjectForm to views.py
* [x] Create a **create** view for the **Project** model, make sure that if the project is created to redirect to the detail view
  * [x] def create_project(request):
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            project = form.save()
            return redierct("show_project", project.pk=pk)
        context {
            "form" = form
        }
        return render(request, "projects/create.html", context)
* [x] Add login decorator to function vie
  * [x] @login_required
* [x] Register the view for the path "create/" in the **projects** *urls.py* with the name "create_project"
  * [x] projects/urls.py
    * [x] import create_project
    * [x] path("create/", create_project, name="create_project"),
* [x] Create an HTML template with the following specifications:
  * [x] fundamental five
  * [x] a **main tag** containing
    * [x] a **div** tag containing
      * [x] an **h1** tag with the content "Create a new project"
      * [x] a **form tag** with the method post and contains
        * [x] a text input for **name**
        * [x] a text input for **description**
        * [x] a select tag with name **members**
        * [x] a button with the content **Create**
* [x] Run Test for Feature 14
     *  [x] python manage.py test tests.test_feature_14
  *  [x] Add, commit, push your progress
     *  [x] git add .
     *  [x] git commit -m "Feature 14 complete"
     *  [x] git push

# Feature 15 Create view for Task model (working in the tasks project)
* [x] Create a forms.py in the **tasks** app
  * [x] tasks/new file
    * [x] forms.py
* [x] Create a TaskForm for the Task model for all the fields except is_completed
* [x] Import Task model from tasks.models
  * [x] from tasks.models import Task
  * [x] class TaskForm(forms.ModelForm):
            class Meta:
                model = task
                fields = [
                    'name',
                    'start_date',
                    'due_date',
                    'project',
                    'assignee'
                ]
* [x] Import TaskForm from forms.py
  * [x] from tasks.forms import TaskForm
* [x] Create a create view for the Task model that redirects to the project if task is successfully created
  * [x] def create_task(request):
            form = TaskForm(request.POST or None)
            if form.is_valid():
                task = form.save()
                return redirect("show_project", pk=task.project.pk)
            context = {
                "form": form
            }
            return render(request, "tasks/create.html", context)
* [x] Apply login decorator to the view function
  * [x] @login_required
* [x] Create a *urls.py* in the **tasks** app
* [x] Register the view function to the path **"create/"** with the name "create_task"
    * [x] urlpatterns = [
        path("create/", create_task, name="create_task"),
    ]
* [x] Include the URL patterns from **tasks** app in the **tracker** project *urls.py* with the prefix **"tasks/"**
  * [x] path("tasks/", include("tasks.urls")),
* [x] Create a templates directory in the tasks project
* [x] Create a tasks directory in the templates directory
* [x] Create a template for the create view with the following specifications:
  * [x] fundamental five
  * [x] a **main** tag containing
    * [x] a **div** tag containing
      * [x] an **h1** tag with the content "Create a new task"
      * [x] a **form** tag that contains:
        * [x] a text input for **name**
        * [x] an input for **start_date**
        * [x] an input for **due_date**
        * [x] a selector for **projects**
        * [x] a selector for **assignee**
        * [x] a button with the content **Create**
* [x] Add a link to create a task from the project detail page
  * [x] projects/detail.html
    * [x] after the h2 tag create a p tag that contains the link to create a task
      * [x] < p > < a href="{% url 'create_task' %}> < /a > < /p>
* [x] Run test for Feature 15
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 15 complete"
  * [x] git push

# Feautre 16 List view for Task
* This list view will display the tasks specific to the logged in user
* [x] Create a list view for the **Task** model that filters to the logged in user by using the **assignee** equal to the current logged in user
  * [x] def show_tasks(request):
        tasks = Task.objects.filter(assignee=request.user)
        context = {
            "tasks": tasks
        }
        return render(request, "tasks/list.html", context)
* [x] Apply login decorator to the view function
  * [x] @login_required
* [x] Register the view to te **tasks** app *urls.py* to the path **"mine/"** with the name "show_my_tasks"
  * [x] path("mine", show_tasks, name="show_my_tasks")
* [x] Create an HTML template with the following specifications:
  * [x] The fundamental five
  * [x] a **main** tag that contains
    * [x] a **div** tag that contains
      * [x] an **h1** tag with the content "My Tasks"
      * [x] *if there are tasks assigned to the person*
        * [x] a **table** tag
          * [x] **table headers**:
            * [x] Name,
            * [x] Start date,
            * [x] End dat,
            * [x] Is completed (should show the word "Done" if completed, else show nothing)
          * [x] **table rows**
            * [x] data of the respective headers
      * [x] *else*
        * [x] a **p** tag with the content "You have no tasks"
* [x] Run test for Feature 16
  * [x] python manage.py test tests.test_feature_16
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 16 complete"
  * [x] git push

# Feature 17 Update Staus
* This feature allows a person to update the status on one of their assigned tasks from incomplete to complete.
* [x] Create an update view for the Task model taht only is concerned with the **is_completed** field and after submissions reidrects to the **"show_my_tasks"** url path
  * [x] def update_task_status(request, pk):
            is_completed = request.POST.get('is_completed')
            task = Task.objects.get(pk=pk)
            try:
                task.is_completed = is_completed
                task.save()
            except IntegrityError:
                pass
            return redirect("show_my_tasks")
* [x] Register the view for the app "< int:pk >/complete/" and the name "**complete_task**
  * [x] path("< int:pk>/complete/", update_task_status, name="complete_task")
* [x] Modify the **My Tasks** *template* tp comply with the template specification:
  * [x] < form method="post" action="{% url 'complete_task' task.id %}">
  {% csrf_token %}
  < input type="hidden" name="is_completed" value="True">
  < button>Complete< /button>
< /form>
* [x] Run test for Feature 17
  * [x] python manage.py test tests.test_feature_17
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Feature 17 complete"
  * [x] git push

# Feature 18 Description Markdown enabled
* In this, you will take the project description and make it Markdown enabled.
* [x] Install the django-markdownify package using pip (the first pip command in the instructions) and put it into the INSTALLED_APPS in the tracker settings.py according to the Installation  instructions block
  * [x] pip install django-markdownify
* [x] Also, in the tracker settings.py file, add the configuration setting to disable sanitation 
* [x] In your the template for the Project detail view, load the markdownify template library as shown in the Usage  section
  * [x] {% load markdownify %}
* [x] Replace the p tag and {{ project.description }} in the Project detail view with this code
  * [x] {{ project.description|markdownify }}
* [x] Use pip freeze to update your requirements.txt file
  * [x] pip freeze > requirements.txt
* [x] Run test for Feature 18
  * [x] python manage.py test tests.test_feature_18
* [x] Add, commit, push progress
  * [x] git add .
  * [x] git commit -m "Featuer 18 complete"
  * [x] git push
 
# Submission
* [x] Format code using the following command:
    * [x] black accounts projects tasks tracker
* [x] Format HTML templates:
  * [x] djhtml -i tasks/templates/tasks/create.html
  * [x] djhtml -i tasks/templates/tasks/list.html
  * [x] djhtml -i projects/templates/base.html
  * [x] djhtml -i projects/templates/projects/create.html
  * [x] djhtml -i projects/templates/projects/detail.html
  * [x] djhtml -i projects/templates/projects/list.html
  * [x] djhtml -i accounts/templates/accounts/login.html
  * [x] djhtml -i accounts/templates/accounts/signup.html
* [x] Check for unused imports or variables with:
  * [x] flake8 --select F401,F403,F541,F601,F631,F632,F634,F701,F702,F703,F706,F707,F811,F821,F823,F831,F841 projects accounts tasks tracker
* [x] Delete any files that Django generated and you didn't use
  * [x] git rm << path/to/file.py >>
* [x] Run unit tests
  * [x] python manage.py test
* [x] Add, commit, and push final project
  * [x] git add .
  * [x] git commit -m "Final submission"
  * [x] git push origin main
