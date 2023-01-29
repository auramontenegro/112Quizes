

#Initialise the input list with academic and non-academic grades
grades = ['D', 'A', 'B', 'B', 'C', 'D', 'B', 'F', 'W', 'B', 'W', 'C', 'B']

#Initialise the output list to the empty list
points = []

#For each input value of the input list
for grade in grades:
    #Transform the input value into an output value (List transformation)
    #Append the output value to the output list (list filtering)
    if grade == 'A':
            point = 4
            points = points + [4]
    elif grade == 'B':
            point = 3
            points = points + [3]
    elif grade == 'C':
            point = 2
            points = points + [2]
    elif grade == 'D':
            point = 1
            points = points + [1]
    elif grade == 'F':
            point = 0
            points = points + [0]
		
# Print the output list
print(points)
