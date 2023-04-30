NoteToMyself:  if you decide to run this on cloud check the settings.py file for the secret.key


# MVC Model	(Model-View-Controller)

```text
								 __ Model
								|
				User---Django---URL---View ---- |
								|  
								|__ Template

```


# Introduction to Django Web framework
Ready admin panel. Quick development.\
Ready User model which is called auth_user. It is a table in the SQLite DB.\
ORM: Object Relational Mapping\
Model View Template stracture\
Jinja 2 templates are going to be used.

# Installation 
You can install Django by following the steps in the website www.djangoproject.com \
You can also use the documentation tab to do search and get more information.\
How to check the version.
```text
PS C:\django> django-admin --version
3.2.13
```
# Create/Start a project
We created a project called djangoblog as below.

```bash
django-admin startproject djangoblog
```
Below files are generated automatically when we initiated the project.

manage.py: we do not edit this file. we use this file when we start/create an application\
__init__.py: This is used to show our project folder is a python module. it is empty.\
settings.py: Location of template files, database settings etc..\
urls.py: url to functions/codes mappings.\
wsgi.py: webserver settings. We don't modify this file.


# Start webserver
We start the webserver as below.
```buildoutcfg
python manage.py runserver
```
We get below warning while running the webserver.
```text
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
Run below command to create the sqlite.db.
```
python manage.py makemigrations
```

When we run the command, there will be many tables crated in the db.
```buildoutcfg
python manage.py migrate
```
# Create a user for admin panel
We create a superuser for the admin GUI. http://127.0.0.1:8000/admin

```buildoutcfg
PS C:\django\djangoblog> python manage.py createsuperuser
Username (leave blank to use 'ozenc499'): ozenc499
Email address: ozencmustafa@hotmail.com
Password:
Password (again):
Superuser created successfully.
```
# Create Application
We can develop our project within multiple sections. These sections are actually called applications and they can be used by other projects too.

We created an application named article as in the below command.
```buildoutcfg
python manage.py startapp article
```
models.py: The tables specific to our application should be created as a class(model).
apps.py: Shows the name of our application.
test.py: We develop our tests here.
views.py: url - function mapping.

# Creating tables according to our app 'article' in models.py
This table structure is created as a class in the models.py See class Article().

# Registering the Model to the Admin site
After we created a model called Article, we have to register this model/class in admin.py.
We do this importing the model.py and admin.site.register(Article) lines in admin.py
So this model will be registered to admin site and so it will be shown in the admin panel.

# Declearing the new app in the settings.py
We also have to add new app in the settings.py under INSTALLED_APPS.

# Migration
We always have to run below command when we created a new model.
This command will generate a file 0001_initial.py which looks like a SQL query. 

```buildoutcfg
python manage.py makemigrations
```

We also have to run this new generated file "xxxx.initial.py"  to create the migration data in the db.

```buildoutcfg
python manage.py migrate
```

# Personalize admin panel
You can use below documantation.\
https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

We do the personalization of admin panel in admin.py.\
We use decorator to register your model. We use classes such as Meta class to bind your Article class to ArticleAdmin class.\
We want to use some features of ModelAdmin class to personalizating our article in the admin panel.
- list_display
- list_display_links
- search_fields

# Django shell and ORM queries
We can do database queries without SQL commands by using the ORM structure of Django.

We can open django shell as below.
```bash
 python manage.py shell
 ```
 
 We have already installed apps in the settings.py. We want to use User Model from the Installed Apps.
 
 ```bash
In [1]: from django.contrib.auth.models import User

In [2]: from article.models import Article
```

Now we can create objects and save them into the Database.\ 
We will create an object a new username from User table/model.\

```bash
newUser = User(username = "testuser", password = "12345678")
```
We record this user to the database with save() function.
```bash
newUser.save()
```
When we check from SQLite db file, it has been seen that password is not enycripted. So if we want to enycript the password we can create users as below.\
set_password() function is going to enycript the password.

```bash
newUser2 = User(username="testuser2")
newUser2.set_password("12345678")
newUser2.save()
```

Another way to create a user. You can see the auth_user table and its variables and just define the users and its variables as below.
```bash
newUser3 = User()
newUser3.username = "testuser3"
newUser3.set_password("12345678")
newUser3.first_name = "Mustafa
newUser3.save()
```

We can create Article as below.
```bash
In [42]: article = Article(title = "episode 3", content = "Our engineer discovers django shell", author=newUser2)

