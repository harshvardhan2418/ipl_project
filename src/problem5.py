# Number of matches played per year for all the years in IPL.
# Plot a bar chart. 


# {'id': '634', 'season': '2016', 'city': 'Delhi', 'date': '2016-05-25', 'team1': 'Sunrisers Hyderabad', 'team2': 'Kolkata Knight Riders', 'toss_winner': 'Kolkata Knight Riders', 'toss_decision': 'field', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '22', 'win_by_wickets': '0', 'player_of_match': 'MC Henriques', 'venue': 'Feroz Shah Kotla', 'umpire1': 'M Erasmus', 'umpire2': 'C Shamshuddin', 'umpire3': ''}
# {'id': '635', 'season': '2016', 'city': 'Delhi', 'date': '2016-05-27', 'team1': 'Gujarat Lions', 'team2': 'Sunrisers Hyderabad', 'toss_winner': 'Sunrisers Hyderabad', 'toss_decision': 'field', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '0', 'win_by_wickets': '4', 'player_of_match': 'DA Warner', 'venue': 'Feroz Shah Kotla', 'umpire1': 'M Erasmus', 'umpire2': 'CK Nandan', 'umpire3': ''}
# {'id': '636', 'season': '2016', 'city': 'Bangalore', 'date': '2016-05-29', 'team1': 'Sunrisers Hyderabad', 'team2': 'Royal Challengers Bangalore', 'toss_winner': 'Sunrisers Hyderabad', 'toss_decision': 'bat', 'result': 'normal', 'dl_applied': '0', 'winner': 'Sunrisers Hyderabad', 'win_by_runs': '8', 'win_by_wickets': '0', 'player_of_match': 'BCJ Cutting', 'venue': 'M Chinnaswamy Stadium', 'umpire1': 'HDPK Dharmasena', 'umpire2': 'BNJ Oxenford', 'umpire3': ''}


import csv
import matplotlib.pyplot as plt 

def read_matches_file():
    delivery_file = open('ipl_data/matches.csv', mode='r')
    reader = csv.DictReader(delivery_file)
    return reader

def no_of_matches_played_for_all_years():
    no_of_matches_played_for_all_years={}
    for each_row in read_matches_file(): 
        if each_row['season'] not in no_of_matches_played_for_all_years: 
            no_of_matches_played_for_all_years[each_row['season']]=1 
        else: 
            no_of_matches_played_for_all_years[each_row['season']]+=1   
    return no_of_matches_played_for_all_years

def plot_graph():
    dic=no_of_matches_played_for_all_years()
    years=list(dic.keys()) 
    no_of_matches=list(dic.values()) 
    plt.bar(years, no_of_matches, color='purple')
    plt.xlabel('seasons')
    plt.ylabel('no of matches')
    plt.title('no of matches in each season')
    # Rotate x-axis labels for better readability (optional)
    plt.xticks(rotation=45)
    # Show the plot
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()
plot_graph()
