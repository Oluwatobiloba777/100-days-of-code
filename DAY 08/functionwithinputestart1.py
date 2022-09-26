# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hi there, the world is selfish")
    print("Hi there, the world is selfish")
    print("Hi there, the world is selfish")
greet()

#Function that allows for input
#'name' is the parameter.
#'Oluwatobiloba' is the argument.
def greetWithName(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greetWithName("Oluwatobiloba")

#Functions with more than 1 input
def greetWith(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greetWith() with Positional Arguments
greetWith("Oluwatobiloba", "United Kingdom")
#vs.
greetWith("United Kingdom", "Oluwatobiloba")


#Calling greetWith() with Keyword Arguments
greetWith(location="London", name="Angela")
