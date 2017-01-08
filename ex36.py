from sys import argv

script, pupper_name = argv
animals = ['leopard', 'elephant', 'giraffe', 'cow', 'panther', 'horse', 'lion', 'goat']

def farm_animals():
    print """
    She starts running towards her parents' house.
    She comes across Mrs. Smith who is standing at the entrance to her farm. She gives %s a logic puzzle to solve. 
    
    The following verse spells out a word, letter by letter.  
    "My first" refers to the word's first letter, and so on.  
    What's the word that this verse describes?

    My first is in fish but not in snail
    My second in rabbit but not in tail
    My third in up but not down
    My fourth in tiara not in crown
    My fifth in tree you plainly see
    My whole a food for you and me
    """ % pupper_name 
    
    word = raw_input("\nPlease enter the word in small letters:")
    
    if word == 'fruit' or word == 'FRUIT':
        print """
        You guessed it right ! 
        Mrs. Smith shows her the shortest route to her parents' house.
        """
        river_crossing()
        
    else: 
        print """
        You guessed it wrong :(
        %s will be left in cold outside Mrs. Smith's farm until her parents come 
        to look for her. 
        """ % pupper_name
        
def river_crossing():
    print """
    After Mrs. Smith's farm she comes to a river crossing.
    Only place to cross the river is a log of wood running between the two banks.
    There are animals sitting in the meadow at the entrance to the river crossing. 
    Out of 8 animals there are only 4 intelligent animals. If the animal you choose is
    amongst the 4 intelligent ones, it will help %s cross the river by giving advice on how to walk on the log
    of wood. 
    """ % pupper_name
    
    for i in animals:
        print "%s" % i
        
    companion = raw_input("Please enter your choice of an intelligent animal in small letters: ")
    
    if companion == 'elephant' or companion == 'cow' or companion == 'horse' or companion == 'goat':
        print """
        Congratulations ! You have selected an intelligent companion.     
        It will help %s cross the river by giving advice on how to walk on the log of wood.
        """ % pupper_name
        wise_old_lady()
    
    elif companion == 'leopard' or companion == 'giraffe' or companion == 'panther' or companion == 'lion':
        print """
        Sorry :( Wrong choice. The animal you selected cannont help %s.
        %s will have to stand in the cold until her parents come looking for her. 
        """ % (pupper_name, pupper_name)
        
    else:
        print "You didn't follow the instructions. You have to start again."
        river_crossing() 

def wise_old_lady():
    print """
    Once across the river on the other side of the bank the road leads %s to a park 
    where an old lady is sitting on a bench. She gives %s a logic puzzle to solve. 
    97 baseball teams participate in an annual state tournament. 
    The champion is chosen for this tournament by the usual elimination scheme. 
    That is, the 97 teams are divided into pairs, and the two teams of each pair play against each other. 
    The loser of each pair is eliminated, and the remaining teams are paired up again, etc. 
    How many games must be played to determine a champion?
    """ % (pupper_name, pupper_name)
    
    games = int(raw_input("\nPlease enter number of games as a number:"))
    
    if games == 96:
        print "\nThat's correct! The old lady shows %s the way to the grocery store." % pupper_name
        print "\nThe grocery store is the last stage before reaching her parents' house."
        grocery_store()

    elif games != 96:
        print "\nWrong answer. But you aleast tried. The wise old lady rings %s's parents asking them to come pick her up." % pupper_name
        
    else:
        print "\nWrong answer. %s gets lost in the park and picked up by a shelter staff. :(" % pupper_name

def grocery_store():
    print """
    When she reaches the grocery store, the shopkeeper gives you another logic puzzle to solve.
    Your sock drawer contains ten pairs of white socks and ten pairs of black socks. 
    If you're only allowed to take one sock from the drawer at a time and 
    you can't see what color sock you're taking until you've taken it, 
    how many socks do you have to take before you're guaranteed to have at least one matching pair?
    """
    socks = int(raw_input("\nPlease enter number of socks as number :"))
    
    if socks == 3:
        print """
        That's correct! The shopkeeper gives %s bread that her parents' forgot on their 
        trip to village market and also shows her the way to her parents' house. They are 
        incredibly happy to see her back home. They were worried sick until now. To crown it all
        she has come back with bread that they forgot to buy at the village market. What a 
        wonderful girl %s is.
        """ % (pupper_name, pupper_name)
    
    elif socks != 3:
        print """
        Wrong answer. Since you worked hard to get here, the shopkeeper shows %s the way to
        her parents' house but doesn't give her any bread. Her parents will have to make 
        an extra trip to the grocery store to pick up some bread.
        """ % pupper_name
    
    else:
        print """
        Wrong answer. The shopkeeper calls %s's parents and asks them to pick her up.
        They are relieved to know where she is and take her home.
        """ % pupper_name 
               

def start():
    print "\n%s has been lost by her parents at the village market." % pupper_name
    print "\nYou have to help her get home. Her parents live just outside the village."

    raw_input("\nPress enter to proceed : ")
    
    farm_animals()
    

start()
