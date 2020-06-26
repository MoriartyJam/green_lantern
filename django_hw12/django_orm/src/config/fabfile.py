from fabric.api import local

def test():
    local("./manage.py test car_dealer")

def commit():
    local("git add -p && git commit")

def push():
    local("git push https://github.com/darkmatter4114/green_lantern.git")

def prepare_deploy():
    test()
    commit()
    push()