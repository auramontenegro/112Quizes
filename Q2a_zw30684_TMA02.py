## first task: produce a list that contains the points for each academic grade

# initialise the input list (grades) with academic and non-academic grades
grades = ['D', 'A', 'B', 'B', 'C', 'D', 'B', 'F', 'W', 'B', 'W', 'C', 'B']
#grades = ['A', 'E', 'E', 'E', 'E', 'E', 'W' 'W', 'W', 'W', 'W', 'W', 'W']

# initialise the output list (points) to the empty list
points = []

# for each input value (grade) of the input list (grades):
for grade in grades:
    # transform the input value (grade) into an output value (point) (List transformation)
    # append the output value (point) to the output list (points) (list filtering)
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
		
# print the output list (points)
print(points)
