# Top 10 economical bowlers in the year 2015
# Plot a bar chart. 

# noball_runs,penalty_runs,batsman_runs,extra_runs 
{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '5', 'batsman': 'Sachin Baby', 'non_striker': 'Iqbal Abdulla', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '1', 'extra_runs': '0', 'total_runs': '1', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '6', 'batsman': 'Iqbal Abdulla', 'non_striker': 'Sachin Baby', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '4', 'extra_runs': '0', 'total_runs': '4', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}

import csv
import matplotlib.pyplot as plt

delivery_file = open('ipl_data/deliveries.csv', mode='r')
reader1 = csv.DictReader(delivery_file)  

delivery_file = open('ipl_data/matches.csv', mode='r')
reader2 = csv.DictReader(delivery_file) 

ids_2015=[] 
for  each_row in reader2: 
    if each_row['season']=='2015': 
        ids_2015.append(each_row['id']) 
dic_runs={}
dic_balls={}
for each_row in reader1: 
    if each_row['match_id'] in ids_2015: 
        bow=each_row['bowler']
        if bow not in dic_runs: 
            dic_runs[bow]=0 
            dic_balls[bow]=0
        dic_runs[bow]+=int(each_row['noball_runs'])+int(each_row['penalty_runs'])+int(each_row['batsman_runs'])+int(each_row['extra_runs'])
        dic_balls[bow]+=1 
dic_overs_bowled={} 
for each_bowler in dic_balls: 
    if each_bowler not in dic_overs_bowled:
        dic_overs_bowled[each_bowler]=0 
    dic_overs_bowled[each_bowler]=dic_balls[each_bowler]/6

dic_economy={} 
for each_bowler in dic_runs: 
    if each_bowler not in dic_economy: 
        dic_economy[each_bowler]=0 
    dic_economy[each_bowler]=dic_runs[each_bowler]/dic_overs_bowled[each_bowler]

def get_value(item):
    return item[1] 
sorted_data = sorted(dic_economy.items(), key=get_value) 
sorted_data=sorted_data[:10]
sorted_dict = dict(sorted_data) 


bowler = list(sorted_dict.keys())
economy = list(sorted_dict.values()) 
plt.bar(bowler, economy, color='orange')
plt.xlabel('bowler', fontsize = 20)
plt.ylabel('Economy', fontsize = 20)
plt.title('top 10 ecnomical bowler in 2015', fontsize = 26) 
plt.xticks(rotation=90)
plt.ion()
plt.show(block=True) 


   
