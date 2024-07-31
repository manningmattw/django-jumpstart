from django.utils.version import get_version


VERSION = (0, 0, 1, "beta", 0)
__version__ = get_version(VERSION)

if __name__ == '__main__':
    print(f"Django Jumpstart: {__version__}")
