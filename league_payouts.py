
def getPayoutPercentages():
    firstPlacePercentage = int(input("Enter percent payout of funds for first: "))
    secondPlacePercentage = int(input("Enter percent payout of funds for second: "))

    while firstPlacePercentage + secondPlacePercentage != 100:
        print("Percentages do not add up to 100, try again")
        firstPlacePercentage = int(input("Enter percent payout of funds for first: "))
        secondPlacePercentage = int(input("Enter percent payout of funds for second: "))
        
    return firstPlacePercentage, secondPlacePercentage

def findPayouts():
    leagueSize = input("League size: ") 
    buyIn = input("Buy in: ")
    weeklyTopScorer = 1
    firstPlace = 1
    secondPlace = 1
    thirdPlace = buyIn 

    totalFunds = int(leagueSize) * int(buyIn)

    weeklyTopScorer = int(input("Weekly top scorer payouts: ")) * 15

    prizePool = int(totalFunds) - int(buyIn) - int(weeklyTopScorer)

    firstPlacePercentage, secondPlacePercentage = getPayoutPercentages()
    
    firstPlace = prizePool * int(firstPlacePercentage) / 100
    secondPlace = prizePool * int(secondPlacePercentage) / 100

    print("First place: " + str(firstPlace) + "\n" + "Second place: " + str(secondPlace) + "\n" + "Third place: " + str(thirdPlace) + "\n" + "Weekly top scorer: " + str(weeklyTopScorer) + "\n")

    close = input("Press ENTER button to close")    

findPayouts()