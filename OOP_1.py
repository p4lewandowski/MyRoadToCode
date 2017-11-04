class Houses:

    NoOfHouses = 0

    def __init__(self,category):
        self.category=category
        print("(Initializing {})".format(self.category))
        Houses.NoOfHouses +=1

    def demolish(self):
        Houses.NoOfHouses -= 1
        print('there are still {:d} houses of category '.format(Houses.NoOfHouses) + str(self.category))

    @classmethod
    def HowManyHouses(cls):
        print('there are still ' + str(cls.NoOfHouses) + ' houses')

house1=Houses('detached')
Houses.HowManyHouses()
house2=Houses('detached')
Houses.HowManyHouses()
house3=Houses('twin')
Houses.HowManyHouses()
house1.demolish()
Houses.HowManyHouses()

print (house1.category)
print (house3.category)

