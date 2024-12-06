# Consider only games played by Royal Challengers Bangalore. Now plot the total runs scored by top 10 batsman playing for Royal Challengers Bangalore over the history of IPL.

# Plot only top 10 batsmen by runs scored in RCB.



import csv
import matplotlib.pyplot as plt

def read_deliveryfile():
    delivery_file = open('ipl_data/deliveries.csv', mode='r')
    reader = csv.DictReader(delivery_file)
    return reader
def batsmen_with_runs():
    batsman_runs = {}
    for row in read_deliveryfile():
        if row['batting_team'] == 'Royal Challengers Bangalore':
            batsman = row['batsman']
            runs = int(row['batsman_runs'])  
            if batsman in batsman_runs:
                batsman_runs[batsman] += runs 
            else:
                batsman_runs[batsman] = runs
    return batsman_runs

def top_ten_batsmen():
    top_ten= dict(sorted(batsmen_with_runs().items(), key=lambda x: x[1], reverse=True)[:10])
    return top_ten

def plot_top_ten_batsmen():
    top_ten_bat=top_ten_batsmen()
    batsmen=top_ten_bat.keys() 
    runs=top_ten_bat.values()
    plt.bar(batsmen, runs, color='purple')
    plt.xlabel('Total Runs', fontsize=20)
    plt.ylabel('Batsman', fontsize=20)
    plt.title('Top 10 Batsmen by Runs for Royal Challengers Bangalore (RCB)', fontsize=26)
    plt.xticks(rotation=45)  
    plt.yticks(fontsize=14)
    plt.show()
plot_top_ten_batsmen()
