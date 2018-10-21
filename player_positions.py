import pandas as pd


def plot_best_LAN_finishers(filename, reqNoOfLANS):
    best_players_dict = get_best_LAN_players(filename, reqNoOfLANS)
    print(best_players_dict)


def get_best_LAN_players(filename, reqNoOfLANS):
    players_position_dict = get_player_LAN_positions_dict(filename)
    best_players_dict = {}
    for player in players_position_dict.keys():
        position_dict = players_position_dict.get(player)
        if len(position_dict.keys()) >= reqNoOfLANS:
            best_players_dict[player] = position_dict
    return best_players_dict


def get_player_LAN_positions_dict(filename):
    positions_dict = {}
    df = pd.read_csv(filename)
    for player in df['Player'].tolist():
        positions_dict[str(player)] = {}
    for i in range(len(df)):
        row_data = df.iloc[i]
        player = row_data['Player']
        season = row_data['Season']
        position = int(row_data['Position'])
        player_dict = positions_dict.get(player)
        player_dict[season] = position
    return positions_dict
