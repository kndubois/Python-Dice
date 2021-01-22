# I, Katie Dubois, certify that all code submitted is my own work; 
# that I have not copied it from any other source. I also certify 
# that I do not allow my work to be edited, worked on, or copied by others.

import random

# defines all functions below
def rollDie(faces):
    # module to roll a single die with a variable number of faces
    # ASSUME faces is a valid positive integer, greater than 1
    roll = random.randint(1,faces)           # varies based on input
    return roll

def validateInt(min, max, prompt):
    # ASSUME min and max are valid positive integers, and that min < max
    while True:
        i = input(prompt)
        if not i.isdecimal():
            print("I'm sorry, that isn't a valid positive integer, please try again.")
        if i.isdecimal():
            if int(i) < min or int(i) > max:
                print("I'm sorry, that isn't in the range " + str(min)+" to " + str(max) + ". Please try again.")
            else:
                break
    return i

def validateStr(prompt, listOfChoices):
    # ASSUME prompt is a String and listOfChoices is a list of Strings
    while True:
        a = input(prompt)
        i = a.lower()
        lchoices = [x.lower() for x in listOfChoices]
        if i not in lchoices:
            print("I'm sorry, the choices are {}. Please pick one of them.".format(listOfChoices))
        else:
            break
    if i == lchoices[0]:
        return True
    if i == lchoices[1]:
        return False

def average(inList):
    # ASSUME inList is a list of numbers and the length of inList is > 0
    sum = 0
    for item in inList:
        sum += item
    avg = sum / len(inList)
    return avg

def calculatePercentage(sides, dice, diceRolls):
    # ASSUME sides * dice != 0, sides, dice are numbers
    # ASSUMe diceRolls is a list of numbers
    maxScore = sides * dice
    rolledSum = sum(diceRolls)
    p = rolledSum / maxScore
    return p

def isPrime(number):
    # ASSUME number is an integer
    if number < 2:
        return False
    if number % 2 == 0:
        return False

    for x in range(3,number,2):
        if number % x == 0:
            return False

    return True

def pattern1(sides, dice):
    # ASSUME sides > 0 and dice is a list of integers
    if sides >= 4:
        numDice = len(dice)
        diceVal = dice[0]
        count = 0
        for x in range(numDice):
            if diceVal != dice[x]:
                break
            else:
                count += 1
        if count == numDice:
            return True
    return False

def pattern2(sides, count, dice):
    # ASSUME sides, count are integers
    # ASSUME dice is a list of integers
    maxScore = sides * len(dice)
    if maxScore >= 20:
        if isPrime(count):
            return True
    return False

def pattern3(dice):
    # ASSUME dice is a list of integers
    if len(dice)>= 5:
        avgRounded = round(average(dice))
        count = 0
        for x in range(len(dice)):
            if dice[x] >= avgRounded:
                count += 1
        half_dice = len(dice)/2
        if count >= half_dice:
            return True
    return False

# utilizes a stragegy to break out of a nested for loop
# double for loop

def pattern4(sides, dice):
    # ASSUME dice is a list of integers
    if len(dice) > 4 and sides > len(dice):
        value_check = 1
        for x in range(len(dice)):
            breakcheck = False
            for y in range(x+1, len(dice)):
                if dice[x] == dice[y]:
                    breakcheck = True
                    value_check -= 1
                    break
            if breakcheck:
                break
        if value_check == 1:
            return True
    return False

# calls other functions

def bonusFactor(sides, count, dice):
    # ASSUME dice is a list of numbers
    # ASSUME sides, count are integers
    bonus = 0
    if pattern1(sides, dice):
        bonus += 10
    if pattern2(sides, count, dice):
        bonus += 15
    if pattern3(dice):
        bonus += 5
    if pattern4(sides, dice):
        bonus += 8

    if bonus != 0:
        return bonus
    else:
        return 1

# score of the roll, every roll will give a different score when you play again
# scores stored in a list - calculates averages of scores
# student number needed to define max score

def score(maxSides, totalDice, diceRolled):
    # ASSUME maxSides and totalDice are integers > 0
    # ASSUME diceRolled is a list of integers
    # to calculate score = [percentage of maxscore times bonusfactor ] + studentid mod 500
    p = calculatePercentage(maxSides, totalDice, diceRolled)
    bonus = bonusFactor(maxSides, totalDice, diceRolled)
    score = p * bonus
    student_id = 809647
    smod500 = student_id % 500
    fullScore = int(score) + smod500
    return fullScore

