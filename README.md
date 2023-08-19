# (database branch) : Implementation of the very basic SQLite database

## Requirement
- Any Linux Distribution (I have not tested with WSL on Windows...)
- python3
- pip
- venv
- Your favorite CUI Terminal / Your favorite VSCode

## Get Started!!
1. Download the souce code via zip or just `git clone` this repos (please checkout to database branch)
2. Rename the file `.env.sample` to `.env`
3. On your terminal, move to the project's root directory (where `requirements.txt` exsists)
4. Run the following commands
```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
- Please make sure you are entering venv environment after running `source` command.

## Setting up the database
1. Run the following commands @ project's root directory (where requirements.txt exsists)
```
$ flask db init
$ flask db migrate
$ flask db upgrade 
```
2. Make sure `database` directory has been created, with the database file & migration folder generated under the database directory
3. You should check how the table & columns has been created inside the `database.db` file. The easiest way is just install the SQLite3 Editor extension via VSCode. (I included VSCode recommendation using `extensions.json`)

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
$ <any flask commands>
```

## Reference Book
https://www.shuwasystem.co.jp/book/9784798067964.html
