##Added possibility for slash commands, test

from bot import *
from LOL_sort_games_wr import *
from responses import *

class author:
    
    def __init__(self, name, nick = None):
        self.author = name
        self.nick = nick

    def author_return(self):
        return self.author

def test_sort():
    Champion1 = Champion('Vex', 20, 10)
    Champion2 = Champion('Ashe', 92, 68)
    Champion3 = Champion('Azir', 33, 29)
    Champion4 = Champion('Karma', 54, 19)
    Champion5 = Champion('Darius', 12, 10)

    Champion1.calc_win_rate()
    Champion2.calc_win_rate()
    Champion3.calc_win_rate()
    Champion4.calc_win_rate()
    Champion5.calc_win_rate()

    Champions = [Champion1, Champion2, Champion3, Champion4, Champion5]
    bubble_sort(Champions)
    print('Champion sorted by win rate\n')
    for i in range(len(Champions)):
        print(f'{Champions[i].champ_name}, win rate: {Champions[i].win_rate}%')
        
    print()


def test_sort2():
    Champion1 = Champion('Lux')
    Champion2 = Champion('Valdimir', 1000, 1)
    Champion3 = Champion('Volibear', 123, 123)
    Champion4 = Champion('Sylas', 98, 26)
    Champion5 = Champion('Orianna', 2122, 1428)

    Champion1.calc_win_rate()
    Champion2.calc_win_rate()
    Champion3.calc_win_rate()
    Champion4.calc_win_rate()
    Champion5.calc_win_rate()

    Champions = [Champion1, Champion2, Champion3, Champion4, Champion5]
    bubble_sort(Champions)

    print('Champion sorted by win rate\n')
    for i in range(len(Champions)):
        print(f'{Champions[i].champ_name}, win rate: {Champions[i].win_rate}%')
    print()

def test_sort3():
    Champion1 = Champion('Yone', 1245, 1000)
    Champion2 = Champion('Sivir', 100, 100)
    Champion3 = Champion('Zeri', 34, 23)
    Champion4 = Champion('Tristana', 124512, 5200)
    Champion5 = Champion('Varus', 120, 119)

    Champion1.calc_win_rate()
    Champion2.calc_win_rate()
    Champion3.calc_win_rate()
    Champion4.calc_win_rate()
    Champion5.calc_win_rate()

    Champions = [Champion1, Champion2, Champion3, Champion4, Champion5]
    bubble_sort(Champions)

    print('Champion sorted by win rate\n')
    for i in range(len(Champions)):
        print(f'{Champions[i].champ_name}, win rate: {Champions[i].win_rate}%')
    print()

def test_roll():
    roll1 = roll(1, 10)
    roll2 = roll(3, 9)
    roll3 = roll(1, 7)
    roll4 = roll(12, 90)

    print(roll1)
    print()

    print(roll2)
    print()

    print(roll3)
    print()

    print(roll4)
    print()

def coin_flip():
    flip1 = coinflip()
    flip2 = coinflip()
    flip3 = coinflip()
    flip4 = coinflip()

    print(flip1[0])
    print()

    print(flip2[0])
    print()

    print(flip3[0])
    print()

    print(flip4[0])
    print()

def test_spin_wheel():
    Soewon = author("Soewon")
    Soewon.nick = "SeowonNick"

    Abhinav = author("Abhinav")
    Abhinav.nick = "Abhi"

    spin1 = spin_wheel(['Renekton','Sivir', 'Ashe'], Soewon)
    spin2 = spin_wheel(['Jhin','Zoe', 'Varus'], Abhinav)
    print(spin1)
    print(spin2)


test_sort()
test_sort2()
test_sort3()
test_roll()
coin_flip()
test_spin_wheel()
