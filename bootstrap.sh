#!/bin/bash
eval "python3 -m pip install pipenv"
eval "pipenv install"
source $(pipenv --venv)/bin/activate
eval "python3 bot.py"
