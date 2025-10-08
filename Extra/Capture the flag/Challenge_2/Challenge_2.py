from random import random, randint

flipperkast = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 235, 0, 0, 0, 0],
    [0, 0, -1 , 0, 0, 0, -1, 0],
    [0, 0, 0, 0, -1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 945, 0, 237, 0, 709, 0]
]

rows = len(flipperkast)
cols = len(flipperkast[0])

def drop_ball(start_col):
    x, y = start_col, 0
    while True:
        if y >= rows:   # fell out the bottom
            return 0
        
        cell = flipperkast[y][x]

        if cell == 0:  # empty, keep falling
            y += 1

        elif cell == -1:  # obstacle
            x += (1 if random() < 0.5 else -1)
            y += 1
            if x < 0 or x >= cols:
                return 0  # out of bounds

        elif cell > 0:  # hit a goal
            return cell

def simulate(trials=100000):
    total = 0
    for _ in range(trials):
        col = randint(0, cols-1)  # avoid first/last column
        total += drop_ball(col)
    return total / trials

avg = simulate(2000000)  # bigger trials = more accurate
print(round(avg, 3))
