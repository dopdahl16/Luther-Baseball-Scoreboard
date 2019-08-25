from selenium import webdriver

LC20062007URLs = f = open("C:\\Users\\dopda\\Desktop\\LCBoxScores\\LC20062007URLs.txt", "r")
for i in LC20062007URLs:
    print("'" + i.rstrip() + "'")
    print("___")

LC20082018URLs = f = open("C:\\Users\\dopda\\Desktop\\LCBoxScores\\LC20082018URLs.txt", "r")
count = 80 #games in 2006 and 2007 total 80 games
for i in LC20082018URLs:
    count += 1
    
    driver = webdriver.Chrome("C:\\Users\\dopda\\Desktop\\scoreboard\\Luther_Baseball_Scoreboard\\chromedriver.exe")
    driver.get(i.rstrip())
    with open("C:\\Users\\dopda\\Desktop\\LCBoxScores\\Game"+str(count), "w") as f:
        f.write(driver.page_source)
    f.close()
    
    print("'" + i.rstrip() + "'")
    print("___")
    print(count)

