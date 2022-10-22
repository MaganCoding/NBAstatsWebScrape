import pandas as pd
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.nba.com/stats")

nba_web_page = response.text
soup = BeautifulSoup(nba_web_page, "html.parser")


data = []

all_players = soup.select(selector=".LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
for player in all_players:
    if len(data) == 0:
        data.append("POINTS")
    data.append(player.text)
    if len(data) == 11:
        data.append("REBOUNDS")
    elif len(data) == 22:
        data.append("ASSISTS")
    elif len(data) == 33:
        data.append("BLOCKS")
    elif len(data) == 44:
        data.append("STEALS")
    elif len(data) == 55:
        data.append("TURNOVERS")
    elif len(data) == 66:
        data.append("THREE POINTERS MADE")
    elif len(data) == 77:
        data.append("FREE THROWS MADE")
    elif len(data) == 88:
        data.append("FANTASY POINTS")
    if len(data) == 99:
        break

points_list = data[0:11]
rebound_list = data[11:22]
assists_list = data[22:33]
blocks_list = data[33:44]
steals_list = data[44:55]
to_list = data[55:66]
threes_list = data[66:77]
frees_list = data[77:88]
fantasy_list = data[88:99]
# print(data)


points_str = ' '.join([str(elem) for elem in points_list])
rebounds_str = ' '.join([str(elem) for elem in rebound_list])
assists_str = ' '.join([str(elem) for elem in assists_list])
blocks_str = ' '.join([str(elem) for elem in blocks_list])
steals_str = ' '.join([str(elem) for elem in steals_list])
to_str = ' '.join([str(elem) for elem in to_list])
threes_str = ' '.join([str(elem) for elem in threes_list])
frees_str = ' '.join([str(elem) for elem in frees_list])
fantasy_str = ' '.join([str(elem) for elem in fantasy_list])

# print(f"{points_list}\n{rebound_list}\n{assists_list}\n{blocks_list}\n{to_list}\n{threes_list}\n{frees_list}\n{fantasy_list}")


with open("nba_stats.csv", "w") as file:
    file.write(f"{points_str}\n{rebounds_str}\n{assists_str}\n{blocks_str}\n{steals_str}\n{to_str}\n{threes_str}\n{frees_str}\n{fantasy_str}")


