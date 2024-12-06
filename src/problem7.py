# 7. Extra runs conceded per team in the year 2016
# Plot a bar chart. 

{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '5', 'batsman': 'Sachin Baby', 'non_striker': 'Iqbal Abdulla', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '1', 'extra_runs': '0', 'total_runs': '1', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}
{'match_id': '636', 'inning': '2', 'batting_team': 'Royal Challengers Bangalore', 'bowling_team': 'Sunrisers Hyderabad', 'over': '20', 'ball': '6', 'batsman': 'Iqbal Abdulla', 'non_striker': 'Sachin Baby', 'bowler': 'B Kumar', 'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 'batsman_runs': '4', 'extra_runs': '0', 'total_runs': '4', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}

import csv
import matplotlib.pyplot as plt

delivery_file = open('ipl_data/deliveries.csv', mode='r')
reader1 = csv.DictReader(delivery_file)  

delivery_file = open('ipl_data/matches.csv', mode='r')
reader2 = csv.DictReader(delivery_file) 
ids_2016=[] 
for  each_row in reader2: 
    if each_row['season']=='2016': 
        ids_2016.append(each_row['id']) 
dic={}
for each_row in reader1: 
    if each_row['match_id'] in ids_2016:  
        team=each_row['bowling_team'] 
        if team not in dic: 
            dic[team]=0 
        dic[team]+=1 

teams = list(dic.keys())
extra_runs = list(dic.values()) 
plt.bar(teams, extra_runs, color='orange')
plt.xlabel('Teams', fontsize = 20)
plt.ylabel('extra Runs', fontsize = 20)
plt.title('extra runs conceded by by Each Team in 2016', fontsize = 26) 
plt.xticks(rotation=90)
plt.ion()
plt.show(block=True) 





# dic={} 
# for each_row in reader: 
#     if each_row[match_id] in ids_2016:  

