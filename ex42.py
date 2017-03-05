# Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal(object):
    i = 10
    j = 20
    k = i+j
    print "%d" %(k)

# Dog is-a animal 
class Dog(Animal):
    i = 10
    j = 20
    print (i+j)*1000

    def __init__(self, name):
        # Dog has-a name
        self.name=name
        
# Cat is-a animal
class Cat(Animal):

    def __init__(self,name):
        # Cat has-a name
        self.name=name
        
# Person is-a object
class Person(object):
    Person = ['Ankit', 'Akshay', 'Vinod', 'Viral', 'Ashok', 'Amit']
    print Person 

    def __init__(self,name):
    # Person has-a name
        self.name=name
    
    # Person has-a pet of some kind
        self.pet=None
    
# Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # hmm what is this strage magic ?
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary=salary
        
# Fish is-a object
class Fish(object):
    Fish = {
    'PSA' : 'Opel',
    'Tata Motors' : 'Jaguar',
    'GM' : 'Corvette',
    'BMW': 'Mini',
    'Mercedes':'Smart',
    'Renault':'Zoe',
    'Toyota':'Lexus' 
    }

    print Fish['PSA']
    Fish['VW'] = 'Audi'
    print Fish ['VW']
    for OEM, brand in Fish.items():
        print "\n%s owns %s brand\n" %(OEM, brand)
    
# Salmon is-a Fish
class Salmon(Fish):
    pass
    
# Halibut is-a Fish
class Halibut(Fish):
    pass
    
    
# instance of Dog that is-a "Rover"
rover = Dog("Rover")

# instance of Cat that is-a "Satan"
satan = Cat("Satan")

# instance of Person that is-a "Mary"
mary = Person("Mary")

# Take pet attribute of mary and set it to satan
mary.pet = satan

# franck is an instance of Employee that takes "Franck" & 120000 as parameters
franck = Employee("Franck", 120000)

print franck

# from franck take pet attribute and set it to rover
franck.pet=rover

# flipper is an instance of class Fish
flipper = Fish()

# crouse is an instance of class Salmon
crouse=Salmon()

# harry is an instance of class Halibut 
harry = Halibut()     
