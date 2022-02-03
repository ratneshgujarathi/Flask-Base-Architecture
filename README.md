**FLASK BASE ARCHITECTURE**
# Flask Clean Architecture

> A clean architecture is a software design that encourages the separation of concerns between the different components of a system.
> It is a software design that encourages the separation of concerns between the different components of a system.

## Steps to make clean flask architecture

**First create virtual environment of python using virtualenv or any virtual environment library**

<pre><code>virtualenv venv
</code></pre>

> **Then create a new folder and create a new project**

## App File Structure as follow
- First create a project folder
- All the folders and their explainations given below
- app folder contains various sub folders
    - controllers - contains all the controllers of the project which will be used to handle the request
    - models - contains all the models of the project which will be used to handle the request
    - helpers - contains all the helpers of the project which will be used to handle for supportive functions
    - middlewares - contains all the middlewares of the project 
    - handlers - contains all the handlers of the project which will be used to handle the errors and complex http request
    - notifications - contains all the notifications of the project which will be used to give the notification to the user
    - repositories - contains all static methods which will support the apis to handle requests
    - seeders - contains all the seeders which will be used to make repeated database operations using automations
    - services - contains all the extra services which will be used for supportive methods
- config folder contains all the config files
- database folder contains the database file
- resources folder is the templates folder contains all html files inside views of diffrent apps
- routes folder contains all the routes of app
    - apis - contains all the api routes
    - web - conatins all other routes 
- static folder contains all the static files for the app such as js, css, UI kits
- storage folder contains all the files that upload by users using web
    - app - files that are related to app which are not public 
    - public - files that are publicly visible such as post images, videos

**create runserver.py which has flask run server**
