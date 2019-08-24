
Teams2018 = [[16,5],[15,6],[14,8],[14,9],[13,9],[10,12],[7,16],[6,17],[5,18]]


Teams2017 = [[19,5],[17,7],[15,9],[15,9],[13,11],[12,12],[7,17],[6,18],[4,20]]


Teams2016 = [[24,4],[22,6],[17,11],[12,16],[12,16],[10,18],[8,20],[7,21]]


Teams2015 = [[20,8],[17,11],[16,12],[15,13],[14,14],[13,15],[10,18],[7,21]]


Teams2014 = [[22,6],[19,9],[17,11],[13,15],[12,16],[11,17],[9,19],[9,19]]


Teams2013 = [[20,6],[19,7],[15,13],[12,14],[12,16],[11,15],[10,18],[9,19]]


Teams2012 = [[19,5],[15,9],[14,10],[13,11],[13,11],[12,12],[11,13],[6,18],[5,19]]


Teams2011 = [[18,6],[16,8],[16,8],[13,10],[13,11],[12,12],[10,14],[8,15],[1,23]]


Teams = [Teams2018, Teams2017, Teams2016, Teams2015, Teams2014, Teams2013, Teams2012, Teams2011]


Games_Back_List = []

for year in Teams:
    rest_of_em = year[1:]
    
    FirstPlace = year[0]

    First_Place_Wins = float(FirstPlace[0])
    First_Place_Losses = float(FirstPlace[1])
    
    print()
    
    for team in rest_of_em:
        
        OtherTeamWins = float(team[0])
        OtherTeamLosses = float(team[1])
        Wins_Diff = First_Place_Wins - OtherTeamWins
        Losses_Diff = OtherTeamLosses - First_Place_Losses
        Games_Back = (Wins_Diff + Losses_Diff)/2
        Games_Back_List.append(Games_Back)

print(Games_Back_List)
digits = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0, '16':0, '17':0}
for i in Games_Back_List:
    digits[str(int(i))] += 1
    
print(digits)
for j in digits:
    print(j, ":", digits[j])