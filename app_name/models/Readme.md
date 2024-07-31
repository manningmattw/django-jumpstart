# Models

## Explanation

Model classes are automatically detected imported. This is exclusive to using the `__init__.py` files and directory structure for Django-Jumpstart. If you make a new app directory with `manage startapp`, replace the following things to maintain this functionality:

- delete `admin.py`
- `models.py`
    - replace with `models/` directory
    - include files:
        - `https://github.com/manningmattw/django-jumpstart/blob/main/app_name/models/__init__.py`
- `views.py`
    - replace with `views/` directory
    - include files:
        - `https://github.com/manningmattw/django-jumpstart/blob/main/app_name/views/__init__.py`


## Features

Models in this structure should generally be organized by their relevance and how much code they employ. Really large models would benefit from their own model file. Otherwise, several model classes can be placed into a single model file or organized within the directory however works best.

Admin code is integrated with the model code. Generally, the admin class should be declared after the model class is declared, for code reference and organizational expectation. If an admin class gets too long for comfort, it can easily be split out into its own file. The recommended naming convention would be `example_admin.py` if `example.py` is where the Model class is.
