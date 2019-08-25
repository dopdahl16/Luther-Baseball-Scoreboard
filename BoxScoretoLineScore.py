import os

for file in os.listdir("\\path\\to\\LCBoxScores"):
    BoxScore = open("\\path\\to\\LCBoxScores\\"+file, "r")
    filename = file[:-5]
    LineScore = open("\\path\\to\\LCBoxScores\\"+filename+".txt", "w")
    write = False
    lines_to_write = 4
    
    ### The below iterates through the .html files line by line and finds the keyphrase "Score by Innings" which indicates that it and the next 3 lines are the line score. 
    
    for Line in BoxScore:
        if "Score by Innings" in Line:
            write = True
        if write == True:
            LineScore.write(Line)
            lines_to_write-=1
        if lines_to_write == 0:
            write = False
            break