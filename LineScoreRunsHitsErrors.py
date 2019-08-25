import os

lst_of_RHE = []

for file in os.listdir("\\path\\to\\LCBoxScores\\LC2008-2018TXT"):
    filename = file[:-4]
    print()
    print()
    print(filename)
    
    ###GAME 249 - use "." as trigger to start reading in numbers for box score
    
    box_score = open("\\path\\to\\LCBoxScores\\LC2008-2018TXT\\"+file, "r")
    line_count = 0
    
    for i in box_score:
        RHE1 = ""
        RHE2 = ""
        if line_count == 2:
            split_idx = i.index("-")
            RHE1 = i[split_idx + 1:]
            lst_of_RHE.append(RHE1.split())
        if line_count == 3:
            split_idx = i.index("-")
            RHE2 = i[split_idx + 1:]
            lst_of_RHE.append(RHE2.split())
                    
        line_count += 1
        
print(lst_of_RHE)
lst_of_final_RHEs_to_be_removed = []

for final_RHE in lst_of_RHE:
    print(final_RHE)
    if len(final_RHE) != 3:
        print(final_RHE)
        revised_final_RHE = final_RHE[-3:]
        lst_of_final_RHEs_to_be_removed.append(final_RHE)
        lst_of_RHE.append(revised_final_RHE)

for to_be_removed_element in lst_of_final_RHEs_to_be_removed:
    lst_of_RHE.remove(to_be_removed_element)

#part 2

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

for game in lst_of_RHE:
    for digit in game[0]:
        run_digit_total_dict[digit] += 1
    
    if int(game[0]) > run_max:
        run_max = int(game[0])
        
    run_total += int(game[0])
    
    for digit in game[1]:
        hit_endgame_digit_total_dict[digit] += 1
    
    hit_num_total_dict[game[1]] += 1
    
    if int(game[1]) > hit_max:
        hit_max = int(game[1])
        
    hit_total += int(game[1])
        
    for digit in game[2]:
        error_endgame_digit_total_dict[digit] += 1
    
    if int(game[2]) > error_max:
        error_max = int(game[2])
        
    error_total += int(game[2])        
    
print("Run Data:")
print(run_digit_total_dict)
print("Max: ", run_max)
print("Total: ", run_total)
print()
print("Hit Data")
print(hit_endgame_digit_total_dict)
print("number of hits: ", hit_num_total_dict)
print("Max: ", hit_max)
print("Total: ", hit_total)
print()
print("Error Data")
print(error_endgame_digit_total_dict)
print("Max: ", error_max)
print("Total: ", error_total)
print()
hit_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for number in hit_num_total_dict:
    for j in range(int(number)+1):
        for digit in str(j):
            hit_digit_total_dict[digit] += hit_num_total_dict[number]

print(hit_digit_total_dict)

error_digit_total_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for number in error_endgame_digit_total_dict:
    for j in range(int(number)+1):
        for digit in str(j):
            error_digit_total_dict[digit] += error_endgame_digit_total_dict[number]
            
print(error_digit_total_dict)


"""
To get final reccomendations, I took the maximum dicitionary from the 1-10 innings part: {'0': 20, '1': 9, '2': 5, '3': 5, '4': 3, '5': 3, '6': 2, '7': 2, '8': 1, '9': 1}, 
and I thought through the likelihood of needing various digits. This was a very "feel" process and not quantitative at all. 
I did consider special cases like sharing digits across the 1-10 section and the RHE section of the board. For example, if all the ones are used on the 1-10 side, there 
probably won't be a need for the max number of 1's possible on the RHE side (10 - not 12 because historically there has not been a game with 11 errors). 
"""