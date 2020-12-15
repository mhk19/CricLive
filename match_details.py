def get_match_info(api_instance, match_id):
    match_info = api_instance.matchinfo(match_id)
    return match_info

def get_series_name(match_info):
    return match_info['srs']

def get_team_names(match_info):
    return [match_info['team1']['name'], match_info['team2']['name']]

def get_venue_name(match_info):
    return match_info['venue_name']

def get_venue_location(match_info):
    return match_info['venue_location']

def get_umpire_name(match_info):
    return match_info['official']['umpire1']['name']

def get_live_score(api_instance, match_id):
    live_score = api_instance.livescore(match_id)
    return live_score

def get_total_runs_of_batting_team(livescore):
    return livescore['batting']['score'][0]['runs']

def get_total_wickets_of_batting_team(livescore):
    return livescore['batting']['score'][0]['wickets']

def get_total_overs(livescore):
    return livescore['batting']['score'][0]['overs']

def get_inning_number(livescore):
    return livescore['batting']['score'][0]['inning_num']

def get_batting_team_name(livescore):
    return livescore['batting']['team']

def get_bowling_team_name(livescore):
    return livescore['bowling']['team']

def get_batsman(livescore):
    return livescore['batting']['batsman']

def get_bowler(livescore):
    return livescore['bowling']['bowler'][0]

def get_commentary(api_instance, match_id):
    comm = api_instance.commentary(match_id)
    return comm['commentary']

def striker(comm):
    name = comm.split(" to ", 1)[1].split()[0]
    print(name)
    return name
