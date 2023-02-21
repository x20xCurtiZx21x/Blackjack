#blackjack.py 

import random

deck = ["ACE♠","KING♠","QUEEN♠","JACK♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","ACE♣","KING♣","QUEEN♣","JACK♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","ACE♥","KING♥","QUEEN♥","JACK♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","ACE♦","KING♦","QUEEN♦","JACK♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦"]

def drawCard(numLeft):

    num = random.randint(0, numLeft)

    return num

def numCheck(card):

    if card == "KING♠" or card == "QUEEN♠" or card == "JACK♠" or card == "KING♣" or card == "QUEEN♣" or card == "JACK♣" or card == "KING♥" or card == "QUEEN♥" or card == "JACK♥" or card == "KING♦" or card == "QUEEN♦" or card == "JACK♦":

        return 10

    elif card == "10♠" or card == "10♣" or card == "10♥" or card == "10♦":

        return 10

    elif card == "9♠" or card == "9♣" or card == "9♥" or card == "9♦":

        return 9

    elif card == "8♠" or card == "8♣" or card == "8♥" or card == "8♦":

        return 8 

    elif card == "7♠" or card == "7♣" or card == "7♥" or card == "7♦":

        return 7    

    elif card == "6♠" or card == "6♣" or card == "6♥" or card == "6♦":

        return 6   

    elif card == "5♠" or card == "5♣" or card == "5♥" or card == "5♦":

        return 5   

    elif card == "4♠" or card == "4♣" or card == "4♥" or card == "4♦":

        return 4              
             
    elif card == "3♠" or card == "3♣" or card == "3♥" or card == "3♦":

        return 3              

    elif card == "2♠" or card == "2♣" or card == "2♥" or card == "2♦":

        return 2

    elif (card == "ACE♠" or card == "ACE♣" or card == "ACE♥" or card == "ACE♦"):

        return 11              

    elif (card == "(11)ACE♠" or card == "(11)ACE♣" or card == "(11)ACE♥" or card == "(11)ACE♦"):

        return 11

    else:

        return 1              

def aceCheck(cards):

    new_cards = cards

    temp = []

    remove = 0

    count = 0

    for i in cards:

        if (i == "ACE♠" or i == "ACE♣" or i == "ACE♥" or i == "ACE♦"):

            temp.append(i)

            new_cards.remove(i)

            remove += 1

    sum = 0

    for i in new_cards:

        sum = sum + numCheck(i)

    if (sum <= 10) and (remove > 0):

        count = 0

        for i in temp:

            if count == 0:

                new_cards.append("(11)"+i)

                count += 1

            else:

                new_cards.append(i)

        if remove > 1:

            new_cards = aceCheck(new_cards)

    if (sum > 10) and (remove > 0):

        for i in temp:

            new_cards.append("(1)"+i)

    return new_cards

def newSum(cards):

    sum = 0

    for i in cards:

        sum = sum + numCheck(i)

    return sum

def createDeck(decknum):

    new_deck = []
    
    while decknum >= 1:

        for i in deck:

            new_deck.append(i)

        decknum -= 1

    return new_deck

def startGame(userDeck, deckLength):

    print("")

    try:

        userChoice = int(input("What is your bet?: "))

    except:

        userChoice = 0

    print("")

    if userChoice != 0:

        dcards = []

        pcards = []

        numLeft = deckLength - 1

        cardnum = drawCard(numLeft)

        card = userDeck[cardnum]

        pcards.append(card)

        userDeck[cardnum] = 0

        userDeck.remove(0)

        numLeft -= 1

        cardnum = drawCard(numLeft)

        card = userDeck[cardnum]

        dcards.append(card)

        userDeck[cardnum] = 0

        userDeck.remove(0)

        numLeft -= 1

        cardnum = drawCard(numLeft)

        card = userDeck[cardnum]

        pcards.append(card)

        userDeck[cardnum] = 0

        userDeck.remove(0)

        numLeft -= 1

        cardnum = drawCard(numLeft)

        card = userDeck[cardnum]

        dcards.append(card)

        userDeck[cardnum] = 0

        userDeck.remove(0)

        numLeft -= 1

        hasace = 0

        pcardsum = numCheck(pcards[0]) + numCheck(pcards[1])

        if pcardsum > 21:

            pcards = aceCheck(pcards)

            pcardsum = newSum(pcards)

        dcardsum = numCheck(dcards[0]) + numCheck(dcards[1])

        if dcardsum > 21:

            dcards = aceCheck(dcards)

            dcardsum = newSum(dcards)

        if dcardsum != 21 and pcardsum != 21:

            stand = 0          

            while pcardsum < 21 and stand == 0:

                print(f"Here are your cards: {pcardsum}")

                for item in pcards:

                    print(item)

                print("")

                print("Dealer's Cards:")

                print(dcards[0])

                print("Hidden")    

                print("")

                userChoice = input("Hit or Stand?: ")  

                print("")

                if userChoice.lower() == "hit":

                    cardnum = drawCard(numLeft)

                    numLeft -= 1

                    card = userDeck[cardnum]

                    pcards.append(card)

                    userDeck[cardnum] = 0

                    userDeck.remove(0)

                    length = len(pcards)

                    pcardsum = pcardsum + numCheck(pcards[length - 1])

                    if pcardsum > 21:

                        pcards = aceCheck(pcards)

                        pcardsum = newSum(pcards)

                else:

                    stand = 1

            if pcardsum <= 21:

                while dcardsum < 17:

                        cardnum = drawCard(numLeft)

                        numLeft -= 1

                        card = userDeck[cardnum]

                        dcards.append(card)

                        userDeck.remove(card)

                        length = len(dcards)

                        dcardsum = dcardsum + numCheck(dcards[length - 1])

                        if dcardsum > 21:

                            dcards = aceCheck(dcards)

                            dcardsum = newSum(dcards)

        print(f"Here are your cards: {pcardsum}")

        for item in pcards:

            print(item)

        print("")

        print(f"Dealer's Cards: {dcardsum}")

        for item in dcards:

            print(item) 

        print("")

        if dcardsum == pcardsum:

            print("IT'S A DRAW") 

        elif pcardsum > 21:

            print("DEALER WINS")

        elif dcardsum > 21:

            print("PLAYER WINS")

        elif dcardsum == 21:

            print("DEALER WINS") 

        elif pcardsum > dcardsum:

            print("PLAYER WINS")

        else:

            print("DEALER WINS")

    else:

        print("Sorry, Invalid Input")

def menu():

    num = 1

    print("====Welcome to Blackjack!====")

    while num == 1:

        print("")

        print("1) SIngleplayer")

        print("2) Multiplayer")

        print("3) Exit")

        print("")

        try:

            userInput = int(input("Enter an Option: "))

        except:

            userInput = 0

        if userInput == 1:

            try:

                print("")

                decknum = int(input("How many decks should be used?: "))

                if decknum > 0:

                    userDeck = createDeck(decknum)

                    deckLength = len(userDeck)

                    startGame(userDeck, deckLength)

                else:

                    print("")

                    print("The Amount of Decks must be Greater than 0!")

            except:

                print("Sorry, Invalid Input")

        elif userInput == 2:

            print("")

            print("Work in Progress")

        elif userInput == 3:

            num = 0

            print("")

            print("Goodbye!")

        else:

            print("")

            print("Sorry, that is not an option!")

menu()