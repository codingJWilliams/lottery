import random
import time
#version 2

num1 = "x"
num2 = "x"
num3 = "x"
num4 = "x"
num5 = "x"
num6 = "x"
num7 = "x"
numCorrect = 0
stopProgram = False
numsint = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Make a custom function for checking nums as i may use more than once
def numChecker(check_string):
    right = 0
    if check_string[0] in numsint:
        right += 1
    if check_string[1] in numsint:
        right += 1
    if check_string[2] in numsint:
        right = right + 1
    if check_string[3] in numsint:
        right = right + 1
    if check_string[4] in numsint:
        right = right + 1
    if check_string[5] in numsint:
        right = right + 1
    if check_string[6] in numsint:
        right = right + 1
    if right == 7:
        return True
    else:
        return False


# Define variables
chosen = []
stopMsg = "YOU HAVE TRIED TO CHEAT THE LOTTERY SYSTEM. WOE BETIDE YE"
# input
userNumbers = input(
    '                             National Lotto! \n   -Please enter your numbers to have a chance of winning the' +
    'JACKPOT!\n\n   -Please enter 7 numbers to be in with a chance to win 1,000,000!\n>')

# input checking
try:
    userNumbers[7]
except:
    numCorrect = 1
if numCorrect == 0:
    print(stopMsg)
    stopProgram = True
else:

    allNumbers = numChecker(userNumbers)
    if not allNumbers:
        print(stopMsg)
        stopProgram = True

if not stopProgram:
    # Code for the lotto system.
    numCorrect = 0
    char1 = random.choice(nums)
    char2 = random.choice(nums)
    char3 = random.choice(nums)
    char4 = random.choice(nums)
    char5 = random.choice(nums)
    char6 = random.choice(nums)
    char7 = random.choice(nums)
    altogether = str(char1) + str(char2) + str(char3) + str(char4) + str(char5) + str(char6) + str(char7)
    if altogether[0] == userNumbers[0]:
        numCorrect += 1
        num1 = userNumbers[0]

    if altogether[1] == userNumbers[1]:
        numCorrect += 1
        num2 = userNumbers[1]

    if altogether[2] == userNumbers[2]:
        numCorrect += 1
        num3 = userNumbers[2]

    if altogether[3] == userNumbers[3]:
        numCorrect += 1
        num4 = userNumbers[3]

    if altogether[4] == userNumbers[4]:
        numCorrect += 1
        num5 = userNumbers[4]

    if altogether[5] == userNumbers[5]:
        numCorrect += 1
        num6 = userNumbers[5]
    if altogether[6] == userNumbers[6]:
        numCorrect += 1
        num7 = userNumbers[6]

    if numCorrect == 1:
        prize = "0 :("
    elif numCorrect == 2:
        prize = "10"
    elif numCorrect == 3:
        prize = "50"
    elif numCorrect == 4:
        prize = "1000"
    elif numCorrect == 5:
        prize = "50,000"
    elif numCorrect == 6:
        prize = "250000"
    elif numCorrect == 7:
        prize = "a jackpot of 1,000,000"
    else:
        prize = "nothing, sorry :-( "
    winnings = num1 + num2 + num3 + num4 + num5 + num6 + num7
    print("You won:")
    time.sleep(0.5)
    print("*drum-roll*")
    time.sleep(1.5)
    print("You've won {0}, with {1} numbers.\nThe numbers that matched were:\n~{2}".format(prize, numCorrect, winnings))
elif stopProgram:
    exit()
