from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = ["Django>=2.2",
                          "asgiref>=3.5.0",
                          "djongo>=1.3.6",
                          "mysql>=0.0.3",
                          "mysql-connector-python>=8.0.28",
                          "mysqlclient>=2.1.0",
                          "protobuf>=3.19.4",
                          "pymongo>=4.0.1",
                          "pytz>=2021.3",
                          "sqlparse>=0.4.2",
                          "django-cors-headers>=3.11.0",
                          "djangorestframework>=3.13.1",
                          "MySQL-python>=1.2.5",
                          "uwsgi>=2.0"],
  extras_require       = {
                            "test": [
                              "colorama>=0.4.4",
                              "coverage>=6.3.2",
                              "django-nose>=1.4.7",
                              "nose>=1.3.7",
                              "pinocchio>=0.4.3"
                            ]
                         }
)