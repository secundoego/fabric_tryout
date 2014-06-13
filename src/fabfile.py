from fabric.api import local

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
