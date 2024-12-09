# Top 10 economical bowlers in the year 2015
# Plot a bar chart. 

# noball_runs,penalty_runs,batsman_runs,extra_runs 
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

def get_all_ids_2015(read_matches_file):
    all_ids_2015=[] 
    for  each_row in read_matches_file: 
        if each_row['season']=='2015': 
            all_ids_2015.append(each_row['id']) 
    return all_ids_2015

def get_balls_and_runs_of_each_bowler(read_deliveries_file,all_ids_2015):
    no_of_runs_conceded_by_each_bowler={}
    dic_balls_bowled_by_each_bowler={}
    for each_row in read_deliveries_file: 
        if each_row['match_id'] in all_ids_2015: 
            bow=each_row['bowler']
            if bow not in no_of_runs_conceded_by_each_bowler: 
                no_of_runs_conceded_by_each_bowler[bow]=0 
                dic_balls_bowled_by_each_bowler[bow]=0
            no_of_runs_conceded_by_each_bowler[bow]+=int(each_row['noball_runs'])+int(each_row['penalty_runs'])+int(each_row['batsman_runs'])+int(each_row['extra_runs'])
            dic_balls_bowled_by_each_bowler[bow]+=1 
    return [no_of_runs_conceded_by_each_bowler,dic_balls_bowled_by_each_bowler]

def get_no_overs_bowled_by_each_bowler(balls_bowled_by_each_bowler):
    overs_bowled_by_each_bowler={} 
    for each_bowler in balls_bowled_by_each_bowler: 
        if each_bowler not in overs_bowled_by_each_bowler:
            overs_bowled_by_each_bowler[each_bowler]=0 
        overs_bowled_by_each_bowler[each_bowler]=balls_bowled_by_each_bowler[each_bowler]/6
    return overs_bowled_by_each_bowler

def get_the_economy_of_each_bowler(runs_given_by_each_bowler,overs_bowled_by_each_bowler):
    economy_of_each_bowler={} 
    for each_bowler in runs_given_by_each_bowler: 
        if each_bowler not in economy_of_each_bowler: 
            economy_of_each_bowler[each_bowler]=0 
        economy_of_each_bowler[each_bowler]=runs_given_by_each_bowler[each_bowler]/overs_bowled_by_each_bowler[each_bowler] 
    return economy_of_each_bowler

def get_value(item):
    return item[1] 

def get_top_10_bowlers(economy_of_each_bowler):
    top_10_bowlers = sorted(economy_of_each_bowler.items(), key=get_value) 
    top_10_bowlers=top_10_bowlers[:10]
    top_10_bowlers = dict(top_10_bowlers) 
    return top_10_bowlers

def plot_bar_graph(top_10_bowlers):
    bowler = list(top_10_bowlers.keys())
    economy = list(top_10_bowlers.values()) 
    plt.bar(bowler, economy, color='orange')
    plt.xlabel('bowler', fontsize = 20)
    plt.ylabel('Economy', fontsize = 20)
    plt.title('top 10 ecnomical bowler in 2015', fontsize = 26) 
    plt.xticks(rotation=90)
    plt.show(block=True) 

def main():
    read_deliveries_file=get_read_deliveries_file('ipl_data/deliveries.csv')
    read_matches_file=get_read_matches_file('ipl_data/matches.csv')  
    all_ids_2015=get_all_ids_2015(read_matches_file) 

    balls_and_runs_of_each_bowler=get_balls_and_runs_of_each_bowler(read_deliveries_file,all_ids_2015)
    runs_given_by_each_bowler=balls_and_runs_of_each_bowler[0]
    balls_bowled_by_each_bowler=balls_and_runs_of_each_bowler[1]

    overs_bowled_by_each_bowler=get_no_overs_bowled_by_each_bowler(balls_bowled_by_each_bowler) 

     
    economy_of_each_bowler=get_the_economy_of_each_bowler(runs_given_by_each_bowler,overs_bowled_by_each_bowler) 

    top_10_bowlers=get_top_10_bowlers(economy_of_each_bowler) 

    plot_bar_graph(top_10_bowlers) 

main()