In [43]: article.save()
```

Another way of creating a new article.
```bash
In [44]: article2 = Article()

In [45]: article2.title = "episode 4"

In [46]: article2.content = "Our engineer creates an article via Django shell by using ORM."

In [47]: article2.author = newUser3

In [48]: article2.save()
```

How to update an article and a third way to create an article
```bash
In [56]: Article.objects.create(title="episode 5", content="Our engineer is learning 3 different ways of creating a title vis django shell", author=newUser2)
Out[56]: <Article: episode 5>

In [57]: article = Article.objects.create(title="episode 5", content="Our engineer is learning 3 different ways of creating a title vis django shell", author=newUser2)

In [58]: article.title
Out[58]: 'episode 5'

In [59]: article.content
Out[59]: 'Our engineer is learning 3 different ways of creating a title vis django shell'

In [60]: article.content =  'Our engineer is learning 3 different ways of creating a title via django shell and also learns how to update via shell'

In [61]: article.save()
```
To list all articles.
```bash
In [68]: Article.objects.all()
Out[68]: <QuerySet [<Article: Pilot episode>, <Article: episode 1>, <Article: episode 2>, <Article: episode 3>, <Article: episode 4>, <Article: episode 5>, <Article: episode 6>]>

In [69]: Article.objects.get(title = "episode 4")
Out[69]: <Article: episode 4>
```

To get a specific article and delete\
```bash
In [70]: article = Article.objects.get(title = "episode 4")

