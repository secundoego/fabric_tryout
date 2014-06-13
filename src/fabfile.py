from fabric.api import local

# Call code: 
#	>fab hello:name=Koen
#	>fab hello:Koen
# name is arg to function hello()
def hello(name): 
	print("Hello %s" % name)
	
def test():
	local("ls -al")
	
def commit():
	local("git add -p && git commit")
