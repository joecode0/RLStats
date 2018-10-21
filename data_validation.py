import pandas as pd


def check_player_names_consistent(filename):
    # By printing out a set of players SORTED, can easily see if players have the wrong name in some places
    df = pd.read_csv(filename)
    players_set = sorted(set(df['Player'].tolist()))
    print(players_set)

    # This pointed out that the names "KUXIR" and "KUXIR97" has been used interchangeably, and therefore would cause plotting bugs. Fix below
    original_col_order = list(df.columns.values)
    df['Player'] = df.apply(fix_player_names, axis=1)
    df = df[original_col_order]
    df.to_csv(filename, index=False)


def fix_player_names(row):
    player = row['Player']
    if player == "KUXIR":
        return "KUXIR97"
    else:
        return player
