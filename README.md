# Basic samples for the study of Flask Development (venv - pip version)

## ((If you are looking for the simplest version to start with, please use [v1.0](https://github.com/Shinya-GitHub-Center/flask-basic-samples/tree/v1.0) instead.))

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
- <ctrl + c> to quit Flask app server.

## Setting up the database
1. Run the following commands @ project's root directory (where requirements.txt exsists)
```
$ flask db init
$ flask db migrate
$ flask db upgrade
```
2. Make sure `database` directory has been created, with the database file & migration folder generated under the database directory
3. You should check how the table & columns has been created inside the `database.db` file. The easiest way is just install 'SQLite3 Editor' extension via VSCode, then click `database.db` file from the VSCode explorer (I included VSCode recommendation using `extensions.json`)
- You can change to 'posted' table from 'SELECT * FROM' section, where you can see the 4 columns - id, title, contents, and create_at

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

## Reference Books or URLs
- https://www.shuwasystem.co.jp/book/9784798067964.html
- https://qiita.com/t-iguchi/items/f7847729631022a5041f
