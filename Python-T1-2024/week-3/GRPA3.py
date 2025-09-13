# moves = input()

# x = 0
# y = 0

# for move in moves:
    
#     if move == 'LEFT' or move == 'RIGHT':
#         x += 1
#         y = y
#         print(f'{x}, {y}')
        
#     elif move == 'UP' or move == 'DOWN':
#         x == x
#         y += 1
#         print(f'{x}, {y}')

#     elif move == 'START':
#         x = 0
#         y = 0
#         print(f'{x}, {y}')

# print(abs(x) +abs(y))


move = input()

x, y = 0, 0

while move != 'STOP':
    if move == 'UP':
        y += 1

    if move == 'DOWN':
        y -= 1

    if move == 'LEFT':
        x -= 1

    if move == 'RIGHT':
        x += 1

    move = input()

dist = abs(x) + abs(y)
print(dist) 