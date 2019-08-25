from selenium import webdriver

LC20062007URLs = File = open("\\path\\to\\LCBoxScores\\LC20062007URLs.txt", "r")

for URL in LC20062007URLs:
    print("'" + URL.rstrip() + "'")
    print("___")

LC20082018URLs = File = open("\\path\\to\\LCBoxScores\\LC20082018URLs.txt", "r")

### games in 2006 and 2007 total 80 games

GameCount = 80 

for URL in LC20082018URLs:
    GameCount += 1
    driver = webdriver.Chrome("\\path\\to\\chromedriver.exe")
    driver.get(URL.rstrip())
    
    with open("\\path\\to\\LCBoxScores\\Game"+str(GameCount), "w") as File:
        File.write(driver.page_source)
    File.close()
    
    print("'" + URL.rstrip() + "'")
    print("___")
    print(GameCount)

