# Views

## Explanation

View classes are automatically detected imported. View functions are detected and imported, too, but do not have all the features of view classes. This is exclusive to using the `__init__.py` files and directory structure for Django-Jumpstart. If you make a new app directory with `manage startapp`, replace the following things to maintain this functionality:

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

To automatically import urls for views, View classes should contain a `url=''` or `urls=[]` class attribute.

To add a template for a view, specifying `template=''` in the class attributes can be a good way to simplify reference in the code to it, while making the template very easy to find and see for that view when reviewing code. This doesn't do anything outside of the View class, however.
