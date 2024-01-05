print("Hello World")
print("I am Syed Asad Jamil. This is my first Python Program")

# Introduction

NAME = "Syed Asad Jamil"
AGE = 21
CITY = "Lahore, Pakistan"
COUNTRY = "Pakistan"
HOBBY = ["Reading", "Writing", "Coding"]

# Print the introduction
print("\nIntroduction:")
print("Name: " + NAME)
print("Age: " + str(AGE))
print("City: " + CITY)
print("Country: " + COUNTRY)
print("Hobby: " + str(HOBBY))


# Many Values to Multiple Variables

x,y,z = "One", "Two", "Three"
print(x,y,z)


# Unpack a Collection
Numbers = ["One", "Two", "Three"]

x,y,z = Numbers
print(x,y,z)


# Output Variables

X = "Python "
Y = "is "
Z = "Awesome"
print(X + Y + Z)

X = 5
Y = 10
print(X+ Y)

# Global Variable

X = "Awesome"
def display():
    """
    This function prints the string "Python is Awesome".
    """
    print("Python is " + X)

display()
