# 7. Extra runs conceded per team in the year 2016
# Plot a bar chart. 

# {'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '5', 'batsman': 'Sachin Baby', 'non_striker': 'Iqbal Abdulla', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '1', 'extra_runs': '0', 'total_runs': '1', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
# {'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '6', 'batsman': 'Iqbal Abdulla', 'non_striker': 'Sachin Baby', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '4', 'extra_runs': '0', 'total_runs': '4', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}

import csv
import matplotlib.pyplot as plt

def get_read_deliveries_file(path):
    delivery_file = open('ipl_data/deliveries.csv', mode='r')
    reader1 = csv.DictReader(delivery_file)  
    return reader1

def get_read_matches_file(path):
    delivery_file = open('ipl_data/matches.csv', mode='r')
    reader2 = csv.DictReader(delivery_file) 
    return reader2
def get_all_ids_of_year_2016(read_matches_file):
    all_ids_of_year_2016=[] 
    for  each_row in read_matches_file: 
        if each_row['season']=='2016': 
            all_ids_of_year_2016.append(each_row['id']) 
    return all_ids_of_year_2016 

def get_each_team_extra_runs_in_2016(read_deliveries_file,all_ids_of_year_2016):
    each_team_extra_runs_in_2016={}
    for each_row in read_deliveries_file: 
        if each_row['match_id'] in all_ids_of_year_2016:  
            team=each_row['bowling_team'] 
            if team not in each_team_extra_runs_in_2016: 
                each_team_extra_runs_in_2016[team]=0 
            each_team_extra_runs_in_2016[team]+=int(each_row['extra_runs'])
    return each_team_extra_runs_in_2016
    
def plot_bar_graph(each_team_extra_runs_in_2016):
    teams = list(each_team_extra_runs_in_2016.keys())
    extra_runs = list(each_team_extra_runs_in_2016.values()) 
    plt.bar(teams, extra_runs, color='orange')
    plt.xlabel('Teams', fontsize = 20)
    plt.ylabel('extra Runs', fontsize = 20)
    plt.title('extra runs conceded by by Each Team in 2016', fontsize = 26) 
    plt.xticks(rotation=90)
    plt.show(block=True) 


def main():
    read_deliveries_file=get_read_deliveries_file('ipl_data/deliveries.csv')
    read_matches_file=get_read_matches_file('ipl_data/matches.csv') 
    all_ids_of_year_2016=get_all_ids_of_year_2016(read_matches_file)
    each_team_extra_runs_in_2016=get_each_team_extra_runs_in_2016(read_deliveries_file,all_ids_of_year_2016) 
    plot_bar_graph(each_team_extra_runs_in_2016)
main()

# dic={} 
# for each_row in reader: 
#     if each_row[match_id] in ids_2016:  

