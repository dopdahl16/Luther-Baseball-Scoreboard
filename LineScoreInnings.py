# Copyright (C) 2019 Daniel Opdahl (dopdahl16@gmail.com) Some Rights Reserved. 
# Permission to copy and modify is granted under the GNU General Public License v3.0 license
# Last revised 8/26/2019

import os

lst_of_inning_box_scores = []

for file in os.listdir("C:\\Users\\danielopdahl\\Desktop\\LCBoxScores\\LC2008-2018TXT"):
    filename = file[:-4]
    line_score = open("C:\\Users\\danielopdahl\\Desktop\\LCBoxScores\\LC2008-2018TXT\\"+file, "r")
    single_digit_runs_by_inning = []
    line_count = 0
    do_not_load_next_digit = False
    
    for line in line_score:
        if line_count == 2 or line_count == 3:
            
            for character in line:
                if character == "-":
                    break
                if character.isdigit() and do_not_load_next_digit == False:
                    single_digit_runs_by_inning.append(character)
                    do_not_load_next_digit = False
                    
                ### We search for the "(" character because of the format of the scoreboard and the line scores. In 
                ### the line scores, if a team scores a double-digit number of runs in a single inning, the line score 
                ### will denote that number in parentheses. Because of how the physical scoreboard is constructed, 
                ### like many hand-turned scoreboards, each inning slot can only display one digit. Because of this 
                ### physical limitation, we only account for the digit in the ones place when reading in the line score 
                ### if an inning has a double digit score. For example, if a team scores 12 runs in one inning, we don't 
                ### want to read in a '1' and a '2', we only want to read in a '2' because only the '2' will be 
                ### displayed in the inning slot on the scoreboard. An example of a line score with a double digit 
                ### inning is displayed below. In this line score, we would only want to read in the '0' digit of the 
                ### '10' number.
                ### 
                ### 
                ### Score by Innings                     R  H  E
                ### --------------------------------------------
                ### Luther Norse........ 30   0 113 0 -  8 12  7
                ### Coe Kohawks......... 0(10)4 203 X - 19 17  2                
                ### 
                ### 
                
                if character == "(":
                    do_not_load_next_digit = True
                else:
                    do_not_load_next_digit = False

        line_count += 1
        
    lst_of_inning_box_scores.append(single_digit_runs_by_inning)
        
print("FINAL: " , lst_of_inning_box_scores)

### Now that we have our list of all the scores of each inning (as it would appear on the scoreboard), we can start 
### counting. We create count_dict to keep track of how often each digit appears in any inning slot. We additionally 
### create max_dict to record what the most number of digits in a line score was. You may find it surprising how 
### max_dict reports how the most 0's on the scoreboard for the innings score was 22, considering how there is a 
### maximum of 20 inning slots on the scoreboard. This is because the program does not take into account the 
### limitations of extra innings. In the game that had a 0 in 22 places for inning scores, there were 13 innings.

count_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
max_dict =  {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
temp_dict =  {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
games_counted = 0

### Again, here is a novice mistake by me. I do not need to use temp_dict here, but I do. I could retroactively fix 
### this, but I chose to leave it here for authenticity, and as a mark of my growth.

for inning_scores_by_game in lst_of_inning_box_scores:
    games_counted += 1
    temp_dict =  {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    
    for inning_score in inning_scores_by_game:
        count_dict[inning_score] = count_dict[inning_score] + 1
        temp_dict[inning_score] = temp_dict[inning_score] + 1
        
    for digit in temp_dict:
        if temp_dict[digit] > max_dict[digit]:
            max_dict[digit] = temp_dict[digit]
   
print("Count Dict" , count_dict)
avg_dict = count_dict.copy()

### Above, we keep track of the number of games we have gone through and pulled data from so that we can find the 
### average number of each digit needed per game, as we do below.

for digit in avg_dict:
    avg_dict[digit] = avg_dict[digit]/games_counted
    
print("AVG: ", avg_dict)
print("MAX DICT : ", max_dict)