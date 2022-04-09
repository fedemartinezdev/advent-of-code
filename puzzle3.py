with open('directions.txt') as file:
    directions = file.readlines()

directions = [direction.rstrip() for direction in directions]

depth = 0
position = 0

for direction in directions:
    action, units = direction.split(' ')
    
    if action == 'forward':
        position += int(units)
    elif action == 'down':
        depth += int(units)
    elif action == 'up':
        depth -= int(units)

print(depth * position)