import features
import player_positions
import data_validation

player_stats = "RLCS_Data/LAN_player_stats.csv"
if __name__ == '__main__':
    data_validation.check_team_names_consistent(player_stats)
