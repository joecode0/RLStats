import pandas as pd


def check_team_names_consistent(filename):
    df = pd.read_csv(filename)
    teamname_set = sorted(set(df['Team'].tolist()))
    print(teamname_set)

    original_col_order = list(df.columns.values)
    df['Team'] = df.apply(fix_team_names, axis=1)
    teamname_set = sorted(set(df['Team'].tolist()))
    print(teamname_set)
    df = df[original_col_order]
    df.to_csv(filename, index=False)


def check_player_names_consistent(filename):
    # By printing out a set of players SORTED, can easily see if players have the wrong name in some places
    df = pd.read_csv(filename)
    players_set = sorted(set(df['Player'].tolist()))
    print(players_set)

    # This pointed out that the names "KUXIR" and "KUXIR97" has been used interchangeably, and therefore would cause plotting bugs. Fix below
    original_col_order = list(df.columns.values)
    df['Player'] = df.apply(fix_player_names, axis=1)
    players_set = sorted(set(df['Player'].tolist()))
    print(players_set)
    df = df[original_col_order]
    df.to_csv(filename, index=False)


def fix_team_names(row):
    team = row['Team']
    if team == 'MOCK-IT EU ':
        return "MOCK-IT EU"
    elif team == "COMPLEXITY GAMING":
        return "COMPLEXITY"
    elif team == "TEAM DIGNITAS":
        return "DIGNITAS"
    elif team == "TEAM ENVYUS":
        return "ENVYUS"
    elif team == "TEAM VITALITY":
        return "RENAULT VITALITY"
    elif team == "NRG ESPORTS":
        return "NRG"
    elif team == "PSG ESPORTS":
        return "PSG"
    elif team == "SELFLESS GAMING":
        return "SELFLESS"
    elif team == "THE LEFTOVERS":
        return "LEFTOVERS"
    else:
        return team


def fix_player_names(row):
    player = row['Player']
    if player == "KUXIR":
        return "KUXIR97"
    else:
        return player
