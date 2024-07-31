from django.urls import path as url_path
from importlib import import_module
from os import path
from pkgutil import iter_modules


modules = []
url_patterns = []


for (_, name, _) in iter_modules([path.dirname(__file__)]):
    modules.append(name)
    imported_module = import_module('.' + name, package='app_name.views')
    class_names = list(filter(lambda x: not x.startswith('__'), dir(imported_module)))

    for class_name in class_names:
        imported_class = getattr(imported_module, class_name)

        if hasattr(imported_class, 'url'):
            url_patterns += [url_path(imported_class.url, imported_class.as_view()), ]

        if hasattr(imported_class, 'urls'):
            for url in imported_class.urls:
                url_patterns += [url_path(url, imported_class.as_view()), ]


del import_module
del iter_modules
del path
del imported_module
del class_names
