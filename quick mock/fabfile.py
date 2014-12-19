from fabric.api import *

env.PROJECT_NAME = "poc"
env.GITHUB_USER = "skoczen"
env.GITHUB_REPO = env.PROJECT_NAME
env.VIRTUALENV_NAME = env.PROJECT_NAME
env.HEROKU_APP_NAME = env.PROJECT_NAME
env.HEROKU_ACCOUNT = "buddyup"

env.SERVERS = {
    "live": "buddyuppoc",
    "staging": "buddyuppoc-staging",
}


def local_venv(cmd):
    env.cmd = cmd
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; %(cmd)s" % env)


def refreeze():
    local_venv("pip install -r requirements.unstable.txt")
    local_venv("pip freeze requirements.unstable.txt > requirements.txt")

def unit():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; manage.py test --attr=\!e2e" % env)


def e2e():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; manage.py test --attr=\!e2e" % env)


def wip():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; manage.py test --attr=wip" % env)

def deploy():
    local("git push heroku master")
    local("heroku run python manage.py syncdb --migrate --settings=envs.live")

def setup_db():
    local_venv("dropdb buddyup-poc --if-exists -U skoczen")
    local_venv("createdb buddyup-poc -U skoczen")
    local_venv("./manage.py syncdb --noinput")
    local_venv("./manage.py loaddata dev_user.json")
    local_venv("./manage.py migrate")
    local_venv("./manage.py fake_db")
