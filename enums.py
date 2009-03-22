import pynotify, sys, re, os
if not pynotify.init("Basic"):
    sys.exit(1)

import gtk
icon =gtk.gdk.pixbuf_new_from_file(
    os.path.abspath(os.path.dirname(__file__))+'/64.png'
)
where = "ssh fdev.foresightlinux.org rmake"
context="fl:2-devel"
TIME = 30
REGEX="(?P<job>\w*)\s+(?P<state>\w*)\s+(?P<time>\d*\s\w*\s\w*)\s+"

def get_info(query):
    query = query.replace("\n","")
    obj = re.compile(REGEX,  re.IGNORECASE| re.DOTALL)
    if obj:
        return obj.search(query).groups()
    else:
        print "Some error passed"
        sys.exit(1)

def notify( summary, desc , warning = True):
    print "%s - %s " % ( summary, desc)
    notify =pynotify.Notification(summary, desc)
    notify.set_icon_from_pixbuf(icon)
    notify.show()
