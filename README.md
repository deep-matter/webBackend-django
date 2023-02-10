# webBackend-django
this is the pathway of learning Backend techno using Django python, 
now as long as far doing this learning of django Framework we will be setting up the whole steps to build End-to-End project 
### Creating Env virtual environment 
* setup environment 

          pip install virtualenv && virtualenv -p python3.9 ./dev 

    now let's install Django Framework in our own ENV 

           pip install django  
    Django Framework has commands CLI that helps with managing the projecr Pipline , first we will need to create the project Folder using **startproject**  

          python manage.py startproject ./development         
* next step is building UI 
  - in my case i used Built-in Template Bootstrap only to save time of doing Frontend . because our main Goal in this Learning process is make web appliaction interface that interact with DataBase and builing APIS 
  here few Resources Could help to get hands-on 
     * FIsrt learning few basic [**Jinja**]{https://documentation.bloomreach.com/engagement/docs/jinja-syntax} becuase we need to code some statment conditions to return something and inhere the from Base.html to make easy sharing components of HTML blocks betwwen Pages 
     * Setup the static Folder here we will save all our Style design of templates in Static folder to do so we will need to add some configuration to project settings.py 

      ```python 
      STATIC_URL = '/static/'
      MAIN_PROJECT = os.path.dirname(__file__)
      STATICFILES_DIRS = (
      os.path.join(MAIN_PROJECT, 'static/'),
      ```
      ```html 
            {% load staticfiles %}
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Clean Blog</title>
            <!-- Bootstrap Core CSS -->
            <link href="{% static "/css/bootstrap.min.css" %}" rel="stylesheet">
            <!-- Custom CSS -->
            <link href="{% static "/css/clean-blog.min.css" %}" rel="stylesheet">
            </head>  
      ``` 
* setting the database connections and Configuration 
   -  at this step most of the application out there used **PostgresSQL** database in Production Level  
   fisrt install PostgreSQL and for more information install install PgAdmin to access the database through GUI interface 
   by default django framework used Sqlite3 as default database , 

   ```python 
      DATABASES = {
            "default": {
                  "ENGINE": "django.db.backends.postgresql",
                  "NAME": "houselist",
                  "USER":"postgres",
                  "PASSWORD":"*******",
                  "host":"localhost"
            }
            }
      ```
* setting the data Upload folder  Configuration 
   -  in our case to save the Images which uploaded through admin area we will configure the Media folder settings that Django provide to us as default setup 

    ```python 
      DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
      ## the media file settings
      MEDIA_ROOT = os.path.join(BASE_DIR , "media")
      MEDIA_URL = "media/"
    ```
    but we will need to add the static Path to in urls.py in project settings 

     ```python 
     urlpattern = [] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     ```
* Queries SQL : in this part we wil use ORM built methods to query the data for more [Info](https://www.w3schools.com/django/django_queryset_filter.php) visit this site to get hands-on the Filter methods used to translate the based method class to SQL language 


                  
   




     