In [71]: article.delete()
```

To get an articles which contains ...
```bash
In [74]: Article.objects.filter(title__contains = "pil")
Out[74]: <QuerySet [<Article: Pilot episode>]>
```

# Django URL structure
There is a variable called TEMPLATES inside the settings.py file.\
We will add "templates" into the DIRS key of this TEMPLATES variable inside the settings.py file.\
This is done to inform django that we are going to locate our html templates into the templates directory.\
- We created a templates directory and then we created index.html file under this templates directory.\
- We go to urls.py and we added a url path for the index.html.\
- Next step is to add a function for this url path but we should create our function inside the views.py file.\
- We created an index function inside the views.py and import this function inside into urls.py and add this function as a path.\
- Name your url addresses inside the urls.py. This helps in the future when you do a redirect you can do based on this naming.\

# Managing Static Files
The static directory and css file which is going to be created in this section is not going to be used in this project.\
So we may skip this part. The reason of it is;\
We are going to use Bootstrap 4 CDN inside of layout.html file which is under templates.
- Create static directory under any application. Inside this static directory we created a css file. 
- We created a href for style.css in index.html file and we gave the path of the css file in the href. 

But this href with path is not handy so django has a feature like {% load static %}.
- if you add {% load static %} in index.html file, you basically say to django to bring all files from /static directory.

But django looks static files only for the ones which are under an application. But there maybe also a static file under the root directory.\
To use these static files which are not in the application directory we have to say django the path of this static directory.

Below text should be added into settings.py for django to find the static files under BASE_DIR (/root).

```bash
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]
```
# Template Inheritance and Home page
We deleted the previous index.html file and we created layout.html and index.html in the template directory.\
We will include Bootstrap 4 CDN. https://getbootstrap.com/docs/4.0/getting-started/introduction/ \
We are going to inherit layout.html from index.html. We created a division and used jinja template so that index.html is going to fill this block body.

# Navbar 
We created a directory called includes under templates directory and we created a navbar.html under includes.
We are going to seach "bootstrap static navbar" on google and we will copy the source code and copy into our navbar.html\
https://getbootstrap.com/docs/4.0/examples/navbar-top-fixed/ \
We do right click and select source code and we copied the nav div. \
We addeded {% include "includes/navbar.html" %} jinja code into the layout.html just above to {% block body %}.

# About Page
We created a new html file about.html under templates directory. \
We inherit layout.html {% extend "layout.html" %} \
We created block body and write a paragrapgh inside the body. So that layout is the same for about and home pages.\
We have to add the path into the urls.py. \ 
we have to add the function in the views.py 

# How to render any contexts on a html template
This part is not going to be added into the code at the moment but we just learn how to do it.
We can send context to html templates.  In the views.py we have functions which renders a html page.\
Render functions has a context parameter which context=None as defult..\
We can give a variable(a value) to this context paramter and we can return this value on the body of an html page.\

# Django and Dynamic URLs
First we created the path in the urls.py.\
We created the function in the views.py.

# Creating a new application called users
We will create a new application called user. This application is going to manage login, logout and register functionality.

```bash
PS C:\django\djangoblog> python manage.py startapp user
```
We are going to create a url.py file under user directory.\
We gave a name to our application in the urls.py file with app_name = "user".\
We are going to make login and register tasks in this urls.py and we dynamically will relate these task to main urls.py.
- Add url paths (register,login and logout) into the user/urls.py.
- We have to relate our user/urls.py with main urls.py by adding the path('user/', include("user.urls")).
- We created a register.html in the templates.
- We create the register function in the user/view.py.
- We have to inform django that we created a new application. We do this in settings.py.

# RegisterForm from Form Class
Django has a forms class to create forms.
- We create forms.py under user application.
- We need username, password and confirm password fields in the form. For that we created a RegisterForm class.\
- We defined a clean() function to get the username and passwords. We write the clean function but name should be clean. This is a must.
- We compare password and confirmed fields and if they are not equal then we raise an exception.
- Else we return username and password.
- We completed the form and now we will show this form on register.html.
- First, We have to import our class (RegisterForm) into ther views.py.
- We create an object in the views.py for the form (form = RegisterForm())
- And we sent the context into the register.html by return render(request, "register.html", context) (in views.py)
- Now we are going to add this form in the register.html. To do that we create a ```<form>``` label.
- And we show the form with {{form.as_p}}.
- Till now we handle the get request but we have to do the post request too.(in views.py)
- POST is going to be sent only if the form is valid. When we say (in views.py) if form.is_valid() actually we call the clean function.
- We then get the username and password and and we insert into Database with ORM commands. 
- Then with login function from auth table we autamatically login this user. 
- We use redirect function (check imports in views.py) and return to the home page. 
- Till now, we register the user into the database and login and redirected to home page.

# Django Messages
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/ \
When you register successfully you may want to see a message on the html page. \
This message should be shown on all pages so it should be on layout.html page. 

- First you import the messages library into the view.py and add a message after login. 
- Then you have to show this on the page. After the navbar inside the container, we may be place html code for messages. 
- You find the html code in the documentation given above.  But we modifed this html code a lot. :)

# Login functionality
We have to create another form like Register. We need username and password fields. 
- We add a new class for the new form  'LoginForm()' in the user/forms.py
- We also have to add the form into the login.html file inside a ```<form>``` tag. We show the form with {{form.as_p}}. 
- We have to import LoginForm() function from forms.py into views.py "from .forms import RegisterForm, LoginForm"
- We now have to complete the loginUser() function in the user/views.py.
- We have to check if username and password is in the database. To do that we have to import authenticate.
- We create the form and show messages if succesfully login or fail.

# Crispy Forms Installation and Configuration
We will personalize our forms with bootstrap 4 grids by using crispy forms.\
We want to centralize our page so we use  https://getbootstrap.com/docs/4.0/layout/grid/ 
- We will use Offset classes like ".col-md-6 .offset-md-3" in the login.htlm page to leave equal spaces from sides.
- Everything in the login.html will be written inside this offset ```<div>```.
- So that Login Username and Password will be located in the middle of the page. But still not good enough.
- There is still a problem on how it looks. Because offset does not reflect to {{form.as_p}}.
- We will use template filter for {{form.as_p}} but we have to download Django Crispy forms. 
- https://django-crispy-forms.readthedocs.io/en/latest/
- pip install django-crispy-forms
- Once installed add crispy_forms to your INSTALLED_APPS in settings.py.
- Also set the template CRISPY_TEMPLATE_PACK in settings.py as CRISPY_TEMPLATE_PACK = 'bootstrap4'
- We have to load crispy filter with {% load crispy_forms_tags %} in the login.html. (like import)
- https://django-crispy-forms.readthedocs.io/en/latest/filters.html
- Now we will use crispy filter in the login.html. We changed {{forms.as_p}} into {{forms|crispy}.
- We do the same for register.html too.

# Log Out Functionality
- import logout in the views.py "from django.contrib.auth import login, authenticate, logout" 
- We completed the logoutUser() function in views.py. We just run logout(request)

# Session Control
- First we add the buttons to the navbar. We add them on the right side inside the same <ul> groups of list and right sided.
- For your information: inside the urls.py, you have the urls mapped to the related functions. Buttons on the navbar href  to urls.
- We do this control in the navbar.html by using {% if request.user.is_authenticated%}

# Dashboard and adding article
- article/dashboard/ url path is already a href in the navbar.html.
- we have to add the url path in article/urls.py
- we have to add function in the article/views.py
- we created dashboard.html under templates/ folder.

# ModelForms Usage
- We add a button on dashboard.html to add articles with a href = "/articles/addarticle".
- we create addarticle path to articles/urls.py
- we add addarticle function into the articles/view.py
- we created addarticle.html under template/ folder.

Now we have to create an article form. 
We will do this under the article application in a forms.py (just to make it better look)

- We created /article/forms.py file.
- We will create ArticleForm from ModelForm. https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
- To use ModelForm, we have to import "from .models import Article" into the forms.py.

Now we are ready this Article form in oour page.
- In views.py and import "from .forms import ArticleForm"
- In views.py, we created the addArticle() function
- we create addarticle.html (by copying from login.hmtl)

# Recording into the Database

- addArticle function is created in the article/views.py file .
- Save article is easy but there is a trick there. In the forms.py we selected fields = ["title", "content"] 
- So we did not select the author. But to save, django should know all three fields.
- The trick is: In thew views.py we save the form without commit so that we inform django with the auther name and save later.

# How to show our own articles on our dashboard
- First we go to article/views.py and import from .models import Article
- We are going to develop our dashboard(request) method of views.py.
- We want to retrieve all articles of the logged-in user. articles = Article.objects.filter(author= request.user)
- articles object is retrieved in a list with a dictionary format.
- Then we are going to give these articles as context into render as an input.
- Bootstrap 4 tables structure is going to be used to show these context in dahboard.html. 
- Bootstrap 4 tables can be checked from https://getbootstrap.com/docs/4.0/content/tables/
- We just copied the html code from the above given link into the dashboard.html and modify this code.
- If there is no article of a user we add {% if %}  {% else %} control in dashboard.html.

# Article Details and links

- We will give a link to the article.title in dashboard.html. 
- We do this with ```<a>``` tag so each article has a url link but we have define them dynamically.
- To define dymamic url we go to urls.py and we add the path as ```article/<int:id>```
- After the path in urls.py, we have to develop the function in views.py.
- def detail(request,id), we provide the id as input to the method as it is a dynamic url.
- We will return a html page "detail.html" and send the article to this page. 
- We use {{article.content}} in details.html but it is better if we use a template filter {{article.content|safe}} otherwise we see html tags.
- We will create detail.html under templates.

# Dynamic Url and startbootstrap blog post (a nicer layout)
- Search "startbootstrap blog post" in google here the link https://startbootstrap.com/template/blog-post
- we do (view frame souce) and we select only page content parts.
- we modified this html file and used as detail.html
- we locate the jinja commands in the html lile {{article.author}} so that we render the article info.

# 404 Not Found page
- We you try http://127.0.0.1:8000/articles/article/18 which does not exists, you see no information.
- Becasue there is no article with id 18.
- In this case we can return a 404 Not Found page
- For this, there is a very good function in django, "get_object_or_404". So we import this.

# Bootstrap files
We want to move our bootstrap files into static folder. 
- Under static we are going to create two directories. css and js.
- In layout.html we have bootsrap and js lines accessing from the internet. 
- We will include them statically on our server.
- We download our bootstrap version 4.0.0 from https://getbootstrap.com/docs/4.0/getting-started/download/
- or href is given in the layout. Just copy and paste the href and take the contents of the files.
- Take the ones in the layout.html and copy them under /static/css and static/js. like "bootstrap.min.css"
- Create a file under js named jquery-3.2.1.slim.min.js and copy.
- Copy the contents of https://code.jquery.com/jquery-3.2.1.js into static/js/jquery-3.2.1.min.js
- So you did for bootstrap js and jquery. So continue and commentout the js and bootstrap links from layout.
- load static into layout.html so add {% load static %}
- Add static bootstrap as ```<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">```
- Now we do not use js css from an external source. All are static and local.

