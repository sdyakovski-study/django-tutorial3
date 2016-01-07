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