# statement to start off dice game
print("COMP 10001 - W2020 Final Project by Katie Dubois, student number #000809647.\n")
print("Hello! Welcome to my dice game. Good Luck!\n")

gameScores = []                         # Start with zero / keeps track of all scores in the game

promptFaces = "Enter # of faces [2, 20]: "
promptDice = "Enter # of dice [3, 6]: "
rangeF = [2, 20]                        # in range between 2 to 20
rangeD = [3, 6]                         # in range between 3 to 6

# validates rolling face and dice with range shown above

enterFaces = validateInt(rangeF[0], rangeF[1], promptFaces)
enterDice = validateInt(rangeD[0], rangeD[1], promptDice)

# main program, generating the game to start
# only when user no longer wants to play, will 'play' be set to False, ending the while loop

play = True
while play:
    faces = int(enterFaces)
    dice = int(enterDice)

    dieRolls = []
    for x in range(dice):
        d = rollDie(faces)
        dieRolls.append(d)

    dieSum = sum(dieRolls)
    dieAvg = round(average(dieRolls))

    print("\nYou have rolled:", dieRolls)
    print("\nThe sum of the die is", dieSum, "and have an average rounded value of {}.".format(dieAvg))

    max_score = faces * dice

    if pattern1(faces, dieRolls):
        print("Pattern 1 matched in your roll!", dieRolls, "as all dice have same value!")
    else:
        if faces < 4:
            print("Pattern 1 does not apply. Less than 4 sides.")
        else:
            print("Pattern 1 not matched in your roll:", dieRolls, "as some dice are different.")

    if pattern2(faces, dieSum, dieRolls):
        print("Pattern 2 matched!", dieSum, "is a prime number.")
    else:
        if max_score < 20:
            print("Pattern 2 does not apply. Maximum score is less than 20.")
        else:
            print("Pattern 2 not matched,", dieSum, "is not a prime number.")

    if pattern3(dieRolls):
        print("Pattern 3 matched! At least half of", dieRolls, "are greater than or equal to the average of {}.".format(dieAvg))
    else:
        if dice < 5:
            print("Pattern 3 does not apply, since there are less than 5 dice.")
        else:
            print("Pattern 3 not matched. Fewer than half of", dieRolls, "are greater or equal to average of {}.".format(dieAvg))

    if pattern4(faces, dieRolls):
        print("Pattern 4 matched in your roll!", dieRolls, "as all the dice are different values.")
    else:
        if dice<=4 or faces <= dice:
            print("Pattern 4 does not apply. Either sides <= 4 or # sides <= # dice.")
        else:
            print("Pattern 4 not matched. Some of the values in", dieRolls, "are the same.")

    bfactor = bonusFactor(faces, dieSum, dieRolls)
    points = score(faces, dice, dieRolls)
    if bfactor > 1:
        print("Since you matched a pattern, pattern 5 is not matched.")
        print("Your bonus factor is {}.".format(bfactor))
        print("These dice are worth", points, "points.")
    else:
        print("Since none of the other patterns were matched, pattern 5 is matched!")
        print("Your bonus factor is 1.")
        print("These dice are worth", points, "points.")

    print("\nYou have rolled:", dieRolls)

    # some prompts and list of choices that will be passed through the validateStr function
    # user will be asked if they want to reroll any dice. those prompts are stored in array with index corresponding to which die #
    # user will enter dice # between at minimum 3 and at most 6: the range [3, 6] is taken into account
    
    prompt_reroll = "\nDo you want to reroll any dice? ['yes', 'no']: "

    prompt_die = [" "]*6
    prompt_die[0] = "Reroll die 1? (was " + str(dieRolls[0]) + ") ['y', 'n']: "
    prompt_die[1] = "Reroll die 2? (was " + str(dieRolls[1]) + ") ['y', 'n']: "
    prompt_die[2] = "Reroll die 3? (was " + str(dieRolls[2]) + ") ['y', 'n']: "
    if len(dieRolls) > 3:
        prompt_die[3] = "Reroll die 4? (was " + str(dieRolls[3]) + ") ['y', 'n']: "
    if len(dieRolls) > 4:
        prompt_die[4] = "Reroll die 5? (was " + str(dieRolls[4]) + ") ['y', 'n']: "
    if len(dieRolls) > 5:
        prompt_die[5] = "Reroll die 6? (was " + str(dieRolls[5]) + ") ['y', 'n']: "

    prompt_sure = "Are you sure? ['yes', 'no']: "

    choiceList1 = ['Yes', 'No']
    choiceList2 = ['y', 'n']

    reroll = [False]*len(dieRolls)                 # declares an array of length by just multiplying
                                                   # however, in this case, we don't use a number; it's all dependant on the length        

    if validateStr(prompt_reroll, choiceList1):
        for x in range(len(dieRolls)):
            if validateStr(prompt_die[x], choiceList2):
                reroll[x] = True

        if validateStr(prompt_sure, choiceList1):
            for i in range(len(reroll)):
                if reroll[i] == True:
                    dieRolls[i] = rollDie(faces)

            dieSum = sum(dieRolls)               # shows total sum from how many dice were rolled
            dieAvg = round(average(dieRolls))    # shows average rounded value of the sum

            print("\nYou have rolled:", dieRolls)
            print("\nThe sum of the die is", dieSum, "and have an average rounded value of {}.".format(dieAvg))

            max_score = faces * dice

            if pattern1(faces, dieRolls):
                print("Pattern 1 matched in your roll!", dieRolls, "as all dice have same value!")
            else:
                if faces < 4:
                    print("Pattern 1 does not apply. Less than 4 sides.")
                else:
                    print("Pattern 1 not matched in your roll:", dieRolls, "as some dice are different.")

            if pattern2(faces, dieSum, dieRolls):
                print("Pattern 2 matched!", dieSum, "is a prime number.")
            else:
                if max_score < 20:
                    print("Pattern 2 does not apply. Maximum score is less than 20.")
                else:
                    print("Pattern 2 not matched,", dieSum, "is not a prime number.")

            if pattern3(dieRolls):
                print("Pattern 3 matched! At least half of", dieRolls, "are greater than or equal to the average of {}.".format(dieAvg))
            else:
                if dice < 5:
                    print("Pattern 3 does not apply, since there are less than 5 dice.")
                else:
                    print("Pattern 3 not matched. Fewer than half of", dieRolls, "are greater or equal to average of {}.".format(dieAvg))

            if pattern4(faces, dieRolls):
                print("Pattern 4 matched in your roll!", dieRolls, "as all the dice are different values.")
            else:
                if dice<=4 or faces <= dice:
                    print("Pattern 4 does not apply. Either sides <= 4 or # sides <= # dice.")
                else:
                    print("Pattern 4 not matched. Some of the values in", dieRolls, "are the same.")

            bfactor = bonusFactor(faces, dieSum, dieRolls)
            points = score(faces, dice, dieRolls)

            if bfactor > 1:
                print("Since you matched a pattern, pattern 5 is not matched.")
                print("Your bonus factor is {}.".format(bfactor))
                print("These dice are worth", points, "points.")
            else:
                print("Since none of the other patterns were matched, pattern 5 is matched!")
                print("Your bonus factor is 1.")
                print("These dice are worth", points, "points.")
            gameScores.append(points)
        else:
            gameScores.append(points)
    else:
        gameScores.append(points)

    # by this point, the game is complete and will declare a statement that you have completed a turn, and giving you the option to play again
    # gameScores array stores the score of each game in, appending each new game and len(gameScores) would tell us how many games played so far

    if len(gameScores) < 2:
        print("\nThis was your first turn, let's go again!")
    if len(gameScores) >=2:
        avg_gameScore = round(average(gameScores))
        last_gameScore = gameScores[-1]

        if last_gameScore > avg_gameScore:
            print("\nYour score of", last_gameScore, "on turn", len(gameScores), "was above average compared to other turns today.")
        if last_gameScore < avg_gameScore:
            print("\nYour score of", last_gameScore, "on turn", len(gameScores), "was below average compared to other turns today.")
        if last_gameScore == avg_gameScore:
            print("\nYour score of", last_gameScore, "on turn", len(gameScores), "was average compared to other turns today.")

        print("\nYou completed turn {}, let's do another!".format(len(gameScores))) 

        prompt_playagain = "\nWould you like to play another turn? ['y', 'n']: "
        if validateStr(prompt_playagain, choiceList2):
            continue
        else:
            print("You played", len(gameScores), "turns today with an average score of", avg_gameScore, "points.")
            play = False                             # breaks the loop to terminate the program
