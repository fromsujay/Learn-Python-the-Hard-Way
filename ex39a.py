# create a mapping of state to abbreviation
states = {
    'Tamil Nadu': 'TN',
    'Maharashtra': 'MH',
    'Mizoram': 'MZ',
    'Arunachal Pradesh': 'ARNCHPR',
    'Jammu and Kashmir': 'JK',
    'Uttarakhand': 'UK',
}

# create a basic set of states and some cities in them
cities = {
    'TN': 'Chennai',
    'MH': 'Mumbai',
    'MZ': 'Aizwal',
    'ARNCHPR': 'Itanagar',
}

# add some more cities
cities['JK']= 'Srinagar'
cities['UK']= 'Dehradun'

# print out some cities
print '-'*10
print "JK State has: ", cities['JK']
print "UK State has: ", cities['UK']

# print some states
print '-'*10
print "Tamil Nadu's abbreviation is: ", states['Tamil Nadu']
print "Maharashtra's abbreviation is: ", states['Maharashtra']

# do it by using the state then cities dict
print '-'*10
print "Mizoram has: ", cities[states['Mizoram']]
print "Maharashtra has: ", cities[states['Maharashtra']]

# print every state abbreviation
print '-'*10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    
# print every city in state
print '-'*10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

# now do both at the same time
print '-'*10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])

print '-'*10
# safely get an abbreviation by state that might not be there
state=states.get('Haryana', None)

if not state:
    print "Sorry, no Harayana."
    
# get a city with a default value
city = cities.get('HR', 'Does Not Exist')
print "The city for the state 'HR' is: %s" % city