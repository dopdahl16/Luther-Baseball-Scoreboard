import os

for file in os.listdir("C:\\Users\\dopda\\Desktop\\LCBoxScores\\LC2008-2018"):
    print(file)
    os.rename("C:\\Users\\dopda\\Desktop\\LCBoxScores\\LC2008-2018\\"+file, "C:\\Users\\dopda\\Desktop\\LCBoxScores\\LC2008-2018HTML\\"+file+".html")
    