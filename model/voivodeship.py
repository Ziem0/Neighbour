from model.statistic import Statistic

class Voivodeship(Statistic):

    all_voivodeship = []

    def __init__(self, *args):
        super().__init__(*args)
        self.counties = []

        Voivodeship.all_voivodeship.append(self)

    def add_county(self, county):
        self.counties.append(county)