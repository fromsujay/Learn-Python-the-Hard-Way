i = 0
numbers = []
progression = []
matrix = []

# Program using while loop
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1 
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i 
    
print "The numbers: "

for num in numbers: 
    print num 

# Program using while loop embedded into a function     
def iteration(j, k, l):
    while j < k:
        print "At the top j is %d" % j 
        progression.append(j)
        j = j+l
        print "Numbers now: ", progression
        print "At the bottom j is %d" % j 

j = int(raw_input("Please enter starting value:"))
k = int(raw_input("Please enter max limiting value:"))
l = int(raw_input("Please enter value of incrementor:")) 
iteration(j, k, l)    
    
print "The numbers: "

for num in progression:
    print num

# Program using for loop embedded into a function 
def generator():
    for n in range(0, 6):
        print "Adding %d to list." % n
        matrix.append(n)
        
    for m in matrix:
        print "Number element in list is : %d" % m
 
generator()