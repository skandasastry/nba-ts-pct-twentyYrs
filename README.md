# NBA League Average TS% progression

This is a simple plot of the league average true-shooting percentage (TS%) from the 1996-97 season to the 2019-20 season. TS% is a measure of scoring efficiency which factors in the added value of three-point shots and benefits players that are able to create more free throw 
opportunities for themselves. Here is the formula, according to Basketball Reference: 

PTS / (2 * (FGA + 0.44 * FTA))

The intuition behind the formula is that dividing points scored by total FGA and FTA will make it so that 3-point baskets are weighted more than 2-point baskets. The multiplication of 2 in the denominator is simply to make the scale similar to FG%. The 0.44 multiplied by FTA is to account for situations where a player shoots only one free throw (and-one opportunities, technical foul shots, etc.). Note that this constant is an empirical one and only has been calibrated based on NBA data, so for other leagues it would make more sense to re-calculate that constant.

Over the past 20 years, the offensive principles of the league have changed drastically. This plot shows the effects
of the explosion of three-point attempts over the past few years as a result of the Golden State Warriors' revolutionary
offensive system, as well as the "dark ages" of efficiency in the early to mid aughts when many teams sought to create
as many isolation opportunities as they could on offense.



Acknowledgements: 
Postseason league average data was pulled from stats.nba.com using the NBA API developed by github user "swar": https://github.com/swar/nba_api

Regular season league average data was found on Basketball-Reference: https://www.basketball-reference.com/leagues/NBA_stats_per_game.html

