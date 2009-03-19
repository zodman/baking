import pynotify
import commands, sys
import enums

if not pynotify.init("Basic"):
    sys.exit(1)


job = sys.argv[1]

query =  commands.getoutput("%s q  %s" %(enums.where, job))

print query
