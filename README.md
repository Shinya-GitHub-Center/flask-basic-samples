# Basic blog-style construction for the study of Flask Development (venv - pip version)

- (( If you are looking for the simplest version to start with, please use [v1.0](https://github.com/Shinya-GitHub-Center/flask-basic-samples/tree/v1.0) instead.))
- (( If you are looking for a simple database starter, please use [v2.0-database](https://github.com/Shinya-GitHub-Center/flask-basic-samples/tree/v2.0-database) instead.))

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
$ flask db init
$ flask db migrate
$ flask db upgrade
$ flask run
```
- (Please make sure you are entering venv environment after running `source` command.)
5. Access to `http://127.0.0.1:5000/` via your browser
- At this point, no articles can be found on the blog, since you have not posted anything yet (No rows are created inside the database's table)
6. <ctrl + c> to quit Flask app server.

## About the database

- Make sure `database` directory has been created, with the database file & migration folder generated under the database directory
- You should check how the table & columns has been created inside the `database.db` file. The easiest way is just install 'SQLite3 Editor' extension via VSCode, then click `database.db` file from the VSCode explorer (I included VSCode recommendation using `extensions.json`)
- You can change to 'posted' table from 'SELECT * FROM' section, where you can see the 4 columns - id, title, contents, and create_at

## Post articles
1. After activation of the flask app server with `flask run` command, please access to `http://127.0.0.1:5000/admincreate` via your browser
2. Please fill out 'Admin Name' and 'Password' then click Login (you can check both values at the file `/app/settings.py`)
3. Fill out the Title and Content, then click Post
4. Access to `http://127.0.0.1:5000/` via your browser
5. Your posted articles can be found on the blog
6. Now you can check if your posts have been created into the database, just click `database.db` from VSCode explorer and switch to the 'posted table'

## Delete articles
1. After activation of the flask app server with `flask run` command, please access to `http://127.0.0.1:5000/admindelete` via your browser
2. Please fill out 'Admin Name' and 'Password' then click Login (you can check both values at the file `/app/settings.py`)
3. Click 'Delete' on the target article to delete the post
4. Access to `http://127.0.0.1:5000/` via your browser
5. The target articles are now removed from the blog
6. Now you can check if your post has been removed from the database, just click `database.db` from VSCode explorer and switch to the 'posted table'

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
- https://github.com/startbootstrap/startbootstrap-clean-blog
