# gohan
gohan is a Python Natural Language Processing (NLP) tool combined from pykakasi/ related packages.

## prerequisites

* Python == 3.8.16
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programing_languages/python/python.md)
* Project dependcy detialls will be in pyproject.toml/poetry.lock
    * [pykakasi](https://codeberg.org/miurahr/pykakasi)
    * [Django REST framework](https://www.django-rest-framework.org/)

## to-do-list

* make a web API with Django REST framework
* How to update "pyproject.toml"? if I change the Python version?
    * ~~changer Python interpreter version from 3.8 to 3.10~~
* make some unittest
* web scraping some data with beautifulsoup4/pandas/lxml packages

## quick start

```shell
#check pyenv+poetry
pyenv versions
poetry --version
poetry shell
#Installing dependencies only
poetry install --no-root

#add new packages
poetre add pykakasi
poetry add beautifulsoup4
poetry add pandas
poetry add lxml
```