# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:59:44 2020

@author: Skanda Sastry
"""

#see how long program takes to run
import time
start_time = time.time()

#for csv file i/o
import csv
import os 

#for api interactions
from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd
from nba_api.stats.library.parameters import SeasonAll

custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Chrome/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

#years that stats.nba.com has available playoff data
END_YEAR = 2019
START_YEAR = 1996
CURRENT_SEASON = "2019-20"


fullSeasons = []

# construct season list with format "2019-20", "2018-19", etc. to abide by
# stats.nba.com API format
for i in range(START_YEAR, END_YEAR):
    fullSeasons.insert(0, str(i) + "-" + str(i + 1)[2:])

# map which will map avg ts% to season
postSeasonTSDict = {}

#finds where ts% is located in the dictionary/array combination
ts_pct_index = 0

#fills the dictionary with average ts% values per postseason
for i in fullSeasons:
    postSeasonsStatsDict = leaguedashteamstats.LeagueDashTeamStats(
        measure_type_detailed_defense="Advanced",
        season=i,
        season_type_all_star="Playoffs").get_dict()

    if ts_pct_index == 0:
        ts_pct_index = postSeasonsStatsDict['resultSets'][0]['headers'].index('TS_PCT')
    
    
    tsSum = 0.0
    tsCounter = 0
    
    #computes average for each season
    for j in postSeasonsStatsDict['resultSets'][0]['rowSet']:
        tsSum += j[ts_pct_index]
        tsCounter += 1
        
    postSeasonTSDict[i] = tsSum/tsCounter



#writes average for each season to csv
with open('postSeason-TS.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Number","Season", "Average TS%"])
    counter = 1
    for i in fullSeasons:
        writer.writerow([counter, i, postSeasonTSDict[i]])
        counter+=1
  

#prints how long program and requests took
print("--- %s seconds ---" % (time.time() - start_time))


