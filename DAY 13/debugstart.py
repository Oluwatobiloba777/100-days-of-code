############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21):#change the range from 20 to 21
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)#change it from 1,6 to 0,5 to have the intended output
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:# add =, then this statements will be printed if 1994 is inputed
  print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?"))#wrap the input within int or float function to avoid errors
if age > 18:
    print(f"You can drive at age {age}.")#indent the print statement, add f to make {age} display the value

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))#make it an assignment(=) instead of equals to(==)
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)#indent this line so it is within the loop
  print(b_list)

mutate([1,2,3,5,8,13])