# Managing Static files
Django suggests to use combined your js and combined css files instead of seperated css or sepearted js files.
Django provides django.contrib.staticfiles to help you manage them.
- Make sure django.contrib.staticfiles is icluded in your INSTALLED_APPS in settings.py
- Make sure STATIC_URL = '/static/' is in settings.py
- Checkout Manage Static files documentation from https://docs.djangoproject.com/en/4.0/
- We have to make an additional settings when we put this application on a production server.!
- This is STATIC_ROOT variable. We add into the settings.py STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
- Run "python manage.py collectstatic"

# CkEditor

- Follow the Installation steps in the link. https://github.com/django-ckeditor/django-ckeditor
- you add in the installed apps and also you run the collectstatics command again,
- Then you move to Usage section. We will do some changes in models.py
- First we add from ckeditor.fields import RichTextField into the models.py
- In the Usage section procedure says to include this settings into a Model. We have Article Model in our code!
- In our Article Model(app or class), we will do a change models.TextField to models.RichTextFiel.
- To use this rich text field what we have to do in our template?  Go to Outside of Django admin in the document.
- We send a form to addarticle.html So we have to add {{ form.media }} before {{ form|crispy }}

# Configure CkEditor
- Go to If you want to use allowedContent section in the procedure https://github.com/django-ckeditor/django-ckeditor
- We will do the change in the settings.py to use allowed content.
- Additionaly then the github project we add "allowedContent": True. To see complete code - see your settings.py.
- There is a bug and if we do not add 'allowedContent:True' then in the editor html source changes does not work. 
- You can use source button in the ckeditor to add html codes in your article.
- Source button is at the right side the last button.
- We are going to add code snippet there in the future.
- ckeditor width is bigger than the title but we want them to be equal. So we will add "width": "100%" into the settings.

