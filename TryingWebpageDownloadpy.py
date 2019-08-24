from selenium import webdriver

name = "1"

driver = webdriver.Chrome("C:\\Users\\dopda\\Desktop\\chromedriver.exe")
driver.get("http://sports.luther.edu/stats/men/baseball/2006/teamstat.htm")
with open("C:\\Users\\dopda\\Desktop\\LCBoxScores\\LC2006-2007\\GGG"+name, "w") as f:
    f.write(driver.page_source)
f.close()