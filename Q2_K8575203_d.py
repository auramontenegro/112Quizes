#Draw a frieze pattern
from turtle import *
number_of_elements = 7
centrex = 0
centrey = 0

for element in range (1, number_of_elements + 1):    
    #Draw a basic element with 8 spokes
    for spokes in range (1, 9):
        #Move pen to centre, starting point of element
        goto(centrex,centrey)
        forward(40)
        right(45)
        
    #Move forward to start of next element    
    penup()
    forward(100)
    #Adds 100 units to the x centre coordinate, centrex
    centrex=centrex+100
    pendown()
    
    
    
