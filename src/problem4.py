#  Stacked chart of matches played by team by season
# Plot a stacked bar chart of ...

#     number of games played
#     by team
#     by season

# {'id': '634', 'season': '2016', 'city': 'Delhi', 'date': '2016-05-25', 'team1': 'Sunrisers Hyderabad', 'team2': 'Kolkata Knight Riders', 'toss_winner': 'Kolkata Knight Riders', 'toss_decision': 'field', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '22', 'win_by_wickets': '0', 'player_of_match': 'MC Henriques', 'venue': 'Feroz Shah Kotla', 'umpire1': 'M Erasmus', 'umpire2': 'C Shamshuddin', 'umpire3': ''}
# {'id': '635', 'season': '2016', 'city': 'Delhi', 'date': '2016-05-27', 'team1': 'Gujarat Lions', 'team2': 'Sunrisers Hyderabad', 'toss_winner': 'Sunrisers Hyderabad', 'toss_decision': 'field', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '0', 'win_by_wickets': '4', 'player_of_match': 'DA Warner', 'venue': 'Feroz Shah Kotla', 'umpire1': 'M Erasmus', 'umpire2': 'CK Nandan', 'umpire3': ''}
# {'id': '636', 'season': '2016', 'city': 'Bangalore', 'date': '2016-05-29', 'team1': 'Sunrisers Hyderabad', 'team2': 'Royal Challengers Bangalore', 'toss_winner': 'Sunrisers Hyderabad', 'toss_decision': 'bat', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '8', 'win_by_wickets': '0', 'player_of_match': 'BCJ Cutting', 'venue': 'M Chinnaswamy Stadium', 'umpire1': 'HDPK Dharmasena', 'umpire2': 'BNJ Oxenford', 'umpire3': ''}

import csv
import matplotlib.pyplot as plt 

def get_read_the_file_matches(path):
    delivery_file = open('ipl_data/matches.csv', mode='r')
    reader1 = csv.DictReader(delivery_file)
    return reader1

def get_season_and_each_team_matches(read_the_file_matches):
    season_team_matches = {}
    for each_match in read_the_file_matches:
        season = each_match['season']
        team1 = each_match['team1']
        team2 = each_match['team2']
        if season not in season_team_matches:
            season_team_matches[season] = {}
        if team1 not in season_team_matches[season]:
            season_team_matches[season][team1] = 0
        if team2 not in season_team_matches[season]:
            season_team_matches[season][team2] = 0
        season_team_matches[season][team1] += 1
        season_team_matches[season][team2] += 1
    return season_team_matches

def get_sort_season_and_each_team_matches(season_team_matches):
    sorted_data = {key: season_team_matches[key] for key in sorted(season_team_matches.keys())}
    return sorted_data

def get_sorted_years(sort_season_and_each_team_matches):
    sorted_data = sort_season_and_each_team_matches
    return list(sorted_data.keys())

def get_all_teams(sort_season_and_each_team_matches,sorted_years):
    all_teams = set()
    for season in sorted_years:
        all_teams.update(sort_season_and_each_team_matches[season].keys())
    return all_teams


def get_team_matches_each_year(sort_season_and_each_team_matches,sorted_years,all_teams):
    team_matches_each_year = {}
    for team in all_teams:
        team_matches_each_year[team] = [0] * len(sorted_years)

    for curr_index, year in enumerate(sorted_years):
        for team, no_of_matches_played in sort_season_and_each_team_matches[year].items():
            team_matches_each_year[team][curr_index] = no_of_matches_played
    return team_matches_each_year

def plot_matches_played_by_each_team_by_each_season(sorted_years,team_matches_each_year):

    bottom_stack = [0] * len(sorted_years)

    for team, team_values in team_matches_each_year.items():
        plt.bar(sorted_years, team_values, bottom=bottom_stack, label=team, width=0.8)
        bottom_stack = [bottom_stack[i] + team_values[i] for i in range(len(team_values))]

    plt.xlabel('Year')
    plt.ylabel('Matches Played')
    plt.title('Stacked Bar Graph of Teams over the Years')
    plt.xticks(rotation=45)
    plt.legend(title="Teams", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def main(): 
        read_the_file_matches=get_read_the_file_matches('ipl_data/matches.csv') 
        season_team_matches=get_season_and_each_team_matches(read_the_file_matches)
        sort_season_and_each_team_matches=get_sort_season_and_each_team_matches(season_team_matches)

        sorted_years=get_sorted_years(sort_season_and_each_team_matches)
        all_teams=get_all_teams(sort_season_and_each_team_matches,sorted_years) 

        team_matches_each_year=get_team_matches_each_year(sort_season_and_each_team_matches,sorted_years,all_teams) 

        plot_matches_played_by_each_team_by_each_season(sorted_years,team_matches_each_year) 
main()





