## second task: calculate and print out the Grade Point Average (GPA) rounded to 2 decimal places

# initialise input list (points)
points = [1, 4, 3, 3, 2, 1, 3, 0, 3, 2, 3]

# initialise the aggregator with a suitable value 
total_points = 0

# for each number (point) in the list (points):
for point in points:
    # update the aggregator (total_points) according to the value of the number (point)
    total_points = total_points + point

# compute the length of the list
total_grades = len(points)

# compute the average grade
GPA = round(float(total_points / total_grades), 2)                

# print average grade
print(GPA)
