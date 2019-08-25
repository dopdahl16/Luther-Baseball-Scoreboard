import os

lst_of_inning_box_scores = []

for file in os.listdir("\\path\\to\\LCBoxScores\\LC2008-2018TXT"):
    filename = file[:-4]
    print()
    print()
    print(filename)
    
    ###GAME 249 - use "." as trigger to start reading in numbers for box score
    
    box_score = open("\\path\\to\\LCBoxScores\\LC2008-2018TXT\\"+file, "r")
    print("BOXSCORE:")
    Full_Box = []
    line_count = 0
    do_not_load_next_digit = False
    
    for i in box_score:
        if line_count == 2 or line_count == 3:
            for element in i:
                if element == "-":
                    break
                if element.isdigit() and do_not_load_next_digit == False:
                    Full_Box.append(element)
                    do_not_load_next_digit = False
                if element == "(":
                    do_not_load_next_digit = True
                else:
                    do_not_load_next_digit = False

        line_count += 1
        
    print("FULL BOX: ", Full_Box)
    lst_of_inning_box_scores.append(Full_Box)
        
print("FINAL: " , lst_of_inning_box_scores)

#part 2

count_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
max_dict =  {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
temp_dict =  {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

print()

for game in lst_of_inning_box_scores:
    temp_dict =  {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    for inning in game:
        count_dict[inning] = count_dict[inning] + 1
        temp_dict[inning] = temp_dict[inning] + 1
    for digit in temp_dict:
        if temp_dict[digit] > max_dict[digit]:
            max_dict[digit] = temp_dict[digit]
   
print("Count Dict" , count_dict)
avg_dict = count_dict.copy()

for digit in avg_dict:
    avg_dict[digit] = avg_dict[digit]/462
    
print("AVG: ", avg_dict)
print("MAX DICT : ", max_dict)