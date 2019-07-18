#Write a function that will ask a user for their NAME and FAVORITE ice cream flavor, 
#and will return a string that says their name and whether or not they have good taste in ice cream.

def checkTaste(favorite):
    if (favorite.upper() == "CHOCOLATE"):
        return "Oooo I like you..."
    elif (favorite.upper() == "VANILLA"):
        return "Isn't it such a classic?"
    elif (favorite.upper() == "STRAWBERRY"):
        return "Fruits? In a dessert? Too healthy."
    elif (favorite.upper() == "COFFEE"):
        return "Meh.It's okay."
    else:
        return "What is that flavor? Weird."
        
print(checkTaste("strawberry"))