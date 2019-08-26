# Luther_Baseball_Scoreboard
A project to determine what the lowest number of each of the digits 0-9 are needed in order to reliably run a manual scoreboard

Luther College baseball head coach Bryan Nikkel commissioned a new scoreboard for the baseball team in spring 2019. The new scoreboard would be a manual, hand-turned scoreboard akin to the kind found in the "Green Monster" at Fenway or the classic centerfield scoreboard found at Wrigley. Coach Nikkel knew I liked unique and interesting problems, so he asked me to give him a recommendation for the lowest number of plates of each digit to buy in order to operate the scoreboard without running out of any digits. This project is how I went about solving that problem. I completed this project in roughly 10 hours (I worked on this project while taking 14 credits and during baseball season), and I estimate I saved the program $100-$300 by not buying redundant/extraneous plates.

Please, contact me at dopdahl16@gmail.com with any questions. I had fun doing this (admittedly rushed) analysis and am always looking for feedback.

Legal notice: I do not claim to own or have created chromedriver.exe. chromedriver.exe exists here as a courtesy to the user. ChromeDriver, of which chromedriver.exe is a part, is currently in the open source Chromium project. This project is developed by members of the Chromium and WebDriver teams. Find more information here: https://chromedriver.chromium.org/home

Unless otherwise explicitly stated (such as in the above paragraph), all files in this repository are the sole property of me, Daniel Opdahl.

## Development notes on the project

My approach to finding out the minimum number of plates of each digit were needed to operate the scoreboard started with a few realizations:
- Following convention, the scoreboard would display a full line score (displays for the runs scored in innings 1-10 for both teams, and displays for the running total of runs, hits, and errors for both teams). I then defined the problem as such: with what frequency does each digit 0-9 appear in line scores, and what is the minimum number of each digit 0-9 that one needs in order to operate a manual scoreboard that has 10 innings, runs, hits, and errors for both teams, making up 26 slots in total?
- Balls, strikes, and outs would not be operated by hanging plates, but would be operated by bulbs. In other words, those don't factor into the problem
- The manufacturer of the plates only prints on one side of the plate. (If this were not the case, the problem would have been more complicated because a plate of a certain digit could be in use without being displayed. I did not have time to do a in-depth investigation of how this would complicate things or how many plates we might be able to "save" by having double-sided plates, but from what little research I did and from a good, hard think on the matter, I think that the number of plates we would save by having this feature is negligible)
- We would not have to order 0's for every slot. It is astronomically unlikely for a Luther baseball game to go 10 innings without either team getting a run, a hit, or an error. Additionally, since all of the plates are blank on their back, we don't need a minimum of 20 0's for all 20 innings slots, we just need a minimum of 20 plates for all 20 innings slots. (While the innings slots start off the game blank, the runs, hits, and errors columns start the game off with 0's in them)
- I would need data on what digits are used in line scores most often

After defining the problem and recognizing the need for data, I discovered that Luther baseball has preserved their line scores on the web dating back to 2006. That meant that at the time of writing, I had 12 years of Luther baseball games to pull data from (2006-2018).

I then collected all of the game URLs into text files. The box scores from 2006 and 2007 were in a different format than the box scores from 2008 on, so I decided to pull the data from 2006 and 2007, but not to analyze it right away because I still had 10 years of game data aside from those two. I decided to only go back and reformat the 2006 and 2007 data if I needed to, which I eventually ended up not needing to. The games from 2008 on had a unique URL for every game, and each game's unique URL can be found in LC20082018URLs.txt.

ScrapeBoxScores.py uses a crude chrome web scraper to pull the html from each of the URLs in LC20082018URLs.txt. I pulled the data from the 2006 and 2007 seasons as well, but I stored those separately as I wasn't sure if I would need them, as mentioned above. Additionally, I started counting the games at 81 because if I did need the data from 2006 and 2007, those seasons combined had 80 games, so I wanted to account for the possibility that I would need that data.

