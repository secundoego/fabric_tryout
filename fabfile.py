from fabric.api import local, env 
from fabric.operations import run, put
from fabric.context_managers import cd
from fabric.contrib.project import rsync_project

'''
fabfile.py

Functions
- Git local and remote actions
- Deploy application to remote server

Input:
Output: 

@author: Koen Warner (koen)
@version:  v0.1,  14 jun. 2014
(c) 2014 Koen Warner
'''

####################
# Global variables #
####################

project_name ="fabric_tryout"

remote_user = "pi"
# remote_host = "10.0.0.18"
# remote_host = "192.168.2.4"
remote_host = "81.68.58.163"
remote_port = "2222"
#remote_port = "2226"
local_path = "./src/*"
remote_path = "~/fabric_tryout/"
env.hosts = ["%s@%s:%s" % (remote_user,  remote_host, remote_port)]


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
	print "Pushing %s to GitHub" % project_name
	local("git push %s" % project_name)

# Pull remote repository from GitHub to local system	
def pull():
	local("git pull %s" % project_name)


###################
# Deploy commands #
###################
	

# Deploy from local to remote server
# NB: the problem with put is that locally removed files are not removed remotely.
# Use rsync
def deploy():
	put("%s" % local_path, "%s" % remote_path)
#	rsync_project("~/fabric_tryout", "./src/")
	
	