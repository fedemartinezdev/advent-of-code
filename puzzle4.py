with open('directions.txt') as file:
    directions = file.readlines()

directions = [direction.rstrip() for direction in directions]

depth = 0
position = 0
aim = 0

for direction in directions:
    action, units = direction.split(' ')
    units = int(units)

    if action == 'forward':
        position += units
        depth += aim * units
    elif action == 'down':
        aim += units
    elif action == 'up':
        aim -= units

print(depth * position)