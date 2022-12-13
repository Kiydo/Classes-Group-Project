class Facility:
    nbr_of_facilities = 0

    def __init__(self, facility):
        self.facility = facility
    
    def __str__(self):
        result = f"{self.facility:<10}"
        # print(self)
        return result

    def formatFacilityInfo(self):
        added = f"{self.facility}\n"
        return added


        