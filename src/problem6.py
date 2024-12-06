#  Number of matches won per team per year in IPL.    year is constant here.
# Plot a stacked bar chart. 

# {'id': '634', 'season': '2016', 'city': 'Delhi', 'date': '2016-05-25', 'team1': 'Sunrisers Hyderabad', 'team2': 'Kolkata Knight Riders', 'toss_winner': 'Kolkata Knight Riders', 'toss_decision': 'field', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '22', 'win_by_wickets': '0', 'player_of_match': 'MC Henriques', 'venue': 'Feroz Shah Kotla', 'umpire1': 'M Erasmus', 'umpire2': 'C Shamshuddin', 'umpire3': ''}

import csv
import matplotlib.pyplot as plt  
def read_matches_file():
    delivery_file = open('ipl_data/matches.csv', mode='r')
    reader = csv.DictReader(delivery_file)
    return reader

def get_how_many_won_by_each_team_by_season(data_of_the_file):
    season_team_winners={} 
    for each_row in data_of_the_file: 
        year=each_row['season'] 
        winning_team=each_row['winner']
        if year not in season_team_winners: 
            season_team_winners[year]={} 
        if winning_team not in season_team_winners[year]: 
            season_team_winners[year][winning_team]=0 
        season_team_winners[year][winning_team]+=1 
    return season_team_winners
# { '2017': {'Sunrisers Hyderabad': 14, 'Royal Challengers Bangalore': 13, 'Mumbai Indians': 17, 'Rising Pune Supergiant': 16, 'Gujarat Lions': 14, 'Kolkata Knight..} } 

def get_sorted_how_many_won_by_each_team_by_season(season_team_winners):
    sorted_data = {key: season_team_winners[key] for key in sorted(season_team_winners.keys())}
    return sorted_data

def get_all_years(season_team_winners):
    years = sorted(season_team_winners.keys()) 
    # ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'] 
    return years

def get_all_teams(sorted_data,years):
    teams = set()  # Total teams we took set to avoid duplication
    for season in years:
        teams.update(sorted_data[season].keys())
    return teams

def team_wins_in_individual_years(teams,years,sorted_data):
    team_matches_each_year={}
    for team in teams: 
        team_matches_each_year[team]=[0]*len(years) 
    Curr_index=0
    for year,matches_played_by_each_team in sorted_data.items(): 
        for team,no_of_matches_played in matches_played_by_each_team.items():
            team_matches_each_year[team][Curr_index]=no_of_matches_played 
        Curr_index+=1   
    return team_matches_each_year

# {'Royal Challengers Bangalore': [14, 16, 16, 16, 15, 16, 14, 16, 16, 13], 'Chennai Super Kings': [16, 14, 16, 16, 18, 18, 16, 17, 0, 0], 'Deccan Chargers': [14, 16, 16, 14, 15, 0, 0, 0, 0, 0], 'Kolkata Knight Riders': [13, 13, 14, 15, 17, 16, 16..}
def plot_winners_by_year_by_team(years,team_matches_each_year):
    bottom_stack=[0]*len(years)
    for team,team_values in team_matches_each_year.items():
            plt.bar(years,team_values, bottom=bottom_stack, label=team, width=0.8) 
            bottom_stack = [bottom_stack[i] + team_values[i] for i in range(len(team_values))]
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.title('Stacked Bar Graph of Teams over the Years')
    plt.xticks(years,rotation=45)
    plt.legend(title="Teams", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show() 

def main(): 
    file_data_in_dic=read_matches_file() 

    how_many_won_by_each_team_by_season=get_how_many_won_by_each_team_by_season(file_data_in_dic)

    sorted_data=get_sorted_how_many_won_by_each_team_by_season(how_many_won_by_each_team_by_season)

    years=get_all_years(sorted_data) 

    teams=get_all_teams(sorted_data,years)

    each_team_wins_in_all_years=team_wins_in_individual_years(teams,years,sorted_data) 

    plot_winners_by_year_by_team(years,each_team_wins_in_all_years) 

main()
