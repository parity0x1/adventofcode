import requests

cookies = dict(session='xxx')

# --- Day 1: Sonar Sweep ---

url = 'https://adventofcode.com/2021/day/1/input'
r = requests.get(url, cookies=cookies)

# Count the number of times a depth measurement increases 
# from the previous measurement.

previousNumber = 9000 # set a high first number so it is ignored
depthMeasurementIncreaseCount = 0

for currentNumber in r.text.splitlines():
    if int(currentNumber) > int(previousNumber):
        depthMeasurementIncreaseCount += 1
    previousNumber = currentNumber

print("\nDepth measurement increased " + str(depthMeasurementIncreaseCount) + " times.")

# Count the number of times the sum of measurements in this 
# sliding window increases from the previous sum. So, compare A with B, 
# then compare B with C, then C with D, and so on. Stop when there 
# aren't enough measurements left to create a new three-measurement sum.

depthMeasurementArray = r.text.splitlines()
depthMeasurementArrayLength = len(depthMeasurementArray)

previousSum = 9000 # set a high first sum so it is ignored
depthMeasurementSumIncreaseCount = 0

for n in range(0, depthMeasurementArrayLength):
    currentSumArray = depthMeasurementArray[n:n+3]
    
    currentSum = 0
    for currentNumber in currentSumArray:
        currentSum += int(currentNumber)

    if int(currentSum) > int(previousSum):
        depthMeasurementSumIncreaseCount += 1
    
    previousSum = currentSum

print("Depth measurement sum increased " + str(depthMeasurementSumIncreaseCount) + " times.")
