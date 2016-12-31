villes = ['New Delhi', 'Mumbai', 'Kolkatta', 'Chennai', 'Hyderabad', 'Pune', 'Bangalore', 'Pondicherry']

print "\nPlease keep in mind that there are only 8 elements in this list."

cardinal_position = int(raw_input("\nPlease enter random position of ville in list from 0 to 7: "))
ordinal_position = raw_input("\nPlease enter rank of ville in the list in letters: ")

print "\nName of ville corresponding to this position is %s" % villes[cardinal_position]

i = cardinal_position+1
if i == 1:
    print "\nSelected element is %dst in the list." % i

elif i <= 8:
    print "\nRank of selected element is %dth in the list." % i

else: 
    print "\nYou are an idiot. I told you there were only eight elements in this list."
    

if ordinal_position == 'first' or ordinal_position == 'FIRST':
    j = 0
    print "\nName of ville at first position is %s\n" % villes[j]

elif ordinal_position == 'second' or ordinal_position == 'SECOND':
    j = 1
    print "\nName of ville at second position is %s\n" % villes[j]
    
elif ordinal_position == 'third' or ordinal_position == 'THIRD':
    j = 2
    print "\nName of ville at third position is %s\n" % villes[j]
    
elif ordinal_position == 'fourth' or ordinal_position == 'FOURTH':
    j = 3
    print "\nName of ville at fourth position is %s\n" % villes[j]
    
elif ordinal_position == 'fifth' or ordinal_position == 'FIFTH':
    j = 4
    print "\nName of ville at fifth position is %s\n" % villes[j]

elif ordinal_position == 'sixth' or ordinal_position == 'SIXTH':
    j = 5
    print "\nName of ville at sixth position is %s\n" % villes[j]
    
elif ordinal_position == 'seventh' or ordinal_position == 'SEVENTH':
    j = 6
    print "\nName of ville at seventh position is %s\n" % villes[j]
    
elif ordinal_position == 'eighth' or ordinal_position == 'EIGHTH':
    j = 7
    print "\nName of ville at eighth position is %s\n" % villes[j]
    
else:
    print "\nYou are an idiot. I told you there were only eight elements in this list.\n"