# Django Handling File Upload
we use https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
- To make ImageField to work we have to install pillow
- We have to add enctype="multipart/form-data" into the html addarticle.html is our form for this project.
- So it becomes as  ```<form method = "post" enctype="multipart/form-data">``` in addarticle.html.
- FileField is for all types of documents including images.
- When we upload a file, this file should be saved some where. This place is to be MEDIA_URL = '/media/' in settings.py.
- In settings.py, If there is no media directory, Django will create it for you when you do an upload.
- In urls.py, We have to add a structure like "urlpatterns += static", otherwise we can not access to media url and python files.
- In settings.py, To access the MEDIA_URL in template you must add django.template.context_processors.media to your context_processeors inside the TEMPLATES config
- Django Clean_up is going to be installed. If we delete an article, all the files and folders to be deleted together. clean_up does this.
- pip install django-cleanup 
- add django-cleanup into INSTALLED_APP in settings.py
- We go to article/models.py and we will add article_image into the models.py.

Now we changed the model and we have inform django and we have to change the table in the database.
- So we have to run "python manage.py makemigrations"

To process it into the database we have to run below. 
- python manage.py migrate

You know that we had created an ArticleForm in forms.py from Artical model in models.py.
- We go to forms.py and as you know, we used the fields ["title","content"] only, but we will add "article_image" too.

How can we save the file or upload to /media/ ?
- We go to article/views.py and we are going to change addArticle(request) function.
- text comes from  request.POST but files come from request.FILES so we add (request.FILES or None) into addArticle(request) in view.py
- when you test the upload if media directory is not created check addartical.html!
- ```<form method = "post" enctype="multipart/form-data">```  should be exist in addarticle.html !!!
- We can also show the picture in the detail.html by adding image tag and location of the photo.
- So this to be added into detail.html.
```
<figure class="mb-4"><img class="img-fluid rounded" src="{{article.article_image.url}}" alt="..." /></figure>
```
- Still there is a problem, if there is no image in an article, it returns 404 Not Found. 
- This is becasue we add ```<img class>``` in detail.html (our template form) without a control.
- So we add an 'if-else' control to image tag. {% if article.article_image %} so if there is an image code will be read.

# Update articles
- urls.py: We will add /articles/update/ into the article/urls.py as 'update/<int:id>'
- /template: We create an update.html. We copy from addarticle.html. Do some minor text changes. instead of Add- Update.
- views.py: We add an updateArticle(request,id) method and return update.html

# Delete article
- url.py: path is added
- views.py: method is developed
- return redirect("article:dashboard")

# The login_required decorator
- We use a decorater to block access to some functions, if the user is  not loggedin. 
- This is called login_required.
- in the views.py we add:
- from django.contrib.auth.decorators import login_required
- ```@login_required``` add this decorator before a function in views.py
- if you define a path in the function ```@login_required(login_url="user:login")``` it redirects you to login.

# Article dashboard
- We have already an url_path for /articles in our project/urls.py. 
- So in article/urls.py we will use empty path '' as our url path. 
- in views.py, we will create a function for it.
- articles = Article.objects.all() can retrieve all articles and stores in a list.
- we create articles.html

# How to deploy on Pythonanywhere
https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

mkvirtualenv --python=/usr/bin/python3.8 mysite-virtualenv






































 

















































