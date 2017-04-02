from sys import exit
from random import randint


class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
    
        while current_scene is not None:
            print "\n------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            print current_scene
            
        else:
            print "The End"
            exit(1) 

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Tavern(Scene):
    
    def enter(self):
        print "You live in a kingdom ruled by an evil king."
        print "Fellow subjects have given you the mission to enter the castle,"
        print "kill the evil king and retrieve the ruby studded bracelet his evil"
        print "soldiers stole from you. You have to gather information from"
        print "other subjects who are eating & drinking in the tavern. At the end of the"
        print "tavern there is a secret entrance to the castle. But this entrance is"
        print "guarded by one of kings' soldiers."
        print "\n"
        print "On seeing you approach the secret entrance, the soldier takes out his"
        print "sword and asks you to make yourself scarce or he will cut you down."
        print "You have the following options : pepper spray, sword fight or dodge."
        print "What do you do ?"  
         
        tavern_entrance = raw_input("> ")
        
        if tavern_entrance == "pepper spray":
            print "Great decision !  The soldier starts shouting because of the pain"
            print "and bangs his head against the wall and is disabled leaving you the path"
            print "clear to enter the castle."
            return 'food_store'
        
        elif tavern_entrance == "sword fight":
            print "The evil king trains his soldiers very well. He is extremely strong and"
            print "overpowers you and kills you. You are dead."
            return 'death'
        
        elif tavern_entrance == "dodge":
            print "Inspite of dodging the soldier, he chases you and catches you while"
            print "entering the castle and kills you with his deadly sword."
            return 'death'
        
        else:
            print "Does not compute :("
            return 'tavern'
        
                  
class FoodStore(Scene):

    def enter(self): 
        print "The secret entrance from the tavern leads you to the food store of the castle."
        print "You run to a corner of the food store to scan the store and examine your"
        print "options. You see that there are three doors leading into other parts of the"
        print "castle. Which door do you chosse : A, B or C ?" 
        
        door_selection = raw_input("> ")
        
        if door_selection == "A":
            print "You enter a dark passage with sounds of dangerous animals coming"
            print "from all the far end of the passage. As you move forward you realize"
            print "that this is a trick and you fall into a trap. Three fierce"
            print "soldiers attack and kill you in a matter of minutes."
            return 'death'
            
        elif door_selection == "B":
            print "This looks like a promising option but isn't. As you move forward"
            print "you realize that it brings you back to the foodstore."
            return 'food_store'
            
        elif door_selection == "C":
            return 'soldiers_dormitory'            
        
        else: 
            print "Does not compute :("
            return 'food_store'
            
        
class SoldiersDormitory(Scene):
    
    def enter(self):
    
        print "Here you find 5 soldiers relaxing off-duty. All the others are on duty"
        print "guarding different parts of the castle. They are suprised to find you"
        print "standing there with a sword. You have two options : 'Fight them' or"
        print "'hand wrestle' all of them one by one. Which one do you choose ?"
        
        soldiers_dormitory_action = raw_input("> ")
        
        if soldiers_dormitory_action == 'Fight them':
            print "You fight valiantly with your sword and succeed in killing three"
            print "of the soldiers. But the remaining two succeed in killing you."
            return 'death'
            
        elif soldiers_dormitory_action == 'hand wrestle':
            print "Incidently you are exceptionally good at hand wrestling"
            print "You beat all five soldiers & out of respect they let you into the"
            print "king's living room."
            return 'kings_livingroom'
        
        else:
            print "Does not compute"
            return 'soldiers_dormitory'
            
 
class KingsLivingroom(Scene):
    
    def enter(self):
        print "You have entered the King's living room. He is standing next to his writing"
        print "table. Your fellow subjects in the tavern have informed you that the King is"
        print "a great sword fighter. That is clearly a tactic that you want to avoid. You"
        print "have two options : tickle or judo. Which one do you select ?"
    
        kings_challenge = raw_input("> ")  

        if kings_challenge == 'tickle':
            print "You start tickling the king but the he quickly regains composure and"
            print "hits you hard with his sword and you die."
            return "death"
        
        elif kings_challenge == 'judo':
            print "The king accepts your challenge to battle with you in a judo fight."
            print "You are good judo fighter and beat the king with your superior skills"
            print "developed through rigorous training."
            print "\n"
            print "After knocking out the king, you see the door to the treasure room"
            print "where the ruby studded bracelet has been hidden."
            return 'treasure_room'
    
        else:
            print "Does not compute"
            return 'kings_livingroom'


class TreasureRoom(Scene):
    
    def enter(self):
        print "The bracelet is hidden in a metallic safe. You have to give the right answer"
        print "to the following riddle. If you do, the ruby studded bracelet is yours."
        print "If you don't, you go back to the tavern to start all over again."
        print "At a recent bowling match, two games were played. Kev beat Stuart" 
        print "in both games, also Richard beat John in both games."
        print "The winner in game 1 came second in game 2. Richard won game 2 and" 
        print "John beat Stuart in game 1. No player got the same placing twice."
        print "Who stood first in the first game ?"
        
        riddle = raw_input("> ")
        
        if riddle != 'Kev':
            print "The metallic safe remains locked and you return to the tavern"
            print "where you started."
            return 'tavern'
        
        else: 
            print "You win. You have not only killed the evil king but also recovered"
            print "your ruby studded bracelet. You return to the village as a hero."
            return 'finished'

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Such a loser.",
        "I have a small puppy that's better at this."
        "Game over."
    ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips))]
        exit(1)

class Map(object):

    scenes = {
    'tavern' : Tavern(),
    'food_store' : FoodStore(),
    'soldiers_dormitory' : SoldiersDormitory(),
    'kings_livingroom' : KingsLivingroom(),
    'treasure_room' : TreasureRoom(),
    'death' : Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('tavern')
a_game = Engine(a_map)
a_game.play()