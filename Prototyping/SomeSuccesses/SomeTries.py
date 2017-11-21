class bobobo:
    k=2
    def passdata(self):
        b =1
        return b

class dasd(bobobo):
    def __init__(self):
        super(self.__class__, self).__init__()
        a=bobobo
        c=a.passdata(self)
        print (c)

db=dasd()