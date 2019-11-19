import random as r
import Card as c
import CardSymbolEnum as cs
import matplotlib.pyplot as plt

def pickACard(deck):
    while(True):
        randomColor = r.randint(0, 3)
        randomSymbol = r.randint(0,12)
        if deck[randomColor][randomSymbol] == False:
            deck[randomColor][randomSymbol] = True
            return c.Card(randomColor, randomSymbol)

def calculateScore(cards):
    #count aces
    aces = sum(1 if card.symbol == cs.CardSymbolEnum.Ace else 0 for card in cards)
    #calculate points
    points = sum(card.getValue() for card in cards)
    #if point are more than 21 get ace as 1
    for _ in range(aces):
        if points > 21:
            points = points - 10
    
    return points


def simulateGame(playerLimit, dilerCard):
    deck = [ [ False for i in range(13) ] for j in range(4) ]

    dilerCards = []
    playerCards = []

    #draw two cards
    dilerCards.append(pickACard(deck))
    playerCards.append(pickACard(deck))
    dilerCards.append(pickACard(deck))
    playerCards.append(pickACard(deck))    
    
    playerPoints = calculateScore(playerCards)
    dilerPoints = calculateScore(dilerCards)

    if playerPoints < playerLimit and dilerCards[1].getValue() >= dilerCard:
        playerCards.append(pickACard(deck))

    if dilerPoints < 16:
        dilerCards.append(pickACard(deck))

    playerPoints = calculateScore(playerCards)
    dilerPoints = calculateScore(dilerCards)

    #draw
    if playerPoints > 21 and dilerPoints > 21:
        return 0
    if playerPoints == dilerPoints:
        return 0

    #lose
    if playerPoints > 21:
        return -1
    if playerPoints < dilerPoints and dilerPoints <= 21:
        return -1
    
    #otherwise win
    return 1
    
def runExperiment(playerLimit, dilerCards, iter = 10000):

    i = 1
    fig = plt.figure()
    fig.suptitle("Limit gracza : " + str(playerLimit))
    fig.subplots_adjust(hspace=0.6, wspace=0.6)

    for dilerCard in dilerCards:
        #draw, win, lose
        score = [0,0,0]

        for _ in range(0, iter):
            score[simulateGame(playerLimit, dilerCard)] += 1
        
        ax = fig.add_subplot(2,3,i)
        ax.set_title("Minimum u krupiera : " + str(dilerCard))
        ax.bar( range(0,3), (score[1], score[0], score[2]) )
        ax.set_xticks( range(0,3))
        ax.set_xticklabels(['WIN\n' + str(score[1]), 'DRAW\n' + str(score[0]), 'LOSE\n' + str(score[2])])
        i = i + 1

    plt.show()