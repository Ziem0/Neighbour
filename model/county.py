from model.statistic import Statistic

class County(Statistic):

    all_counties = []

    def __init__(self, *args):
        super().__init__(*args)
        self.communities = []
        County.all_counties.append(self)

    def add_community(self, community):
        self.communities.append(community)

    