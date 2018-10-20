import features

if __name__ == '__main__':
    season_data_dict = {"1": "RLCS Data/RLCS1_PLAYER_STATS_LAN_checked.csv"}
    season_data_dict["2"] = "RLCS Data/RLCS2_PLAYER_STATS_LAN_checked.csv"
    season_data_dict["3"] = "RLCS Data/RLCS3_PLAYER_STATS_LAN_checked.csv"
    season_data_dict["4"] = "RLCS Data/RLCS4_PLAYER_STATS_LAN_checked.csv"
    season_data_dict["5"] = "RLCS Data/RLCS5_PLAYER_STATS_LAN_checked.csv"
    features.merge_raw_per_game_data(
        season_data_dict, "RLCS Data/LAN_player_stats.csv")
