import random
import time
#version 2 compacted

correct = ['x','x','x','x','x','x','x']
numCorrect = 0
stopProgram = False
numsint = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def numChecker(check_string):
    right = 0
    for i in range(7):
        if check_string[i] in numsint:
            right += 1
    if right == 7:
        return True
    else:
        return False
chosen = []
userNumbers = input('                             National Lotto! \n   -Please enter your numbers to have a chance of winning the' + 'JACKPOT!\n\n   -Please enter 7 numbers to be in with a chance to win 1,000,000!\n>')
try:
    userNumbers[7]
except:
    numCorrect = 1
if numCorrect == 0:
    print("YOU HAVE TRIED TO CHEAT THE LOTTERY SYSTEM. WOE BETIDE YE")
    stopProgram = True
else:
    allNumbers = numChecker(userNumbers)
    if not allNumbers:
        print("YOU HAVE TRIED TO CHEAT THE LOTTERY SYSTEM. WOE BETIDE YE")
        stopProgram = True
if not stopProgram:
    # Code for the lotto system.
    numCorrect = 0
    chars = []
    for i in range(7):
        chars.append(random.choice(numsint))
    compnum = sum(chars)
    if compnum[0] == userNumbers[0]:
        numCorrect += 1
        correct[0] = userNumbers[0]
    if compnum[1] == userNumbers[1]:
        numCorrect += 1
        correct[1] = userNumbers[1]
    if compnum[2] == userNumbers[2]:
        numCorrect += 1
        correct[2] = userNumbers[2]
    if compnum[3] == userNumbers[3]:
        numCorrect += 1
        correct[3] = userNumbers[3]
    if compnum[4] == userNumbers[4]:
        numCorrect += 1
        correct[4] = userNumbers[4]
    if compnum[5] == userNumbers[5]:
        numCorrect += 1
        correct[5] = userNumbers[5]
    if compnum[6] == userNumbers[6]:
        numCorrect += 1
        correct[6] = userNumbers[6]
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
    print("You won:")
    time.sleep(0.5)
    print("*drum-roll*")
    time.sleep(1.5)
    print("You've won {0}, with {1} numbers.\nThe numbers that matched were:\n~{2}".format(prize, numCorrect, winnings = correct[0] + correct[1] + correct[2] + correct[3] + correct[4] + correct[5] + correct[6]))
elif stopProgram:
    exit()
