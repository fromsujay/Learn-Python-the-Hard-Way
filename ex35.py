from sys import exit

def gold_room():
    print "\nThis room is full of gold. How much do you take ?\n"
    
    next = int(raw_input("\nPlease enter an integer value for number of gold coins : \n"))
    if next <= 100:    
        print "\nNice, you're not greedy, you win! You become a rich person.\n"
        exit(0)
    elif next > 100:
        dead("\nYou greedy bastard. You die!\n")
    else:
        dead("\nMan, learn to type a number.\n")
            
def bear_room():
    print "\nThere is a fat bear here. The bear has a jar of honey.\n"
    print "\nThe bear is standing in front of another door.\n"
    print "\nHow are you going to move the bear ?\n"
    print "\nYour only options are : taunt bear, take honey & open door.\n"
    print "\nPlease enter your response in small letters. For e.g. 'take honey'\n"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("\nThe bear looks at you then slaps your face off. You die!\n")
        elif next == "taunt bear" and not bear_moved:
            print "\nThe bear has moved from the door. You can go through it now.\n"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("\nThe bear gets pissed off and chews your leg off. You die !\n")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "\nHere you see the great evil Cthulhu.\n"
    print "\nHe, it, whatever stares at you and you go insane.\n"
    print "\nDo you flee for your life, eat your head or rub the magic lamp ?\n"
    
    next = raw_input("\nPlease enter your answer as 'flee', 'head' or 'magic lamp' in small letters")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("\nWell that was tasty! You die :( \n")
    elif "lamp" in next:
        park_bench()            
    else:
        print "\nWelcome back. You did'nt heed to the insutructions given earlier.\n"
        cthulhu_room()

def Cute_Puppers_room():
    print "\nHere you see a cute homeless pupper standing alone in a corner of the room.\n"
    print "\nShe has been alone here since being rescued.\n"
    print "\nShe is extremely happy to see you & can't stop wagging her tail.\n"

    adoption = raw_input("\nWill you adopt her ? Please answer as 'yes' or 'no' in small letters.")
    
    if adoption == 'yes': 
        print "\nYou are a great person. You win 100000 gold coins !\n"
        
    elif adoption == 'no':
        print "\nYou don't seem to have a heart.\n"
        cthulhu_room()
    else:
        print "\nA valid response is 'yes' or 'no' in small letters.\n"

def park_bench():
        print "\nA hidden door opens and you see a path leading towards a park.\n"
        print "\nThe park has beautiful trees and plants. You see an old woman sitting on a bench.\n"
        print "\nShe gives you a puzzle to solve.\n"
        print "\nAfter a local bungled heist, five suspects were being interviewed by the police.\n"
        print "\nEventually the police managed to get a confession.\n"
        print "\nBelow is a summary of their statements and it turns out that exactly 5 of these statements were true.\n"
        print "\nAdrian said: It wasn't Barry. It was Cedric.\n"
        print "\nBarry said: It wasn't Adrian. It was Derek.\n"
        print "\nCedric said: It wasn't Derek. It wasn't Barry.\n"
        print "\nDerek said: It wasn't Eric. It was Adrian.\n"
        print "\nEric said: It wasn't Cedric. It was Derek.\n"
        
        answer =raw_input("\nWho committed the crime? Please spell the names exactly like the Old lady.\n")
        
        if answer == 'Eric':
            print "\nYou cracked the puzzle. The lady gives you a pouch of 15 gold coins. God job !\n"
        elif answer != 'Eric':
            print "\nWrong anwser. The Old lady gives you a bus ticket to go back home.\n" 
        else: 
            print "\nYou didn't seem to pay attention to the instructions. Start again.\n"
            park_bench()

def dead(why):
    print why
    exit(0)
    
def start():
    print "\nYou are in a dark room.\n"
    print "\nThere is a door to your right, left & front.\n"
    print "\nWhich one do you take?\n"
    
    next = raw_input("\nPlease respond as right, left or front in small letters : \n")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    elif next == "front":
        Cute_Puppers_room()
    else:
        dead("\nYou stumble around the room until you starve.\n")


start()