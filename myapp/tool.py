
logdebug = False
def logt(tag,msg):
    if logdebug:
        print("%s,--%s" % (tag,msg))

def log(msg):
    if logdebug:
        print("%s" % msg)
