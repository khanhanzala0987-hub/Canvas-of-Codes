# IPL Cricket Dashboard Scenario

# 2 Teams
# 4 Players
# 5 Matches

import numpy as np

arr = np.array(
   [[[88,98,78,80,77],
    [58,76,68,66,89],
    [15,69,88,74,62],
    [81,65,100,45,31]],
    [[51,55,89,65,29],
    [88,79,62,54,81],
    [91,36,64,50,80],
    [88,99,33,78,73]]]
)

# Question 1. Find total runs

print("\nTotal Run:", np.sum(arr))  


# Question 2. Find the highest scorer

highest = np.max(arr)  

for team in range(len(arr)):
    for player in range(len(arr[team])):
        if highest in arr[team][player]:
            print("\nHighest Score:", highest)
            print("Team:", team + 1)
            print("Player:", player + 1)


# Question 3. Find the total score Team Wise

print("\nTotal Run of Team One:", np.sum(arr[0]))  
print("Total Run of Team Two:", np.sum(arr[1]))


# Question 4. Find the average of each player

print("\nAverage of Players:")    

for team in range(len(arr)):
    print("\nTeam", team + 1)
    for player in range(len(arr[team])):
        avg = np.mean(arr[team][player])
        print("Player", player + 1, "Average:", avg)


#Question 5. Search for century score

found = False   

for team in range(len(arr)):
    for player in range(len(arr[team])):
        for match in range(len(arr[team][player])):
            if arr[team][player][match] >= 100:
                print("\nCentury Found")
                print("Team:", team + 1)
                print("Player:", player + 1)
                print("Match:", match + 1)
                print("Score:", arr[team][player][match])

                found = True

if found == False:
    print("No Century Found")