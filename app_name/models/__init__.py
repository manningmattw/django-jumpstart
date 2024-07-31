from importlib import import_module
from pkgutil import iter_modules
from os import path


modules = []

for (_, name, _) in iter_modules([path.dirname(__file__)]):
    modules.append(name)
    imported_module = import_module('.' + name, package='app_name.models')
    class_names = list(filter(lambda x: not x.startswith('__'), dir(imported_module)))

del import_module
del iter_modules
del path
del imported_module
del class_names
