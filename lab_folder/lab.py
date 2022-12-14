class Lab():

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        # result = f"{self.name:>20s}{self.cost:>15d}"
        result = "{0:20}{1:8}".format(self.name, self.cost)
        return result

    def formatLabInfo(self):
        added = f"{self.name}_{self.cost}\n"
        return added