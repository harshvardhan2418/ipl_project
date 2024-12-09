import csv
import matplotlib.pyplot as plt

def read_the_file_ipl_data(path):
    delivery_file = open(path, mode='r')
    reader = csv.DictReader(delivery_file) 
    return reader

def get_total_runs_per_team(read_the_file):
    total_runs_per_team = {}
    for row in read_the_file:
        team = row['batting_team']
        runs_scored = int(row['total_runs'])
        if team in total_runs_per_team:
            total_runs_per_team[team] += runs_scored
        else:
            total_runs_per_team[team] = runs_scored 
    return total_runs_per_team

def plot_bar_chart(total_runs_per_team):
    teams = list(total_runs_per_team.keys())
    runs = list(total_runs_per_team.values()) 
    plt.bar(teams, runs, color='orange')
    plt.xlabel('Teams', fontsize = 20)
    plt.ylabel('Total Runs', fontsize = 20)
    plt.title('Total Runs Scored by Each Team', fontsize = 26) 
    plt.xticks(rotation=90)
    plt.show(block=True) 

def main():
    read_the_file=read_the_file_ipl_data('ipl_data/deliveries.csv')
    total_runs_per_team=get_total_runs_per_team(read_the_file) 
    plot_bar_chart(total_runs_per_team) 
main()


#{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '5', 'batsman': 'Sachin Baby', 'non_striker': 'Iqbal Abdulla', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '1', 'extra_runs': '0', 'total_runs': '1', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
                                 #{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '6', 'batsman': 'Iqbal Abdulla', 'non_striker': 'Sachin Baby', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '4', 'extra_runs': '0', 'total_runs': '4', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
