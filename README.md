# Instagram Backend
1. [API Docs](http://localhost:8000/v1/api/docs)

# Start developement
After installing `docker` and `docker-compose` please run
```
docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up
```

Then you will have and instance of the application [here](http://localhost:8000)

You can create the migrations with the following command **after creating the container**
```
docker exec -it gunicorn python manage.py migrate
```

## Start commiting to the repo
Please before you start commit for the first type start with following command to install `pre-commit` on your local system.
```
pip install pre-commit
pre-commit install
```

## What is pre-commit?
Pre-commit is built to solve hook issues. It is a multi-language package manager for pre-commit hooks. You specify a list of hooks you want and pre-commit manages the installation and execution of any hook written in any language before every commit. pre-commit is specifically designed to not require root access. If one of your developers doesn’t have node installed but modifies a JavaScript file, pre-commit automatically handles downloading and building node to run eslint without root.
## Usefull commands
<!-- TODO: more explanation -->

pre-commit auto-update
```
pre-commit autoupdate
```

Run against all files
```
pre-commit run --all-files
```
