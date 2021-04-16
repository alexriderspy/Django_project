# Django_project
Views in django actually mean functions that are going to process some kind of request and respond accordingly. Like mostly users request a webpage and we help them navigate to a webpage and at other times they may need to login or download a file or share a webpage 

Basic Structure of a Django Webpage
1. user types in website/music/
2. as a response it opens urls.py in our project
3. searches in urlpatterns.. pattern matched include('music.urls') so now it moves over to music.urls.py file and does what the views want us to do
4. looks for a view(aka function) that matches with views.index (index is the function and views is the file name)

when we do python manage.py migrate-- it basically synchronises our webapp with our database.. which in this case is mySql

Now we create a model for our webapp--blueprint
we basically open models.py and create a class with some variables and django automatically converts the variables into columns in our database
# Very Very important
migrations are basically changes made to our database. so we need to do python manage.py makemigrations "name of our app"
and then do python manage.py migrate
now we are good to go
to see what are migrations do python manage.py sqlmigrate music 0001 (or whatever name we see)
and it shows exactly what we created
