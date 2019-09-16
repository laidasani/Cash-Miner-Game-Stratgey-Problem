from copy import deepcopy                                   #Importing deepcopy to make a copy of the matrix
import time                                                 
start=time.time()
def finalpolicy(grid,prev_grid):                              #finalpolicy is a function that takes in grid and it's copy of previous iteration as an argument and returns the final policy
    policy=[['' for m in range(0,s)] for n in range(0,s)]     #Initializing a policy matrix to store the policy
    mid2=time.time()
    print mid2-start

    while(prev_grid!=grid):                                 #Iterating till the time the utility values of 2 iterations don't become same
        prev_grid = deepcopy(grid)                          #Prev_Grid takes the utility values of the previous iteration
        for i in range(0,s):
            for j in range(0,s):
                maximum_utility = -100000000.0

                # Wall or Terminal
                if grid[i][j] == -10000.0 or terminal[i][j] == "t":
                    if grid[i][j] == -10000.0:
                        policy[i][j] = "N"
                    else:
                        policy[i][j] = "E"

                # Not a wall or a terminal
                else:

                    #Checking for the case of Walking Up
                    if i - 1 > -1 and grid[i - 1][j] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if j + 1 < s and grid[i-1][j + 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i-1][j + 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i - 1][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "U"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if i - 1 < 0:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                            u2 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if j - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if j + 1 < s and grid[i-1][j + 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i-1][j + 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "U" 

                    #Checking for the case of Walking Down
                    if i + 1 < s and grid[i + 1][j] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 > -1 and grid[i+1][j - 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i+1][j - 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if j + 1 < s and grid[i+1][j + 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i + 1][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "D"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if i + 1 > s-1:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                            u1 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if j - 1 > -1 and grid[i+1][j - 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i+1][j - 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if j + 1 < s and grid[i+1][j + 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "D" 
                    
                    #Checking for the case of Walking Left
                    if j - 1 > -1 and grid[i][j-1] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if i - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if i + 1 < s and grid[i+1][j - 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i+1][j - 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j-1] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "L"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 < 0:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                            u2 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if i - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if i + 1 < s and grid[i+1][j - 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i+1][j - 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "L"

                    #Checking for the case of Walking Right
                    if j + 1 < s and grid[i][j+1] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if i - 1 > -1 and grid[i-1][j + 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i-1][j + 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if i + 1 < s and grid[i+1][j + 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j+1] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "R"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j + 1 > s-1:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                            u2 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if i - 1 > -1 and grid[i-1][j + 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i-1][j + 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if i + 1 < s and grid[i+1][j + 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "R" 
      
                    grid[i][j] = maximum_utility  
    mid3=time.time()
    print mid3-start 
    return policy

def finalpolicyepsilon(grid,prev_grid):                         #finalpolicyepsilon is a function that takes in grid and it's copy of previous iteration as an argument and returns the final policy using epsilon value of 0.01
    policy=[['' for m in range(0,s)] for n in range(0,s)]       #Initializing a policy matrix to store the policy

    mid2=time.time()
    print mid2-start
    epsilon=0.01                                                #Epsilon is initialized to 0.01
    while(True):                                                #Iterating till the time the delta formula is satisfied
        delta=0                                                 #Delta is initialized to 0
        prev_grid = deepcopy(grid)                              #Prev_Grid takes the utility values of the previous iteration
        for i in range(0,s):
            for j in range(0,s):
                maximum_utility = -1000000.0

                # Wall or Terminal
                if grid[i][j] == -10000.0 or terminal[i][j] == "t":
                    if grid[i][j] == -10000.0:
                        policy[i][j] = "N"
                    else:
                        policy[i][j] = "E"

                # Not a wall or a terminal
                else:

                    #Checking for the case of Walking Up
                    if i - 1 > -1 and grid[i - 1][j] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if j + 1 < s and grid[i-1][j + 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i-1][j + 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i - 1][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "U"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if i - 1 < 0:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                            u2 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if j - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if j + 1 < s and grid[i-1][j + 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i-1][j + 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "U" 

                    #Checking for the case of Walking Down
                    if i + 1 < s and grid[i + 1][j] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 > -1 and grid[i+1][j - 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i+1][j - 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if j + 1 < s and grid[i+1][j + 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i + 1][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "D"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if i + 1 > s-1:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                            u1 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if j - 1 > -1 and grid[i+1][j - 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i+1][j - 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if j + 1 < s and grid[i+1][j + 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "D" 
                    
                    #Checking for the case of Walking Left
                    if j - 1 > -1 and grid[i][j-1] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if i - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if i + 1 < s and grid[i+1][j - 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i+1][j - 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j-1] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "L"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 < 0:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                            u2 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if i - 1 > -1 and grid[i-1][j - 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i-1][j - 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if i + 1 < s and grid[i+1][j - 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i+1][j - 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "L"

                    #Checking for the case of Walking Right
                    if j + 1 < s and grid[i][j+1] != -10000.0:
                        u1 = 0.0
                        u2 = 0.0

                        if i - 1 > -1 and grid[i-1][j + 1] != -10000.0:
                            u1 = 0.5 * (1 - p) * grid[i-1][j + 1]
                        else:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                        if i + 1 < s and grid[i+1][j + 1] != -10000.0:
                            u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                        else:
                            u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j+1] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "R"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j + 1 > s-1:
                            u1 = 0.5 * (1 - p) * grid[i][j]
                            u2 = 0.5 * (1 - p) * grid[i][j]

                        else:
                            if i - 1 > -1 and grid[i-1][j + 1] != -10000.0:
                                u1 = 0.5 * (1 - p) * grid[i-1][j + 1]
                            else:
                                u1 = 0.5 * (1 - p) * grid[i][j]
                            if i + 1 < s and grid[i+1][j + 1] != -10000.0:
                                u2 = 0.5 * (1 - p) * grid[i+1][j + 1]
                            else:
                                u2 = 0.5 * (1 - p) * grid[i][j]
                        util = r + (discount_factor) * (p * grid[i][j] + u1 + u2)
                        if util > maximum_utility:
                            maximum_utility = util
                            policy[i][j] = "R" 
      
                    grid[i][j] = maximum_utility  
                    delta=max(delta,abs(grid[i][j]-prev_grid[i][j]))
        if delta < epsilon*(1-discount_factor)/discount_factor:                
            mid3=time.time()
            print mid3-start 
            return policy
    
f = open("input.txt","r")
lines = f.readlines()
grid_size = (lines[0].strip("\n"))
no_of_walls = int(lines[1].strip("\n"))
wall_position = []
for i in range(0,no_of_walls):
     wall_position.append(lines[i+2].replace("\n", "").split(","))
no_of_terminal_states = int(lines[2+no_of_walls].strip("\n"))
terminal_states_position = []
for j in range(0,no_of_terminal_states):
     terminal_states_position.append(lines[j+3+no_of_walls].replace("\n","").split(","))
p = float(lines[no_of_terminal_states+no_of_walls+3].strip("\n"))
r = float(lines[no_of_terminal_states+no_of_walls+4].strip("\n"))
discount_factor = float(lines[no_of_terminal_states+no_of_walls+5].strip("\n"))

s=int(grid_size)


grid = [[0.0 for x in range(s)] for y in range(s)]
terminal = [['' for x in range(s)] for y in range(s)]
prev_grid=deepcopy(grid)
# Placing walls in grid
for k in range(0,no_of_walls):
    a=int(wall_position[k][0])-1 
    b=int(wall_position[k][1])-1
    grid[a][b] = -10000.0


# Placing terminals in grid
for k in range(0,no_of_terminal_states):
    a=int(terminal_states_position[k][0])-1
    b=int(terminal_states_position[k][1])-1
    grid[a][b] = float(terminal_states_position[k][2])
    terminal[a][b] = "t"

mid1=time.time()
print mid1-start

if s<126:
    policy=finalpolicy(grid,prev_grid)
    print ("Without epsilon")
else:
    policy=finalpolicyepsilon(grid,prev_grid)

with open('output.txt', 'w') as file:
    for i in range(0,s):
        for j in range(0,s):
            file.write(policy[i][j])
            if j!=s-1:
                file.write(",")
            else:
                file.write("\n")


end=time.time()
print end-start