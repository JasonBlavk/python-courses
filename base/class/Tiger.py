from Animal import Animal


class Tiger(Animal):

    def __init__(self, ani_type):
        Animal.__init__(self, ani_type)
        print "init Tiger"

    def eat(self):
        print "eat something"
