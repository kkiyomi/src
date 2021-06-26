import os
import sys

if __name__ == '__main__':
    # The path to your project
    path = 'file:C:/Users/user/Desktop/python/src'
    if path not in sys.path:
        sys.path.append(path)

    # Change to your project settings root
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    # django.setup()

    # exec(open('shell.py').read())

    from django.core.management import execute_from_command_line

    execute_from_command_line(['.', 'shell'])


def setup_django():
    import sys
    import django
    import os

    path = 'file:C:/Users/user/Desktop/python/src'
    if path not in sys.path:
        sys.path.append(path)  # /home/projects/my-djproj
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mysite.settings')
    django.setup()
