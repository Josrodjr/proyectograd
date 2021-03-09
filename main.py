

from steamapi import core, user
import pandas as pd

core.APIConnection(api_key="", validate_key=True)
steam_user = 0

try:
    # query the username to the api
    steam_user = user.SteamUser(userurl="alhvi")

    # extract the data
    name = steam_user.name
    real_name = steam_user.real_name
    country_code = steam_user.country_code
    level = steam_user.level
    xp = steam_user.xp
    bans = steam_user.number_of_game_bans
    
    # parseable data
    friends = steam_user.friends
    games = steam_user.games
    recently_played_games = steam_user.recently_played
    owned_games = steam_user.owned_games
    badges = steam_user.badges

    # print(name, real_name, country_code, level, xp, bans, friends, games, recently_played_games, owned_games, badges)
    
except Exception as error:
    print("Error: " + error)


