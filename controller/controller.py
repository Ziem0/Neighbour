from model.voivodeship import Voivodeship
from model.county import County
from model.community import Community
from model.statistic import Statistic
import os, sys

class Controller:

    def __init__(self, ui, dao):
        self.ui = ui
        self.dao = dao
        self.dao.load_file()
        self.start_controller()

    def start_controller(self):
        self.start = 1
        while self.start:
            self.ui.print(self.ui.create_menu(self.ui.menu ,self.ui.title))
            self.user = self.ui.user_choice(self.ui.menu)
            self.handle_menu()

    def handle_menu(self):
        if self.user == 1:
            self.display_stats()
        elif self.user == 2:
            self.show_longest_name()
        elif self.user == 3:
            self.display_biggest_county()
        elif self.user == 4:
            self.check_same_locations()
        elif self.user == 5:
            self.advanced_search()
        elif self.user == 0:
            sys.exit('bye')

    @staticmethod
    def calculate_stats():
        for unit in Statistic.all_units:
            for type, amount in Statistic.statistic.items():
                if unit.type == type:
                    Statistic.statistic[type] += 1

    def display_stats(self):
        self.calculate_stats()
        self.ui.print(self.ui.show_stats(Statistic.statistic))

    def show_longest_name(self):
        cities = {city.name:len(city.name) for city in Statistic.all_units if city.type == 'miasto'}
        cities = sorted(cities, key=lambda value:cities[value], reverse = True)
        self.ui.print(self.ui.create_menu(cities[0:3], self.ui.title1))

    def display_biggest_county(self):
        self.ui.print(max(County.all_counties, key=lambda county:len(county.communities)).name)

    def check_same_locations(self):
        locations = {}
        for location in Statistic.all_units:
            if location.name not in locations:
                locations[location.name] = 1
            else:
                locations[location.name] += 1

        locations = {k:v for k,v in locations.items() if v > 1}
        self.ui.print(self.ui.show_stats(locations))

    def advanced_search(self):
        user = self.ui.search_input()
        search_list = sorted([unit.name+'--->'+unit.type for unit in Statistic.all_units if user in unit.name])
        self.ui.print(self.ui.create_menu(search_list, self.ui.title2))