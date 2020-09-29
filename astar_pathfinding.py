import math                                             #Importing necessary modules
import heapq

array = [[(0,0), (4,0), (0,4)],                         #Array containing list of coordinates forming obstacles
         [(4,0), (0,0), (4,4), (7,4), (9,6)],           
         [(4,4), (0,4), (4,0), (7,4), (2,8)],         
         [(0,4), (0,0), (4,4), (2,8)],
         [(2,8), (0,4), (4,4), (4,10), (7,4)],
         [(4,10), (2,8), (9,6)],
         [(7,4), (4,0), (4,4), (2,8), (9,6)],
         [(9,6), (4,0), (7,4), (4,10)]]


def allowed(current):                       #Function to return list of allowed coordinates given current coordinate as input
    for row in range(len(array)):
        if current == array[row][0]:
            legal = array[row]
            return legal[1:]


def distance(a,b):                                                  #Function to calculate distance between coordinates
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

dataset = open("DatasetPr1.txt", "r")           #Opening text file containing coordinates
start = dataset.readline()                      #Reading start coordinates
start = (int(start[0]), int(start[2]))          #Storing start coordinate as tuple
end = dataset.readline()                        #Reading end coordinates
end = (int(end[0]), int(end[2]))                #Storing end coordinate as tuple
dataset.close()                                 #Closing file

f = {start: distance(start, end)}       #Dictionary holding coordinates and their corresponding f-value
g = {start: 0}                          #Dictionary holding coordinates and their corresponding g-value
minheap = []                            #Initializing heap to hold and later return minimum f-value coordinates
explored = set()                        #Set holding explored coordinates which do not have to be visited again
route = {}                              #Dictionary holding parent coordinate for current route

def search():                                           #A* search function

    heapq.heappush(minheap, (f[start], start))          #Pushing f-values and corresponding coordinate onto heap

    while minheap:                                      #Loop until minheap is empty
        current = heapq.heappop(minheap)[1]             #Pop current least f-valued coordinate onto variable
        legal = allowed(current)                        #Get list of coordinates to where movement is allowed
        if current == end:                              #Loop to return path when end coordinate reached
            path = []                                   #Variable to hold parent coordinates for current route
            while current in route:                     #Looping to call parent coordinates
                path.append(current)                    #Coordinates appended to list one by one
                current = route[current]                #Calling parent coordinate value to variable from current coordinate key
            path = path + [start]                       #Manually adding start coordinates to path list as not stored in route dictionary
            path = path[::-1]                           #Parents coordinates were appended to the end of the list, so reversing
            return path                                 #Returning path

        explored.add(current)                           #Putting current coordinate to explored set

        for a,b in legal:                                            #Loop for all allowed coordinates
            next = a,b                                               #Extracting and putting allowed coordinate in variable
            nextg = g[current] + distance(current, next)             #Calculating g-score of allowed coordinate
            if next in explored:                                     #If extracted coordinate in list of already explored, then
                continue                                             #ignore and continue to next allowed coordinate

            if next not in [a[1] for a in minheap]:                                 #If unexplored coordinate then put into heap
                route[next] = current                                               #Adding coordinate to route dictionary
                g[next] = nextg                                                     #G-score attributed to next coordinate
                f[next] = nextg + distance(next, end)                               #F-score attributed to next coordinate
                heapq.heappush(minheap, (f[next], next))                            #Push into minheap F-score and coordinate


path = search()            #Running A* search function and retrieving answer
z = 0                      #Print loop iterating variable

for p in path:                                              #Printing coordinates one by one
    print(str(path[z]) + " | F-Value : " + str(g[p]))
    z += 1




