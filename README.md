# mini-blog-flask
Flask based mini-blog application

# Setup

Before running the flask application, create the docker container from the root directory
```
docker-compose up
```
**note : If docker-compose DB data is changed, make sure to change it in blog_app/__init__.py as well!
```
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:{root_password}@localhost:{port}/{db_name}"
```

Database name, root password & port can be modified in the docker-compose.yml file

Run app (from root directory)

```
python app.py
```

![mini-blog-sc](https://user-images.githubusercontent.com/42161058/159187226-474d608a-e19f-480d-aa8a-4819e304b0cb.png)
