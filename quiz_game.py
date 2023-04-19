name = input("What is your name : ")

# opening the game
print("Hello " + name + ", Welcome to my computer quiz!")

# getting the users input
playing = input("Would you like to play? ")

# checking if input is anything other than yes
if playing.lower() != "yes":
    # quit is for ending the program
    print("Okay, maybe next time :-)")
    quit() 

# if input is yes print below 
print("Okay! let the games begin :-)")    

# keep track of scores
score = 0

"""Quiz 1"""

answer = input("What does CPU stand for ? ")

# check if answer is correct 
if answer.lower() == "central processing unit":
    print("Woop! Woop!, Correct :-)")
    score +=1
else:
    print("Oops, Wrong answer :-(")


"""Quiz 2"""
answer = input("What does GPU stand for ? ")

# check if answer is correct 
if answer.lower() == "graphic processing unit":
    print("Woop! Woop!, Correct :-)")
    score +=1
else:
    print("Oops, Wrong answer :-(")


"""Quiz 3"""
answer = input("What does RAM stand for ? ")

# check if answer is correct 
if answer.lower() == "random access memory":
    print("Woop! Woop!, Correct :-)")
    score +=1
else:
    print("Oops, Wrong answer :-(")


"""Quiz 4"""
answer = input("Who created python language ? ")

# check if answer is correct 
if answer.lower() == "guido van rossum":
    print("Woop! Woop!, Correct :-)")
    score +=1
else:
    print("Oops, Wrong answer :-(")


"""Quiz 5"""
answer = input("Is the sky blue ? ")

# check if answer is correct 
if answer.lower() == "yes":
    print("Woop! Woop!, Correct :-)")
    score +=1
else:
    print("Oops, Wrong answer :-(")

# convert the score into a string
print ( name + " you got " + str(score) +  " points")

# printing the % of the score
print ( name + " your total score is " + str((score/5)*100) + "%")

