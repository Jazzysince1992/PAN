#Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •	 Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# •	 Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


alien_color = "red"
# Alien Colors #3: Turn your if-else chain from previous excercise into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
if alien_color == "green":
    print("You just earned 5 points")
# •	 If the alien is yellow, print a message that the player earned 10 points.
elif alien_color=="yellow":
    print("You just earned 10 points")
# •	 If the alien is red, print a message that the player earned 15 points.
elif alien_color=="red":
    print("You just earned 15 points")
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
age =34
# Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is a baby.
if age <2:
    print("You are a baby")
# •	 If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
elif age >=2 and age<4:
    print("You are a toddler")
# •	 If the person is at least 4 years old but less than 13, print a message that the person is a kid.
elif age >=4 and age<13:
    print("You are a kid")
# •	 If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
elif age >=13 and age<20:
    print("You are a teenager")
# •	 If the person is at least 20 years old but less than 65, print a message that the person is an adult.
elif age >=20 and age<65:
    print("You are a adult")
# •	 If the person is age 65 or older, print a message that the person is an elder.
else:
    print("You are a elder")




# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement# such as You really like bananas!
favorite_fruits = ["Apple","Banana","Kiwi"]
if "Banana" in favorite_fruits:
    print("Do you really like Banana")