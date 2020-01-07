class earthling():
    #Class Attributes
    species = "human"
    #Instance ATTRIBUTES
    def __init__(self, name, age, gender, eyeColor, city):
        self.name = name
        self.age = age
        self.gender = gender
        self.eyeColor = eyeColor
        self.city = city
    #Instace METHOD
    def run(self, mph):
        return "{} is running {}".format(self.name, mph) #MPH is defined by what you type in. Not stored in a Instance variable.

#Create INSTANCES with unique instance attributes. 
Isaac = earthling("Isaac", 23, "male", "brown", "Des Moines")
Jacob = earthling("Jacob", 27, "male", "brown", "Des Moines")
Zach = earthling("Zach", 30, "male", "brown", "Des Moines")
Sarah = earthling("Sarah", 39, "female", "gray", "Des Moines")

#This takes calls from the Class Attributes, NOT INSTANCE attributes
print("Isaac is a {}".format(Isaac.__class__.species))
print("Jacob is also a {}".format(Jacob.__class__.species))

# {} and its corresponding attributes go in the order they are called.
#This takes calls from INSTANCE attributes, NOT CLASS attributes.
print("{} is {} years old.".format(Isaac.name,Isaac.age))

print("{} is a {} {} from {}. He is {} years old and has {} eyes.".format(Isaac.name, Isaac.__class__.species, Isaac.gender, Isaac.city, Isaac.age, Isaac.eyeColor))
print("{} is a {} {} from {}. He is {} years old and has {} eyes.".format(Jacob.name, Jacob.__class__.species, Jacob.gender, Jacob.city, Jacob.age, Jacob.eyeColor))
print("{} is a {} {} from {}. She is {} years old and has {} eyes.".format(Sarah.name, Sarah.__class__.species, Sarah.gender, Sarah.city, Sarah.age, Sarah.eyeColor))

print(Isaac.run("11 miles per hour"))
