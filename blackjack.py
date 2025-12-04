#also known as 21, is a card game where players try to get as close to 21 points without going over

import random, sys

#set up the constants
HEARTS      = chr(0x2665)
DIAMONDS    = chr(0x2666)
SPADES      = chr(0x2660)
CLUBS       = chr(0x2663)
BACKSIDE    = 'backside'

def main():
    print('''Welcome to Blackjack!
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player
        The dealer stops hitting at 17.''')

    money = int(input('How much money do you have?'))
    while True:
        if money <= 0:
            print('Come back when you have money!')
            sys.exit()

        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions
        print('Bet:', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust
            if getHandValue(playerHand) > 21:
                break

            # Get the player move
            move = getMove(playerHand, money - bet)

            # Handle the player actions
            if move == 'D':
                # Player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                #Hit/Doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('New card {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue

            if move in ('S', 'D'):
                #Stand/doubling down stops the players turn
                break

        #handle the dealers actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break #the dealer has busted
                input('Press enter to continue...')
                print('\n\n')

        #Show the final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost, or tied:
        if playerValue > 21:
            print('You busted!, You lose ${}!'.format(bet))
            money -= bet
        elif dealerValue > 21:
            print('Dealer bust! You win ${}'.format(bet))
            money += bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue < dealerValue:
            print('You lose ${}!'.format(bet))
            money -= bet
        else:
            print('It\'s a tie,  the bet is returned to the player')

        input('Press enter to continue...')
        print('\n\n')

def getBet(maxBet):
    while True:
        print('How much do you bet? (1-{}, ALL-IN, or QUIT'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thank you for playing!')
            sys.exit()

        if bet in ("ALL", "ALL-IN", "A"):
            print("All-in it is! Bet: ${}".format(maxBet))
            return maxBet

        if not bet.isdecimal():
            continue #if the player didnt enter a number, ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit)) # Add the numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        #Hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])

    # SHow the players cards
    print('Player:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0] # card is a tuple
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points
            value += 10
        else:
            value += int(rank)

    # Add the value for the aces:
    value += numberOfAces # Add 1 per ace
    for i in range(numberOfAces):
        # if another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    rows = ['','','','',''] # The text to display on each row
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            # Print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the cards front
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the players move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H','S'):
            pass
            return move # Player entered a valid move
        if move == 'D':
            return move # Player entered a valid move

if __name__ == '__main__':
    main()