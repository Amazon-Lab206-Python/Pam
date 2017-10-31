from datetime import datetime

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def get_queue_size(self):
        print len(self.calls)
        #return len(self.calls)

    def add(self,a_call):
        self.calls.append(a_call)
        self.queue_size += 1
        return self

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()

class Call(object):
    NUM_CALLS = 1
    def __init__(self, name, phone_num, reason):
        self.name = name
        self.phone_num = phone_num
        self.time = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display_info(self):
        print "***Info***"
        print self.name
        print self.phone_num
        print self.time
        print self.reason
        print "***End Info***"

        
cc1 = CallCenter()
c1 = Call("Pam", 912587109, "Because")
c2 = Call("Sam", 23262626, "no reason")
c3 = Call("Brad", 6586794467, "i need help")

cc1.add(c1).add(c2).add(c3).info()

