# Setup

### Virtual Environment
Check if your current python has virtual environments installed
```virtualenv --version```

Otherwise you can install via ```pip install virtualenv```.

These are the steps to setup a new virtual environments.

1. Now either make a directory in your project folder or in a virtual environments folder by going 
to the location of where you want to put your new directory by ```$ cd /path/of/directory```
2.  Make a new directory by ```mkdir ~/virtualenvironment```
3.  Then install new virtual environment here by ```virtualenv ~/virtualenvironment/webdev -no-site-packages```
4.  Go to your bin directory of your new environment by ```cd ~/virtualenvironment/webdev/bin```
4.  Activate environment by ```source activate```

Within this environment you can import all the libraries and modules you need these type of projects.
Alternatively you can save your environment in in your repository. 
This kind of only works in smaller projects with specific libraries.

### Django
First install Django by ```pip install Django```. 
Check if it installed by ```python -m django --version```. 

Now you have Django installed you can use it to create a new project.
Go to the directory where you want to create a new Django project by 
```cd path/to/repo```
Then create the project by ```django-admin startproject otopos```.

That's it! You made your Django project framework. 
You can test it by going to your new project directory by ```cd otopos``` and typing ```python manage.py runserver```

#### Apps
The framework created is actually this: a framework. You will need to create apps in order to add functionality. 
Apps are modular and can be interchanged between different frameworks.

Assuming you are still inside your 
Django project directive you can create a 
new app by ```django-admin startapp map_viewer```

#### Templates
```
mkdir templates
mkdir static
```
Make a new HTML file in templates and write some text in it.

