import os

for file in os.listdir("C:\\Users\\dopda\\Desktop\\LCBoxScores"):
    print(file)
    os.rename("C:\\Users\\dopda\\Desktop\\LCBoxScores\\"+file, "C:\\Users\\dopda\\Desktop\\LCBoxScores\\"+file+".html")
    