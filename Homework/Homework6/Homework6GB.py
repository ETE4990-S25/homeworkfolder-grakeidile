#Basic Lambda Function
#  Create a lambda function that takes one arguments and returns even or odd.
#Advanced lambda Function
#  Create a lambda function that takes a list and returns their sum 
#Sorting with Lambda
#Filtering with Lambda - `filter()` 
#Mapping with Lambda - `map()`
#Reducing with Lambda -  `reduce()` 
#Enumerate with or without Lambda - `enumerate()`
#zip with or without lambda (may combine enumerate like in class) - `zip()`

even_odd = lambda x: 'The numer is even' if x % 2 == 0 else 'The number is odd'
print (even_odd(5))


#summing = lambda x: list = [1,2,3,4,5] sum(list)
#^attempt #1 
summing = lambda list: sum(list) 
listoffun = [2,4,3,5,1]
print('The sum of the list is: ', summing(listoffun))


#sorted(listoffun)
#print('Sorted fun list', listoffun)
#figuring out sort function
listoffun.sort(key=lambda x: x, reverse=False)
print ('Lambda sorted list:', listoffun)

#figuring out when and when not to use key
filteredlist = list(filter(lambda x: (x % 2 == 0), listoffun))
print ('Lambda filtered list: ', filteredlist)

#looking at examples from the web, essentially adds a function to each item in the list independently, i thought it was literally mapping lol
squared = list(map(lambda x: x**2, listoffun))
print('Lambda mapped list:', squared)

from functools import reduce #only way i could get reduce to go through, why this imported and not the others?
sumbutweirder = reduce(lambda x,y: x + y, listoffun)
print ('Lambda reduced list: ', sumbutweirder)

#this one works better inexample with words, however i see how this would be great for a decoding type thing in a game
listofwords = ['what', 'the', 'heck', 'is', 'this']
for i, word in enumerate(listofwords):
    print(f"Place {i}: {word}")
#i could use lambda but given the option not to this felt simpler

#i couldnt find your zip example from class, but found a simple one on geeks for geeks
alltogetherbaby = zip(listoffun, listofwords)
print(list(alltogetherbaby))

#mostly i based the code on examples from forums by people asking similar questions, after attempting myself
#only for the list did i consult the evil ai after trying myself a few times
