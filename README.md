# Basic samples for the study of Flask Development (venv - pip version)

## Requirement
- Any Linux Distribution (I have not tested with WSL on Windows...)
- python3
- pip
- venv
- Your favorite CUI Terminal / Your favorite VSCode

## Get Started!!
1. Download the souce code via zip or just `git clone` this repos
2. Rename the file `.env.sample` to `.env`
3. On your terminal, move to the project's root directory (where `requirements.txt` exsists)
4. Run the following commands
```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ flask run
```
- Please make sure you are entering venv environment after running `source` command.

## To finish today's your flask development
```
$ deactivate
$ exit
```
- `deactivate` to exit venv environment, `exit` to close your terminal

## To resume yesterday's your flask development
Run the following commands @ where `requirements.txt` exsists
```
$ source .venv/bin/activate
$ flask run
```
