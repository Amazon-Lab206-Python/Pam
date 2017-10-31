myinfo = {
    "name": "Pam",
    "age": "32",
    "birthplace": "US",
    "language": "Unknown",
    }

def getinfo():
    for key in myinfo:
        print "My", key , "is", myinfo[key]


getinfo()