After I had collected all of the box scores from the 2008 season through the 2018 season in plain files, I simply appended a .html to the end of each one to return them to their proper format using BoxScorestoHTML.py.

Then, I converted the box scores in .html format to line scores in .txt format. BoxScoretoLineScore.py changes the type of file and then pulls out only the line score from the whole webpage.

Once I had the line scores isolated and collected, it was time to start analyzing. I started off by splitting my analysis into two parts: the innings analysis; and the runs, hits, errors analysis.

LineScoreInnings.py handles the analysis of the 20 inning slots for each game, producing an average number of digits used per game and a maximum number of digits used per game.

LineScoreRunsHitsErrors.py handles the analysis of the runs, hits, and errors columns slots (total of 6 slots), producing total counts of how often the digits 0-9 appear in the final line scores of games for hits, runs, and errors. The program also produces total counts of how often the digits 0-9 appear at any point during the game in the line score for hits and errors. This is because hits and errors* are incremental, meaning that only one can occur per play, which means that the scoreboard can only increase the amount of hits by one (if the operator is doing their job right). This impacts how many digits are used in a game because if a team has 4 hits in a game, they use the 4 that appears in the line score at the end of the game, but the scoreboard would also use the digits 0, 1, 2, and 3 in order to get to 4. Runs are not liable to this effect because scoring 2 or more runs on a play is not only possible, it's probable over the course of a game.

In order to produce my final recommendations, I started with the maximum number of digits used per game produced by LineScoreInnings.py: {'0': 20, '1': 9, '2': 5, '3': 5, '4': 3, '5': 3, '6': 2, '7': 2, '8': 1, '9': 1}. I used the maximum in order to be safe. This result represents only what has been historically true over the past 10 years, and not what is possible, but I think 10 years is a large enough sample size to have confidence in the results. Then, I used some good ol' intuition and the LineScoreRunsHitsErrors.py results to make educated estimates on what digits are needed in order for the runs, hits, and errors section. I did take into account sharing digits across both sections of the score board and the relationship between the two sections. For example, if all the 1's are in use on the innings side, there probably won't be much of a need for 1's on the runs, hits, errors side. The recommendation that I finally went with, and what Coach Nikkel ultimately ordered was: {'0': 25, '1': 13, '2': 9, '3': 9, '4': 7, '5': 7, '6': 6, '7': 5, '8': 4, '9': 3}.

Luther College Baseball played the majority of the 2019 home games using the hand-turned scoreboard. Through the beginning of the 2020 season, the scoreboard has not been short any digits. You can assume that the scoreboard has not failed the program yet, as I will update this README immediately if it ever does fall short of any digit. 

\* Errors are not technically incremental, as more than one error can occur in a single play. However, more than 1 error occurring on a play is very rare, and as such, I treat errors as incremental for my purposes here.

## Things I wish I had done differently
- Taken into account the difference between a seven inning and a nine inning game. You are much more likely to run out of numbers in a nine inning game than in a seven inning game simply because you use more numbers in a nine inning game. While this is less of an issue since roughly 35% of Luther baseball's games are 7 inning games, I still wish I would have taken this into account and done a separate analysis of both 7 inning games and 9 inning games (and maybe even extra inning games).

- Given a little more time, I think I could have made the process of gathering data more efficient by using a more sophisticated web scraper and only pulling the line score from the webpages, instead of the whole html.

- I think that analyzing the relationship between hits and runs and what digits are most commonly shared between the two columns could have provided some more insight that may have enabled me to give a more accurate estimate. E.g., what do 6 hits usually give in runs? Or if we get 13 hits, do we have 3 runs and therefore do we need another 3? What is the likelihood of needing the same digit for runs and hits?

- I wish I had considered putting digits on both sides of the plates that are put into the slots. At the time I didn't look into this because I was very busy and I thought it was very complicated. If this were possible (which it may have been with a different manufacturer), it would have made this a very different problem to solve.

Copyright (C) 2019 Daniel Opdahl (dopdahl16@gmail.com) Some Rights Reserved.
