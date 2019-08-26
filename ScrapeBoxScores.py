# Copyright (C) 2019 Daniel Opdahl (dopdahl16@gmail.com) Some Rights Reserved. 
# Permission to copy and modify is granted under the GNU General Public License v3.0 license
# Last revised 8/26/2019

from selenium import webdriver

LC_2006_2007_URLs = file = open("\\path\\to\\LCBoxScores\\LC20062007URLs.txt", "r")

for URL in LC_2006_2007_URLs:
    print("'" + URL.rstrip() + "'")
    print("___")

LC_2008_2018_URLs = file = open("\\path\\to\\LCBoxScores\\LC20082018URLs.txt", "r")

### Games in 2006 and 2007 total 80 games, so we initialize our count at 80, anticipating the event in which we go back and include the 2006 and 2007 games

game_count = 80 

for URL in LC_2008_2018_URLs:
    game_count += 1
    driver = webdriver.Chrome("\\path\\to\\chromedriver.exe")
    driver.get(URL.rstrip())
    
    with open("\\path\\to\\LCBoxScores\\Game"+str(game_count), "w") as file:
        file.write(driver.page_source)
    file.close()
    
    print("'" + URL.rstrip() + "'")
    print("___")
    print(game_count)

