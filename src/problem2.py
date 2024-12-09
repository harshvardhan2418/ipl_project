# Consider only games played by Royal Challengers Bangalore. Now plot the total runs scored by top 10 batsman playing for Royal Challengers Bangalore over the history of IPL.

# Plot only top 10 batsmen by runs scored in RCB.



import csv
import matplotlib.pyplot as plt

def read_the_file_ipl_data(path):
    delivery_file = open(path, mode='r')
    reader = csv.DictReader(delivery_file) 
    return reader

def get_batsmen_runs_for_rcb(read_the_file):
    batsmen_runs_for_rcb = {}
    for row in read_the_file:
        if row['batting_team'] == 'Royal Challengers Bangalore':
            batsman = row['batsman']
            runs = int(row['batsman_runs'])  
            if batsman in batsmen_runs_for_rcb:
                batsmen_runs_for_rcb[batsman] += runs 
            else:
                batsmen_runs_for_rcb[batsman] = runs
    return batsmen_runs_for_rcb

def get_top_ten_batsmen_for_rcb(batsmen_runs_for_rcb):
    top_ten_batsmen_for_rcb= dict(sorted(batsmen_runs_for_rcb.items(), key=lambda x: x[1], reverse=True)[:10])
    return top_ten_batsmen_for_rcb


def plot_top_ten_batsmen(top_ten_batsmen_for_rcb):
    batsmen=top_ten_batsmen_for_rcb.keys() 
    runs=top_ten_batsmen_for_rcb.values()
    plt.bar(batsmen, runs, color='purple')
    plt.xlabel('Total Runs', fontsize=20)
    plt.ylabel('Batsman', fontsize=20)
    plt.title('Top 10 Batsmen by Runs for Royal Challengers Bangalore (RCB)', fontsize=26)
    plt.xticks(rotation=45)  
    plt.yticks(fontsize=14)
    plt.show()
    
def main():
    read_the_file=read_the_file_ipl_data('ipl_data/deliveries.csv') 
    batsmen_runs_for_rcb=get_batsmen_runs_for_rcb(read_the_file)
    top_ten_batsmen_for_rcb=get_top_ten_batsmen_for_rcb(batsmen_runs_for_rcb) 
    plot_top_ten_batsmen(top_ten_batsmen_for_rcb) 
main()