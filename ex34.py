animals = ['bear', 'python','peacock', 'kangaroo', 'whale', 'platypus']

print "\nPlease note that there are only 6 elements in this list.\n"

cardinal_position = int(raw_input("\nPlease enter random position of animal in this list from 0 to 5 : \n"))

print "\nRemember to enter all letters in small or all letters in capital.\n"

ordinal_position = raw_input("\nPlease enter rank of animal in this list : ")

print "\nAnimal corresponding to this position is %s" % animals[cardinal_position]

i = cardinal_position+1
if i == 1:
    print "\nSelected element is %dst in the list." % i

elif i <= 6:
    print "\nRank of selected element is %dth in the list." % i

else: 
    print "\nYou are an idiot. I told you there were only six animals in this list."
    

if ordinal_position == 'first' or ordinal_position == 'FIRST':
    j = 0
    print "\nName of animal at first position is %s\n" % animals[j]

elif ordinal_position == 'second' or ordinal_position == 'SECOND':
    j = 1
    print "\nName of animal at second position is %s\n" % animals[j]
    
elif ordinal_position == 'third' or ordinal_position == 'THIRD':
    j = 2
    print "\nName of animal at third position is %s\n" % animals[j]
    
elif ordinal_position == 'fourth' or ordinal_position == 'FOURTH':
    j = 3
    print "\nName of animal at fourth position is %s\n" % animals[j]
    
elif ordinal_position == 'fifth' or ordinal_position == 'FIFTH':
    j = 4
    print "\nName of animal at fifth position is %s\n" % animals[j]

elif ordinal_position == 'sixth' or ordinal_position == 'SIXTH':
    j = 5
    print "\nName of animal at sixth position is %s\n" % animals[j]
        
else:
    print "\nYou are an idiot. I told you there were only six animals in this list.\n"