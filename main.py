from dao.dao import Dao
from ui.ui import UI
from controller.controller import Controller

def main():
    ui = UI()
    dao = Dao()
    controller = Controller(ui, dao)

    # dao = Dao()
    # dao.load_file()

if __name__ == '__main__':
    main()



'''
$python main.py
What would you like to do:
(1) List statistics
(2) Display 3 cities with longest names
(3) Display county's name with the largest number of communities
(4) Display locations, that belong to more than one category
(5) Advanced search
(0) Exit program
Option: 1
(https://classroom.github.com/assignment-invitations/7f139263ffbc91cfaecbea2b27a320ac)/---------------------------------\
|
MAŁOPOLSKIE
|
|-----+---------------------------|
|
1 | wojewódźtwo
|
|-----+---------------------------|
|
22 | powiaty
|
|-----+---------------------------|
|
14 | gmina miejska
|
|-----+---------------------------|
| 122 | gmina wiejska
|
|-----+---------------------------|
|
46 | gmina miejsko-wiejska
|
|-----+---------------------------|
|
46 | obszar wiejski
|
|-----+---------------------------|
|
46 | miasto
|
|-----+---------------------------|
|
3 | miasto na prawach powiatu |
|-----+---------------------------|
|
4 | delegatura
|
\---------------------------------/
Option:
5
Searching for: Nowy
Found 7 location(s):
/------------------------------------------\
| LOCATION
| TYPE
|
|--------------+---------------------------|
| Nowy Sącz | gmina miejska
|
| Nowy Sącz | miasto na prawach powiatu |
| Nowy Targ | gmina miejska
|
| Nowy Targ | gmina wiejska
|
| Nowy Wiśnicz | gmina miejsko-wiejska |
| Nowy Wiśnicz | miasto |
| Nowy Wiśnicz | obszar wiejski |\------------------------------------------/
(Please notice, that locations are sorted in ascending order, and 
types are also sorted ascending within the same location)'''