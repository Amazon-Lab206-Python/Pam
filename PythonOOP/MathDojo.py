class MathDojo(object):
    def __init__(self, *args):
        self.result = 0
    def add(self, *args):
        for val in args:
            if type(val) == list or type(val) == tuple:
                for data in val:
                    self.result += data
            else:
                self.result += val
        print self.result
        return self
    def subtract(self, *args):
        for val in args:
            if type(val) == list or type(val) == tuple:
                for data in val:
                    self.result -= data
            else:
                self.result -= val
        print self.result
        return self

md1 = MathDojo()

md1.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
