import random  # import to use random function


def checkInput():
    while True:
        human = input("Rock Scissors Paper! : ")
        try:  # check that input can be convert to int type
            ihuman = int(human)
            if ihuman >= 3:
                print("You should insert 0(rock), 1(scissors), 2(paper) only. Try again")
                continue
        except:  # if input can not be convert to int type, convert the input manually.
            if (human == "rock"):
                ihuman = 0
            elif (human == "scissors"):
                ihuman = 1
            elif (human == "paper"):
                ihuman = 2
            else:
                print("Invalid Input!! Please check it")
                continue
        break
    return ihuman  # return the input that type of int

# play the game
def doGame(human):
    computer = random.randint(0, 2)
    if (human == computer):  # case : draw
        printStatus(human, computer)  # print the status
        print('Round',i,'result: Draw!')
        result = 'draw'
        return result
    # Calculate the levicivita since the game is based on the permutation
    # Rock(0) -> Scissors(1) -> Papaer(2) -> Rock(0) ->....
    levicivita = lambda i, j, k: (i - j) * (j - k) * (k - i) / 2
    other = [0, 1, 2]  # remain component of levicivita calcaulation
    other.remove(int(human))
    other.remove(int(computer))
    levi = levicivita(human, computer, other[0])

    if (levi == 1):  # case : win
        printStatus(human, computer)  # print the status
        print('Round',i,'result: You win!')
        result = 'win'
        return result

    elif (levi == -1):  # case : loose
        printStatus(human, computer)  # print the status
        print('Round',i,'result: You lose!')
        result = 'lose'
        return result

# print the status
def printStatus(human, com):
    a = 0  # for Indexing
    for tmpinput in [str(human), str(com)]:
        if (tmpinput == "0"):
            soutput = "rock"
        elif (tmpinput == "1"):
            soutput = "scissors"
        else:
            soutput = "paper"
        if (a == 0):
            print(f"You : {soutput}")
            a = a + 1  # for indexing
        else:
            print(f"Computer : {soutput}")


# -----------------------------------main--------------------------------------
print("------------------------ROCK SCISSORS PAPER ------------------------")
print("------Please enter the input as 0(rock), 1(scissors), 2(paper)------")

#input numbers for turns of game
while True:
    try:
        games = int(input("How many times do you want play?:"))
    except:
        print("Only numbers are allowed. Please try again.")
        continue
    break
if games == 0:
    print("Oh, you don't want to play game? Ok, bye")
    quit()
#execute the games
w=0
d=0
l=0
for i in range(1,games+1):

    print('-----Round',i, '!-----')
    score = doGame(checkInput())
    if score == 'draw':
        d = d + 1
    elif score == 'win':
        w = w + 1
    else:
        l = l + 1
# total score after game ends
print("-----------------------------Total score----------------------------")
print('My record:',w,'win',d,'draw',l,'lose')
print("Com's record:",games-d-w,'win',d,'draw',w,'lose')
