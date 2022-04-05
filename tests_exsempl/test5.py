# различия IF \ WHILE
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

if 'Max' in friends:
    print('У меня есть такой друг')

if 'M' in friend_name:
    print('Буква М есть в имени друга')

# Переберем список друзей двумя способами:
# while
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1  # надо в любом счетчике прибавлять или отнимать номер,
    # иначе будет бесконечный цикл


