import requests
import os
from dotenv import load_dotenv

class Champion:

    def __init__(self, champ_name, games_played = 0, wins = 0):
        self.games_played = games_played
        self.wins = wins
        self.champ_name = champ_name
        self.win_rate = None
    
    def calc_win_rate(self):
        if self.games_played > 0:
            self.win_rate = (self.wins / self.games_played) * 100
            self.win_rate = round(self.win_rate)
        else:
            self.win_rate = 0

def configure():
    load_dotenv()

def bubble_sort(champions):

    n = len(champions)
    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):

            if champions[j].win_rate < champions[j+1].win_rate:

                champions[j], champions[j+1] = champions[j+1], champions[j]
                swapped = True

        if not swapped:
            break

def get_puuid(region, game_name, id, api_key):

    puuid_url = (
        "https://" +
        region +
        ".api.riotgames.com/riot/account/v1/accounts/by-riot-id/" +
        game_name +
        "/" +
        id +
        "?api_key=" +
        api_key
    )

    resp = requests.get(puuid_url)
    data = resp.json()
    puuid = data["puuid"]

    return puuid

def get_match_list(region, puuid, api_key):

    match_list_url = (
        "https://" +
        region +
        ".api.riotgames.com/lol/match/v5/matches/by-puuid/" +
        puuid +
        "/ids?start=0&count=20" +
        "&api_key=" +
        api_key
    )

    resp = requests.get(match_list_url)
    data = resp.json()

    return(data)

def get_champ_win_loss_data(region, puuid, api_key, game_id):

    champ_win_loss_data = []

    specific_match_url = (
        "https://" +
        region +
        ".api.riotgames.com/lol/match/v5/matches/" +
        game_id +
        "?api_key=" +
        api_key
    )

    resp = requests.get(specific_match_url)
    data = resp.json()

    player_index = data["metadata"]["participants"].index(puuid)

    our_player_info = data["info"]["participants"][player_index]

    champion_played = our_player_info["championName"]

    champ_win_loss_data.append(champion_played)

    w_or_l = our_player_info["win"]

    champ_win_loss_data.append(w_or_l)

    return champ_win_loss_data

def get_match_data(user_name, tag, region, api_key):

    puuid = get_puuid(region, user_name, tag, api_key)
    match_list = get_match_list(region, puuid, api_key)

    all_match_data = []

    #Adding all data to all_match_data
    for i in range(len(match_list)):
        
        game_win_loss_champ = get_champ_win_loss_data(region, puuid, api_key, match_list[i])

        all_match_data.append(game_win_loss_champ)
    
    return all_match_data

def calculate_win_rates(match_data):

    champs_stats = {}

    # Count games played and wins for each champion
    for match in match_data:
        champ_name, won = match
        if champ_name not in champs_stats:
            champs_stats[champ_name] = {'games_played': 0, 'wins': 0}
        champs_stats[champ_name]['games_played'] += 1
        if won:
            champs_stats[champ_name]['wins'] += 1

    champs_in_list = []

    # Create Champion objects and calculate win rates
    for champ_name, stats in champs_stats.items():
        champ = Champion(champ_name, stats['games_played'], stats['wins'])
        champ.calc_win_rate()
        champs_in_list.append(champ)

    return champs_in_list

def main(user_name, tag):

    region = "americas"
    api_key = os.getenv("riot_api_token")

    player = get_match_data(user_name, tag, region, api_key)
    win_rates = calculate_win_rates(player)

    bubble_sort(win_rates)

    champ_list = []
    win_rate_percent = []
    games_played = []

    for champ in win_rates:
        champ_list.append(champ.champ_name)
        win_rate_percent.append(champ.win_rate)
        games_played.append(champ.games_played)

    for i in range(len(win_rate_percent)):
        win_rate_percent[i] = str(win_rate_percent[i]) + "%"
        games_played[i] = str(games_played[i])

    champ_list = "\n".join(champ_list)
    win_rate_percent = "\n".join(win_rate_percent)
    games_played = "\n".join(games_played)

    return champ_list, win_rate_percent, games_played