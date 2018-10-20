import pandas as pd


def merge_raw_per_game_data(season_data_dict, output_filename):
    df = pd.DataFrame()
    for k in season_data_dict.keys():
        df_data = add_per_game_columns(season_data_dict.get(k), k)
        df = pd.concat([df, df_data], axis=0)
    df.to_csv(output_filename, index=False)


def add_per_game_columns(filename, k):
    df = pd.read_csv(filename)
    df['Season'] = ["RLCS" + str(k)]*len(df)
    df['Total Games'] = df['Games Played']
    df['Total Wins'] = df.apply(get_total_wins, axis=1)
    df['Total Score'] = df['Score']
    df['Total Goals'] = df['Goals']
    df['Total Assists'] = df['Assists']
    df['Total Saves'] = df['Saves']
    df['Total Shots'] = df['Shots']
    df['Prize'] = df['Prize$']
    df['Team'] = [x.upper() for x in df['Team'].tolist()]
    df['Player'] = [x.upper() for x in df['Player'].tolist()]

    df.drop(['Games Played', 'Score', 'Goals', 'Assists',
             'Saves', 'Shots', 'Prize$'], inplace=True, axis=1)
    df = df[['Season', 'Position', 'Prize', 'Team', 'Player', 'Total Games', 'Total Wins',
             'Total Score', 'Total Goals', 'Total Assists', 'Total Saves', 'Total Shots', 'Win%']]

    df['Score per game'] = df.apply(
        calc_stat_per_game, args=('Total Score',), axis=1)
    df['Goals per game'] = df.apply(
        calc_stat_per_game, args=('Total Goals',), axis=1)
    df['Assists per game'] = df.apply(
        calc_stat_per_game, args=('Total Assists',), axis=1)
    df['Saves per game'] = df.apply(
        calc_stat_per_game, args=('Total Saves',), axis=1)
    df['Shots per game'] = df.apply(
        calc_stat_per_game, args=('Total Shots',), axis=1)

    df.sort_values(['Season', 'Position', 'Team', 'Player'],
                   inplace=True, axis=0)
    return df


def get_total_wins(row):
    return int(round((row['Total Games']*row['Win%'])/100, 0))


def calc_stat_per_game(row, stat):
    total_games = row['Total Games']
    stat_total = row[stat]
    stat_per_game = round(stat_total/total_games, 2)
    return stat_per_game
