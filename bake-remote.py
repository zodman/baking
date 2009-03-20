import commands, sys, time
import pynotify
import re
import enums


cmd =  { 'where': enums.where ,'context': enums.context }
reps=sys.argv[1:]
recipe=""

for r in reps:
    recipe += "%s{x86} %s{x86_64}" % ( r, r)

cmd["recipes"] = recipe
enums.notify("Mooking", ",".join(reps))
result = commands.getoutput( "%(where)s build --quiet --no-watch  --context \"%(context)s\" %(recipes)s" %  cmd )
#result= 239

enums.notify("Packages Queue", ",".join(reps) )
cmd["result"] = result
enums.notify("Job: %s" % result,",".join(reps))
old_state = ""
state=""
while True:
    old_state = state
    if "Built" in state:
        commands.getoutput("%s commit %s"%( enums.where, job) )
        enums.notify("Commit Package", "%s" % ",".join(reps))

    query = commands.getoutput("%(where)s q %(result)s " % cmd)
    job, state, timeago = enums.get_info(query)
    enums.notify("%s %s"% ( state, ",".join(reps)) , "Job: %s - %s    (%s)"%( job, state, timeago.lstrip()) )
    if old_state != state:
        print "status: %s" % state
    if "Committed" in state or "Failed" in state :
        print "exiting ......"
        enums.notify("%s" % state, "%s"%  ",".join(reps) )
        sys.exit(0)
    time.sleep(enums.TIME)

    

