# 3. Foreign umpire analysis
# Obtain a source for country of origin of umpires. Plot a chart of number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph.




import csv
import matplotlib.pyplot as plt

def get_read_the_file_matches(path):
    delivery_file = open('ipl_data/matches.csv', mode='r')
    reader1 = csv.DictReader(delivery_file)
    return reader1

def get_read_the_file_umpires(path):
    delivery_file = open('ipl_data/umpires.csv', mode='r')
    reader2 = csv.DictReader(delivery_file)
    return reader2

def list_of_umpires(read_the_file_matches):
    umpires_list=set()  #to avoid duplication
    for row in read_the_file_matches:
        umpire_in_match = [row['umpire1'],row['umpire2'],row['umpire3']]
        umpires_list.update(umpire_in_match)
    return umpires_list

def get_unmire_country(read_the_file_umpires):
    umpire_country_map = {}
    for row in read_the_file_umpires:
        umpire_name=row['umpire'] 
        umpire_country=row['country_from'] 
        if umpire_country!='India':
            umpire_country_map[umpire_name]=umpire_country
    return umpire_country_map 

def get_umpire_count_from_each_country(umpire_country_map,umpires_list):
    umpire_count_from_each_country = {} 
    for umpire in umpires_list:
        umpire_country = umpire_country_map.get(umpire)
        if umpire_country:
            if umpire_country not in umpire_count_from_each_country:
                umpire_count_from_each_country[umpire_country] = 0
            umpire_count_from_each_country[umpire_country] +=1 
    return umpire_count_from_each_country

def plot_bar_graph(umpire_count_from_each_country):
    countries = list(umpire_count_from_each_country.keys())
    counts = list(umpire_count_from_each_country.values())
    plt.bar(countries, counts, color='yellow', edgecolor='black')
    plt.title('Number of Foreign Umpires by Country in IPL', fontsize=14)
    plt.xlabel('Country', fontsize=24)
    plt.ylabel('Number of Umpires', fontsize=24)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()

def main(): 
    read_the_file_matches=get_read_the_file_matches('ipl_data/matches.csv') 
    read_the_file_umpires=get_read_the_file_umpires('ipl_data/umpires.csv') 

    umpires_list=list_of_umpires(read_the_file_matches) 
    umpire_country=get_unmire_country(read_the_file_umpires) 

    umpire_count_from_each_country=get_umpire_count_from_each_country(umpire_country,umpires_list) 

    plot_bar_graph(umpire_count_from_each_country) 

main()