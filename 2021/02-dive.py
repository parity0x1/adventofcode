import requests

cookies = dict(session='xxx')

# --- Day 2: Dive ---

url = 'https://adventofcode.com/2021/day/2/input'
r = requests.get(url, cookies=cookies)

# The submarine seems to already have a planned course (your puzzle input). 
# You should probably figure out where it's going. Calculate the horizontal 
# position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your 
# final depth?

submarinePosition = [0,0]

for movement in r.text.splitlines():
    direction = movement.split()

    if direction[0] == "up" and submarinePosition[1] < 0:
        submarinePosition[1] = submarinePosition[1] + int(direction[1])
    elif direction[0] == "down":
        submarinePosition[1] = submarinePosition[1] - int(direction[1])
    elif direction[0] == "forward":
        submarinePosition[0] = submarinePosition[0] + int(direction[1])
      
print("\nSubmarine final coordinates: " + str(submarinePosition))
print("Submarine final coordinates: " + str(submarinePosition[0] * (submarinePosition[1] * -1))) # make final depth a positive number

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
  # It increases your horizontal position by X units.
  # It increases your depth by your aim multiplied by X.

# forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
# down 5 adds 5 to your aim, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
# up 3 decreases your aim by 3, resulting in a value of 2.
# down 8 adds 8 to your aim, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.

submarinePosition = [0,0,0] # [x,y,aim]

for movement in r.text.splitlines():
    direction = movement.split()

    if direction[0] == "up" and submarinePosition[1] < 0:
        submarinePosition[2] = submarinePosition[2] - int(direction[1]) # aim decreases
    elif direction[0] == "down":
        submarinePosition[2] = submarinePosition[2] + int(direction[1]) # aim increases
    elif direction[0] == "forward":
        submarinePosition[1] -= int(direction[1]) * submarinePosition[2] # x * aim
        submarinePosition[0] = submarinePosition[0] + int(direction[1]) # x + forward

print("\nSubmarine final coordinates: " + str(submarinePosition))
print("Submarine final coordinates (with aim): " + str(submarinePosition[0] * (submarinePosition[1] * -1))) # make final depth a positive number
