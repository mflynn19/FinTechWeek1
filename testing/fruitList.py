#LIST

favFruits = ["Mango", "Avacado", "Pineapple", "Grapes", "Pomegranate"]

favFruits.append("Orange")

enisFav = favFruits[2]

favFruits.pop(2)
#pop deletes the index 

favFruits.remove("Grapes")
#deletes the first index of the instance

favFruits[2] = "Apple"

for fruit in favFruits:
    print("I like " + fruit)
    
for fruit in range(0, len(favFruits)):
    print("I like " + favFruits[fruit])
    
print(favFruits)

#DICTIONARY

fruitCriteria = [True, 0.20, True, True, 100, "Banana", True]
#list is really bad to use bc elements are ambiguous

fruitCriteria = {
    "isFresh" : True, 
    "costPerPound" : 0.20, 
    "isRipe" : True, 
    "inSeason" : True, 
    "likeabilityScale" : 100, 
    "whatIsIt" : "Banana", 
    "allergic" : True
}
#dictionaries are better bc they have a key and value

print(fruitCriteria["allergic"])

fruitCriteria["specialFeature"] = "GMO"

for key in fruitCriteria:
    print("The answer to " + str(key) + " is " + str(fruitCriteria[key]) + ".")

print(fruitCriteria)

#importing other files
import address_book
print(address_book.contacts[6]["email"])

import address_book as ab
print(ab.contacts[6]["email"])

from address_book import contacts
print(contacts[6]["email"])