import pynotify, sys, re
if not pynotify.init("Basic"):
    sys.exit(1)



where = "ssh fdev.foresightlinux.org rmake"
context="fl:2-devel"
TIME = 60
REGEX="(?P<job>\w*)\s+(?P<state>\w*)\s+(?P<time>\d*\s\w*\s\w*)\s+"

def get_info(query):
    query = query.replace("\n","")
    obj = re.compile(REGEX,  re.IGNORECASE| re.DOTALL)
    return obj.search(query).groups()

def notify( summary, desc ):
    print "%s \n %s \n=======" % ( summary, desc)
    pynotify.Notification(summary, desc).show()
