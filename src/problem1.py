import csv
import matplotlib.pyplot as plt

def read_deliveries_folder():
    delivery_file = open('ipl_data/deliveries.csv', mode='r')
    reader = csv.DictReader(delivery_file) 
    return reader

def get_total_runs_per_team():
    runs_per_team = {}
    for row in read_deliveries_folder():
        team = row['batting_team']
        runs_scored = int(row['total_runs'])
        if team in runs_per_team:
            runs_per_team[team] += runs_scored
        else:
            runs_per_team[team] = runs_scored 
    return runs_per_team

def plot():
    runs_per_team=get_total_runs_per_team()
    teams = list(runs_per_team.keys())
    runs = list(runs_per_team.values()) 
    plt.bar(teams, runs, color='orange')
    plt.xlabel('Teams', fontsize = 20)
    plt.ylabel('Total Runs', fontsize = 20)
    plt.title('Total Runs Scored by Each Team', fontsize = 26) 
    plt.xticks(rotation=90)
    plt.ion()
    plt.show(block=True) 

plot()


#{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '5', 'batsman': 'Sachin Baby', 'non_striker': 'Iqbal Abdulla', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '1', 'extra_runs': '0', 'total_runs': '1', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
                                 #{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '6', 'batsman': 'Iqbal Abdulla', 'non_striker': 'Sachin Baby', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '4', 'extra_runs': '0', 'total_runs': '4', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
