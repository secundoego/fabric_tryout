from __future__ import with_statement # to use Python's with:
from fabric.api import local 
from fabric.api import settings, abort
from fabric.contrib.console import confirm
from fabric.operations import run
from fabric.operations import put
from fabric.context_managers import cd

# Call code: 
#	>fab hello:name=Koen
#	>fab hello:Koen
# name is arg to function hello()
def hello(name): 
	print("Hello %s" % name)
	
def test():
	local("ls -al")
	
# Add and local changes to local repository
def add():
	local("git add -p")
	
def commit():
	local("git commit")

# Push local changes to remote GitHub
def push():
	local("git push fabric_tryout")

# Pull remote repository from GitHub to local system	
def pull():
	local("git pull fabric_tryout master")
	
def deploy():
	code_dir = '/src'
	with cd(code_dir):
		#local("ls -al")
		run("git pull fabric_tryout master")
		#run("touch app.wsgi")

def deploy_remote():
	fabric.operations.put("/src/*", remote_path, use_sudo=False, mirror_local_mode=False, mode=None)