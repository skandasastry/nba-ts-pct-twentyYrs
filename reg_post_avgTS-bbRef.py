# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 09:35:16 2020

@author: skand
"""

#for csv fiel i/o
import csv

#for plotting line graph
import matplotlib.pyplot as plt

# calculation of ts% per bbref data
def calculate_ts(pts, fga, fta):
    tsa = fga + (0.44 * fta)
    return round(pts/(2 * tsa),3)


# parses league averages data into a dictionary
reader = csv.DictReader(open("data/regseason-leagueAvgs.txt"))



regSeasonAvgTS = {}
postSeasonAvgTS = {}

#calcualtes ts% per season and fills dictionary for reg season
for row in reader:
    total_pts = float(row['PTS']) * float(row['G'])
    regSeasonAvgTS[str(int(row['Season'][0:4]) + 1)] = calculate_ts(float(row['PTS']),
                  float(row['FGA']), float(row['FTA']))


#reads csv of postseason avg data and fills dictionary w avg ts% per postseason
postreader = csv.DictReader(open("data/postSeason-TS.csv"))
for row in postreader:
    postSeasonAvgTS[str(int(row['Season'][0:4]) + 1)] = round(float(row['Average TS%']), 3)





#plots the two data sets on a line graph
lists = sorted(regSeasonAvgTS.items())
list3 = sorted(postSeasonAvgTS.items())
a, b = zip(*list3)
x, y = zip(*lists)

fig, ax = plt.subplots(figsize = (16.0, 9.0))

ax.plot(x, y, label='Regular Season NBA Avg. TS', color='blue', linestyle='dashed',
        marker = 'o')

    
ax.plot(a, b, label='Postseason NBA Avg. TS', color = 'red', linestyle='dashed',
        marker='o')


legend = ax.legend(fontsize = 12)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Season', fontsize = 18, labelpad = 20)
plt.ylabel('TS%', fontsize = 18, labelpad = 20)
plt.title('Scoring efficiency in the NBA over past 20 years', fontsize = 20)
plt.show()
plt.savefig("output_files/ts-over-the-years.png")

