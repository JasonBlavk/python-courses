class Animal:
    """Animal base class"""

    type = ""

    def __init__(self, ani_type):
        self.type = ani_type
        print "Animal init"
