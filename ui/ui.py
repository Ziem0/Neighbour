import os, sys

class UI:

    menu = ['(1) List statistics',
            '(2) Display 3 cities with longest names',
            '(3) Display county\'s name with the largest number of communities',
            '(4) Display locations, that belong to more than one category',
            '(5) Advanced search',
            '(0) Exit program']
    title = '\nWhat would you like to do?\n\n'
    title1 = '\nCities with the longest name:\n\n'
    title2 = '\nFound:\n\n'

    @staticmethod
    def print(it):
        print(it)

    @staticmethod
    def pause():
        input('Press Enter to continue..')

    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def create_menu(menu, title):
        for option in menu:
            title += "{}\n".format(option)
        return title

    @staticmethod
    def user_choice(menu):
        user = -1
        while user > len(menu)-1 or user < 0:
            try:
                user = int(input('Choose option: '))
            except ValueError:
                print('Invalid input. Only number allowed!')
        return user

    @staticmethod
    def show_stats(stats):
        out = '\n'
        for k,v in stats.items():
            out += "type:{} amount:{}\n".format(k, v)
        return out

    @staticmethod
    def search_input():
        user = input('Type letter(s): ')
        return user