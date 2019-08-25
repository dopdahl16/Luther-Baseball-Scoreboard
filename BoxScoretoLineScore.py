import os

for file in os.listdir("C:\\Users\\dopda\\Desktop\\LCBoxScores"):
    
    f = open("C:\\Users\\dopda\\Desktop\\LCBoxScores\\"+file, "r")
    filename = file[:-5]
    box_score = open("C:\\Users\\dopda\\Desktop\\LCBoxScores\\"+filename+".txt", "w")
    
    write = False
    lines_to_write = 4
    
    for i in f:
        if "Score by Innings" in i:
            write = True
        if write == True:
            box_score.write(i)
            lines_to_write-=1
        if lines_to_write == 0:
            write = False
            break