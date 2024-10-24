# Django Jumpstart<br>A Foundational Django Setup For Simple Startup and Development

## Purpose
Django Jumpstart is a project meant to save time in building and maintaining a Django/Postgres backend using a container-based environment. A working knowledge of Python, Django, Postgres, and Docker is still needed to this setup, though.

This repo is always a work in progress. Use this code at your own risk. There are many more processes and code simplification techniques that will be standardized by this project over time. Note that this project is versioned and will be tagged in the `__version__.py` file and Github to make compatibility management easier.

---

## Features
- Prebuilt settings files for development and production
- A scalable and commonly recognizable file structure
- Automatic import of Models, Views, etc
- Dockerfile and docker-compose ready to go
- Docker-extensions and iPython for advanced shell interaction
- Shortcuts for common commands:
    - `manage` or `m` = `python manage.py`
    - `shell_plus` or `sp` = `python manage.py shell_plus`

---

## Setup
This setup prefers a development environment using either pure Linux or WSL/WSL2. Note, WSL2 has a few issues in Windows 10, so if you are using Windows 10, consider using WSL. Otherwise Windows 11 WSL2 work like a treat.

The containerization tool used in these instructions is Docker but any other container service, like podman, should work, but its up to you to know the syntax differences.

The IDE instructions are based on VSCode. Even if your development setup is different, these instructions should likely work with just a little change in how you might execute each part.

### Python Versions:
This project and the Docker setup is currently built with Python 3.13.0. You do not need to have these versions or dependencies installed, as Docker will take care of this. Therefore, Python `venv` instructions are not included here.


**1. Create a new repo**
You can template Django Jumpstart to create a new repository. I recommend this method. After you do so, just `git clone` the new repo and follow the next instructions. If you have a repo, and you want to setup Django for the first time using this repo, you can `git clone` the Django Jumpstart repo directly into the existing repo:
```
cd /path/to/repos/project_directory
git clone git@github.com:manningmattw/django-jumpstart.git .
```
Then, just follow the next instructions.


**2. Update project name and app name and all references**

I load open VSCode from the project directory with `code .` since I am using WSL 2. This opens VSCode to work with the WSL instance directly.

- In VSCode, Edit > Replace in Files:
    - from `project_name` to your_lowercase_project_name
    - from `PROJECT_NAME` to YOUR_UPPERCASE_PROJECT_NAME
    - from `ProjectName` to YourCamelCaseProjectName
    - from `app_name` to your_lowercase_app_name
    - from `APP_NAME` to YOUR_UPPERCASE_PROJECT_NAME
    - from `AppName` to YourCamelCaseAppName


**3. Create a .env file with a generated SECRET_KEY for Django in it**

Run the following command:
```
python django_jumpstart.py
```
This will create a `.env` file and add `SECRET_KEY=<random secret key>` to the `.env` file. This also outputs the version of Django Jumpstart used to build this project.


**5. Build the development containers**

I use Windows Terminal, which supports tabs, so I dedicate a tab to the container, because it let's me watch the Django manage console output, which is useful in debugging and testing. So, in a new terminal tab/window, navigate to /path/to/repos/project_directory/ and run
```
docker compose up --build --force-recreate
```

If the postgres fails when running, and Django manage doesn't start, `CTRL-C` and `docker compose up` again and it should work. Once the services are up, navigate to http://localhost:8000 and you should see a hello world index view. This will prove that the setup is working.


**6. Migrate the built-in Django modules and create the superuser account.**

There is an example model built, and if you want to use it, you will need to make a migration first. Otherwise, I recommend replacing the example code with your own before doing any migration file creation. Therefore, we need a new terminal window in the /path/to/repos/project_directory location. Then, exec into an interactive web container instance:
```
docker compose exec -it web bash
```
Now, migrate the current migrations from the built-in Django modules, using the `manage` alias:
```
manage migrate
```
Then, you will need to create a superuser account:
```
manage createsuperuser
```
Then, navigate in your browser to http://localhost:8000/admin, and use your new superuser account to log in.

---

## Good to Know Things
### Django Shell Plus
One of the most powerful ORM testing tools is the Django shell. In the exec web shell, you can use the aliases `sp` or `shell_plus` to access it. In the settings files, there is a `SHELL_PLUS_IMPORTS` list where you can add custom imports for shell_plus.

### Django Management Commands
`m` or `manage` without anything else will give a full list of the management commands, including any custom management commands you make. There is an example management command in the app management/commands directory, if you need an example of a command.

### Quick commands
Build and spin up the Docker image and console.
```docker-compose up --build```

After pressing `CTRL-C` in the Docker console, you should down the image to shutdown the network, too.
```docker-compose down```

Load the exec shell for the web container.
```docker-compose exec -it web bash```

Load the exec shell for the postgres container.
```docker-compose exec -it db bash```
