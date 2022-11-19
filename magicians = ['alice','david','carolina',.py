magicians = ['alice','david','carolina','alice']
for magician in magicians:
    print(magician)
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print('Thank you, everyone. That was a great magic show!\n')

for value in range(1,5):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)
    #better is squares.append(value**2)

print(squares)

digits = list(range(10))
print(max(digits))
print(min(digits))
print(sum(digits))
print(digits)

players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print('Here are the first three players of my team:')
for player in players[:3]:
    print(player.title())



