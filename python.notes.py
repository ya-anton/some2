class some_common(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class some_certain(some_common):

    def __init__(self, name, feature1):
        some_common.__init__(self, name, "hello")
        self.feature1 = feature1

    def getFeature1(self):
        return self.feature1

>>> cl1 = some_common("someone", "special")
>>> cl2 = some_certain("someone", True)

>>> isinstance(cl1, some_common)
True




