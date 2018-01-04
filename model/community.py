from model.statistic import Statistic

class Community(Statistic):

    all_communities = []

    def __init__(self, id_com, *args):
        self.id_com = id_com
        super().__init__(*args)
        Community.all_communities.append(self)

