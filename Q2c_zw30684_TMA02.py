## Find GPA

# Initialise the input list (grades) with academic and non-academic grades
#grades = ['D', 'A', 'B', 'B', 'C', 'D', 'B', 'F', 'W', 'B', 'W', 'C', 'B']
#grades = ['D', 'A', 'B', 'B', 'C', 'D', 'B', 'F', 'W', 'B', 'W', 'C', 'C']
grades = ['A', 'E', 'E', 'E', 'E', 'E', 'W' 'W', 'W', 'W', 'W', 'W', 'W']

# initialise the output list to the empty list (points)
points = []

# for each input value (grade) of the input list (grades)
for grade in grades:
    # transform the input value into an output value (List transformation)
    # append the output value to the output list (list filtering)
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
		
# initialise the aggregator (total_points)
total_points = 0

# for each number (point) in the transformed list (points):
for point in points:
    # update the aggregator (total_points) according to the value of the number (point):
    total_points = total_points + point

# compute the length of the list
total_grades = len(points)

# compute the average grade to 2 d.p.
GPA = round(float(total_points / total_grades), 2)                

# print average grade
print(GPA)
