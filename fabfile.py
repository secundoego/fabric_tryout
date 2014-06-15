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
remote_host = "10.0.0.18"
# remote_host = "192.168.2.4"
#  	remote_host = "81.68.58.163"
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

# fabric.contrib.project.rsync_project source definition
#	[https://github.com/fabric/fabric/blob/master/fabric/contrib/project.py} 
#
#	def rsync_project(
#    remote_dir,
#    local_dir=None,
#    exclude=(),
#    delete=False,
#    extra_opts='',
#    ssh_opts='',
#    capture=False,
#    upload=True,
#    default_opts='-pthrvz'
#	):

# The rsync_project() below will give
#	rsync --delete -pthrvz -EgolHDu --out-format="info - %i %B %12b %12l %M %f%L" --rsh='ssh  -p 2222 ' src/ pi@10.0.0.18:~/fabric_tryout
#		rsync					generate by fabric 
#		--delete 				added by programmer as: delete=True
#		-pthrvz 				added by fabric
#		-EgolHDu <etc>			added by programmer as: extra_opts=-EgolHDu --out-format="info - %i %B %12b %12l %M %f%L"
#		--rsh='ssh  -p 2222 '	added by Fabric using variable env.hosts
#		src/ 					added by programmer
#		pi@10.0.0.18:			added by Fabric using variable env.hosts
#		~/fabric_tryout			added by programmer
def deploy():
	local= "src/"
	remote = "~/fabric_tryout"
	opt = '-EgolHDu --out-format="info - %i %B %12b %12l %M %f%L"'
	rsync_project(remote, local, delete=True, extra_opts=opt)
	
	