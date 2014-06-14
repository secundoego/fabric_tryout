from fabric.api import local, env 
from fabric.operations import run, put
from fabric.context_managers import cd

# When using an argument for a fabfile 
#	>fab hello:name=Koen
#	>fab hello:Koen
# name is arg to function hello()
def hello(name): 
	print("Hello %s" % name)

################
# Git commands #
################

# Add all local changes to local repository
#	-all: also handles removals
def add():
	local("git add --all")

# Commit local changes to local repository
def commit():
	local("git commit")

# Push local changes to remote GitHub
def push():
	local("git push fabric_tryout")

# Pull remote repository from GitHub to local system	
def pull():
	local("git pull fabric_tryout master")


###################
# Deploy commands #
###################
	
# Deploy application to remote server
# 

# user server ssh-port to deploy to
env.hosts = ['pi@10.0.0.18:2222']

# Deploy from local_path to remote_path
def deploy_remote():
	put("./src/*", "~/fabric_tryout/")
	
	