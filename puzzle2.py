with open('data.txt') as f:
    measurements = f.readlines()

measurements = [int(measure.rstrip()) for measure in measurements]

num_increments = 0

# pick an initial value
prev_measure = measurements[0] + measurements[1] + measurements[2]
for i in range(len(measurements) - 2):
    measure = measurements[i] + measurements[i+1] + measurements[i+2]
    if measure > prev_measure:
        num_increments += 1
    prev_measure = measure

print(num_increments)