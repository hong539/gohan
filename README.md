# gohan
gohan is a Python Natural Language Processing (NLP) tool combined from pykakasi/ related packages.

## prerequisites

* Python == 3.8.16
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programing_languages/python/python.md)
* Project dependcy detialls will be in pyproject.toml/poetry.lock

## to-do-list

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
poetry add beautifulsoup4
poetry add pandas
poetry add lxml
```