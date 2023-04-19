# this is a module
import random

# print a random number
""" one way to get a random number """
""" randrange does not inclue the max number"""
# r = random.randrange(-5, 11)
# print(r)

""" another way to get a random number"""
""" randint includes the max number"""







# ask user to print number
name = input("what is your name : ")


top_of_range = input(name + " could you type any number: ")

# check if value is a digit
if top_of_range.isdigit():
    # convert to integer
    top_of_range = int(top_of_range)

    # check if value is less than zero
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
# if its not a digit quit
else:
    print('Please type a number next time.')
    quit()    

# generate the random number typed
random_number = random.randint(0,top_of_range)   

# keep track of guesses
guess_track = 0


# to ensure that the user guesses the value true to the random number
while True:
    user_guess = input("Make a guess of any number: ")
    guess_track +=1

    # ensure what you have typed is a number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')

        # continue does not end the loop just returns it back to the top  
        continue
    if user_guess == random_number:
        print("You got it!")
        # used to break the loop 
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You are below the number")

print( name," you got it in ",guess_track, "guesses")