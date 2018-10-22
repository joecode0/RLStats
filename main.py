import features
import player_positions
import data_validation

player_stats = "RLCS_Data/LAN_player_stats.csv"
if __name__ == '__main__':
    f = player_positions.calculate_score_per_player(player_stats)
    print(f)
