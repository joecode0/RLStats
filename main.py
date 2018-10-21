import features
import player_positions
import data_validation

player_stats = "RLCS_Data/LAN_player_stats.csv"
if __name__ == '__main__':
    player_positions.plot_best_LAN_finishers(player_stats, 4)
