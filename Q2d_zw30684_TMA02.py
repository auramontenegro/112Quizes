# initialise the input list (grades) with academic and non-academic grades
grades = ['D', 'A', 'B', 'B', 'C', 'D', 'B', 'F', 'W', 'B', 'W', 'C', 'B']

# set counter to zero
A=0
B=0
C=0
D=0
F=0

# for each item in the list:
for grade in grades:
    if grade == 'A':
        A = A + 1
    elif grade == 'B':
        B = B + 1
    elif grade == 'C':
        C = C + 1
    elif grade == 'D':
        D = D + 1
    elif grade == 'F':
        F = F + 1

# multiply each counter by the weight of the grade
A_points= 4 * A
B_points= 3 * B
C_points= 2 * C
D_points= 1 * D
F_points= 0 * F

# sum of points
total_points = A_points + B_points + C_points + D_points + F_points

# sum of all the counters, total number of grades
total_grades = A + B + C + D + F

# compute GPA
GPA = round(float(total_points / total_grades), 2)

# print average grade
print(GPA)
