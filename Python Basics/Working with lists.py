# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

# pizzas = ["Chicken Trio","Pineapple","Pepproni"]
# for pizza in pizzas:
#     print("I love",pizza)

# . Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive
# for value in range(1,21):
#     print(value)

# Summing a million: Make a list of the numbers from one to one million,and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
# listOfNumbers = list(range(1,1000001))
# print(listOfNumbers)
# print(sum(listOfNumbers))
# print(min(listOfNumbers))
# print(max(listOfNumbers))

#Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
print("::::::::::::::::::::::::::::::::::::::")
# threes = list(range(3,31,3))
# for num in threes:
#     print(num)

#Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
#squares = [value**2 for value in range(1,11)]
# squares =[]
# for value in range(1,11):
#     squares.append(value**2)
# cube =[]
# for num in range(1,11):
#     cube.append(num**3)
# print(cube)
# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. 
# Print the message
# My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
fav_pizzas = ["Chicken Trio","Pineapple","Pepproni"]
fav_Friends_pizzas = fav_pizzas[:]
fav_pizzas.append("Seafood")
fav_Friends_pizzas.append("Double Cheese")

print("My favorite pizzas are:")
for pizza in fav_pizzas:
    print(pizza)
print("-----------------------------------------")
print("My friends favorite pizzas are:")
for pizza in fav_Friends_pizzas:
    print(pizza)
print("Hello")