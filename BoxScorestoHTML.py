import os

for BoxScore in os.listdir("\\path\\to\\LCBoxScores"):
    print(BoxScore)
    os.rename("\\path\\to\\LCBoxScores\\"+BoxScore, "\\path\\to\\LCBoxScores\\"+BoxScore+".html")
    