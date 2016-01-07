Following "Web Development with Django Cookbook" recepes.
I changed the project structure a bit compared to the one suggested in the book:
- Instead of creating the virtualenv in ., I created it in django-tutorial3-env:
   $ virtualenv django-tutorial3-env
   $ source django-tutorial3-env/bin/activate
- So instead of getting bin, include, lib etc. directly in the django-tutorial3 folder, I have in there an django-tutorial3-env folder, and these are inside
- I do not create a project/django_project/myproject
- instead I run 
   (django-tutorial3-env)$ django-admin.py startproject project 
  directly in the django-tutorial3 folder, which created in it project/project
- then cd project && mv project tutorialsite
- now I have in django-tutorial3 a folder project which has tutorialsite and manage.py. Added in here this README.md

- In my other study projects I had called startproject myproject, which would create myproject/myproject and then would rename the outer myproject to project.
 It worked without a problem because Django (in manage.py, myproject/settings.py and myproject/wsgl.py) only cares how the inner folder is called. THat folder is the project's Django package. 
 But this time I renamed the inner one - from project to tutorialsite. Then I had to go in the 3 py files and manually chnaged the reference from project to tutorialsite.
- Now python manage.py runserver works and starts the Development Server.
