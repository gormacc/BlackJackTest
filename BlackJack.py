import random as r
import Card as c
import CardSymbolEnum as cs
import matplotlib.pyplot as plt

def pickACard():
    return  c.Card(r.randint(0,12))

def calculateScore(points, card):
    newPoints = points + card.getValue()
    if(card.symbol == cs.CardSymbolEnum.Ace and newPoints > 21):
        newPoints = newPoints - 10
    return newPoints

def simulateGame(playerLimit):
    playerPoints = 0
    dealerPoints = 0

    #draw two cards
    playerPoints = calculateScore(playerPoints, pickACard())
    dealerCard = pickACard()
    dealerPoints = calculateScore(dealerPoints, dealerCard)
    playerPoints = calculateScore(playerPoints, pickACard())
    dealerPoints = calculateScore(dealerPoints, pickACard())

    stopGame = False
    while stopGame == False:
        
        if playerPoints < playerLimit:
            playerPoints = calculateScore(playerPoints, pickACard())    
        else:
            stopGame = True

        if dealerPoints < 17:
            dealerPoints = calculateScore(dealerPoints, pickACard())
        else:
            stopGame = True

    #lose
    if(playerPoints > 21):
        return (dealerCard.getValue(), -1)
    if playerPoints < dealerPoints and dealerPoints <= 21:
        return (dealerCard.getValue(), -1)
    #draw
    if(playerPoints == dealerPoints):
        return (dealerCard.getValue(), 0)
    #win
    return (dealerCard.getValue(), 1)


def runExperiment(playerLimit, iter = 100000):
    score = [0,0,0]
    scoreCardsWins = [ 0 for j in range(13) ]
    scoreCardsGames = [ 0 for j in range(13) ]


    for _ in range(0, iter):
        result = simulateGame(playerLimit)
        score[result[1]] += 1
        scoreCardsGames[result[0]] += 1
        if result[1] == 1:
            scoreCardsWins[result[0]] += 1

    #liczba wygranych , remisów i przegranych
    plt.title("Limit gracza : " + str(playerLimit))
    plt.bar(range(0,3), (score[1], score[0], score[2]))
    plt.xticks(range(0,3), ['WIN\n' + str(score[1]), 'DRAW\n' + str(score[0]), 'LOSE\n' + str(score[2])])
    plt.show()

    #procent zwycięstw w zależności od widocznej karty krupiera
    plt.title("Limit gracza : " + str(playerLimit))
    x = range(2,12)
    y = []
    for i in x:
        y.append(scoreCardsWins[i]/scoreCardsGames[i])
    plt.plot(x, y)
    plt.show()