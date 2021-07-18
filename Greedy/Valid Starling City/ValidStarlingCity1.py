# O(n^2) time | O(1) space - where n is the number of cities
def validStartingCity(distances, fuel, mpg):

    numberOfCities = len(distances)

    for startCityIdx in range(numberOfCities):

        milesRemaining = 0

        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
            if milesRemaining < 0:
                continue

            currentCityIdx = currentCityIdx % numberOfCities

            fuelFromCurrentCity = fuel[currentCityIdx]

            distanceToNextCity = distances[currentCityIdx]

            milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity

        if milesRemaining >= 0:
            return startCityIdx
    # This line should never be reached if the inputs are correct.

    return -1