from model.voivodeship import Voivodeship
from model.county import County
from model.community import Community
import csv
import os, sys

class Dao:

    @staticmethod
    def load_file():
        if not os.path.isfile('static/malopolska.csv'):
            raise FileNotFoundError
        else:
            with open('static/malopolska.csv', 'r') as csvfile:

                for row in csvfile:
                    row = row.strip()
                    row = row.split('\t')

                    if row[0].isdigit():
                        data = (row[4], row[5])
                        if not row[1]:
                            voivodeship = Voivodeship(row[0], *data)
                        elif not row[2]:
                            county = County(row[1], *data)                    
                            voivodeship.add_county(county)
                        elif row[3]:
                            community = Community(row[2], row[3], *data)
                            county.add_community(community)
                            

