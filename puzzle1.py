with open('data.txt') as f:
    measurements = f.readlines()

measurements = [int(measure.rstrip()) for measure in measurements]

num_increments = 0

# pick an initial value
prev_measure = measurements[0]
for measure in measurements[1:]:
    if measure > prev_measure:
        num_increments += 1
    prev_measure = measure

print(num_increments)