# lose-found-platform
This a simple lose&amp;found system based on Vue.js and djangorestframework which might be a good example to learn vue and django
## overall design 
frontend: vue-router is applied the overall pagenation of the website and vue-component is used to complement the basic like data-view&data-submit
backend: with the vue as our frontend framework, the backend only need to save and provide the data for the requirement from frontend. Thus, the Djangorestframework is a good choice to wirte web API with ease. 
ajax: axios is used because it works well with vue, you can see the configuration of the axios in   frontend\src\main.js
## Install
You can get into the virtual enviroment by [virtualenv](https://virtualenv.pypa.io/en/stable/) to avoid some unexpected trouble, and django and djangorestframework is required to installed by pip. 

### 1.run the backend
`cd backend`  

`python manage.py runserver`

### 2.run the frontend
`cd frontend`  

`npm run dev`

## database
The database is based on SQLite,you can download some plug-in unit like [SQLite Manager](https://sqlitemanager.en.softonic.com/) to visualize the database
