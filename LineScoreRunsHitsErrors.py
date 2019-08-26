# Copyright (C) 2019 Daniel Opdahl (dopdahl16@gmail.com) Some Rights Reserved. 
# Permission to copy and modify is granted under the GNU General Public License v3.0 license
# Last revised 8/26/2019

import os

lst_runs_hits_errors = []

for file in os.listdir("C:\\Users\\danielopdahl\\Desktop\\LCBoxScores\\LC2008-2018TXT"):
    filename = file[:-4]
    print("Processing: " + filename)
    line_score = open("C:\\Users\\danielopdahl\\Desktop\\LCBoxScores\\LC2008-2018TXT\\"+file, "r")
    # \\path\\to\\
    line_count = 0
    
    ### Each line score has four lines: The title line, the divider line, the away line, and the home line
    ### An example line score is shown below. This is game256.txt. A narrow home victory for the Norse.
    ###
    ###
    ### Score by Innings                  R  H  E
    ### -----------------------------------------
    ### Saint Mary's........ 000 010 0 -  1  5  0
    ### Luther.............. 000 002 X -  2  6  0
    ###
    ###
    
    for line in line_score:
        runs_hits_errors_team_1 = ""
        runs_hits_errors_team_2 = ""
        if line_count == 2:
            
            ### Because line scores always follow the same format, we are able to pull just the R, H, and E 
            ### columns by splitting the line at the "-" character.
            
            split_idx = line.index("-")
            runs_hits_errors_team_1 = line[split_idx + 1:]
            lst_runs_hits_errors.append(runs_hits_errors_team_1.split())
        if line_count == 3:
            split_idx = line.index("-")
            runs_hits_errors_team_2 = line[split_idx + 1:]
            lst_runs_hits_errors.append(runs_hits_errors_team_2.split())
                    
        line_count += 1
        
### The below serves as a kind of novice mistake on my part. Splitting by the "-" character as I do above works 
### great until you realize that certain team names include a "-" character (e.g., "UW-Oshkosh"). To solve this,
### my solution at the time was to hunt for the malformed additions to the lst_runs_hits_errors list, make note 
### of them in the lst_of_malformed_RHEs_to_be_removed list, extract the data that I actually wanted (the R, H, E 
### columns), put that data back into the lst_runs_hits_errors, then finally iterate through the 
### lst_of_malformed_RHEs_to_be_removed list, and extract matches from the lst_runs_hits_errors list. Not very elegant
### in retrospect, but it does do the job... I guess...

lst_of_malformed_RHEs_to_be_removed = []

for R_H_E in lst_runs_hits_errors:
    if len(R_H_E) != 3:
        revised_R_H_E = R_H_E[-3:]
        lst_of_malformed_RHEs_to_be_removed.append(R_H_E)
        lst_runs_hits_errors.append(revised_R_H_E)

for element_to_be_removed in lst_of_malformed_RHEs_to_be_removed:
    lst_runs_hits_errors.remove(element_to_be_removed)

### Now we have gathered all of the runs, hits, and errors that have shown up in our sample of line scores in 
### the form of length 3 lists in the format: ['R', 'H', 'E']. We create a dictionary of the digits 0-9 to keep
### a tally of every time a number appears, and we also keep track of the maximum number and total aggragate 
### number of each category just for fun. Additionally, for hits, we keep track of how often certain number hit
### games appear. There has never been a Norse baseball game in the past 10 years with more than 27 hits accredited
### to a single team, so we cap the dictionary at no less than that number.

run_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
run_max = 0
run_total = 0
hit_endgame_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
hit_num_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0, '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0, '24':0, '25':0, '26':0, '27':0, '28':0, '29':0}
hit_max = 0
hit_total = 0
error_endgame_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
error_max = 0
error_total = 0
print()
print()

for team_runs_hits_errors_result in lst_runs_hits_errors:
    for digit in team_runs_hits_errors_result[0]:
        run_digit_total_dict[digit] += 1
    
    if int(team_runs_hits_errors_result[0]) > run_max:
        run_max = int(team_runs_hits_errors_result[0])
        
    run_total += int(team_runs_hits_errors_result[0])
    
    for digit in team_runs_hits_errors_result[1]:
        hit_endgame_digit_total_dict[digit] += 1
    
    hit_num_total_dict[team_runs_hits_errors_result[1]] += 1
    
    if int(team_runs_hits_errors_result[1]) > hit_max:
        hit_max = int(team_runs_hits_errors_result[1])
        
    hit_total += int(team_runs_hits_errors_result[1])
        
    for digit in team_runs_hits_errors_result[2]:
        error_endgame_digit_total_dict[digit] += 1
    
    if int(team_runs_hits_errors_result[2]) > error_max:
        error_max = int(team_runs_hits_errors_result[2])
        
    error_total += int(team_runs_hits_errors_result[2])        
    
print("Run Data:")
print(run_digit_total_dict)
print("Max: ", run_max)
print("Total: ", run_total)
print()
print("Hit Data")
print(hit_endgame_digit_total_dict)
print("Number of Hits (Not Digits): ", hit_num_total_dict)
print("Max: ", hit_max)
print("Total: ", hit_total)
print()
print("Error Data")
print(error_endgame_digit_total_dict)
print("Max: ", error_max)
print("Total: ", error_total)
print()
hit_aggregate_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

### These loops' usefulness hinges on the fact that hits are incremental, you can only get one hit at a time, never two 
### or three or so on. Thusly, this look counts how many times each digit was needed during the course of the games. 
### For example, if a team ends the game with 3 hits, that means that they had a 0, a 1, a 2, and a 3 displayed for 
### their number of hits at some moment during the game. This loop essentially analizes the frequency with which every 
### digit is needed. Side note: it may surprise you to see that 1 is actually needed the most often instead of 0. This 
### makes sense if you consider how many games have 10 >= hits, and also if you take into account that it's rather 
### rare to have a 0 in the runs column (a shut out) and even rarer to have a 0 in the hits column (a no-hitter). In 
### fact, for Luther baseball and its opponenets, it's actually more likely to have 1 error in the game than 0.

for index in hit_num_total_dict:
    for num_hits in range(int(index)+1):
        for digit in str(num_hits):
            hit_aggregate_digit_total_dict[digit] += hit_num_total_dict[index]

print("Frequency of Hits Digits Usage: ", hit_aggregate_digit_total_dict)
error_aggregate_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for index in error_endgame_digit_total_dict:
    for num_hits in range(int(index)+1):
        for digit in str(num_hits):
            error_aggregate_digit_total_dict[digit] += error_endgame_digit_total_dict[index]
            
print("Frequency of Errors Digits Usage: ", error_aggregate_digit_total_dict)