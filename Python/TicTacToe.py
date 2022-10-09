
theboard = {'top-left':'','top-mid':'','top-right':'',
            'mid-left':'','mid-mid':'','mid-right':'',
            'bot-left':'','bot-mid':'','bot-right':''
            }

def createBoard(board):
    print(board['top-left'] ,'|',board['top-mid'] ,'|',board['top-right'])
    print('-+ - +-')
    print(board['mid-left'] ,'|',board['mid-mid'] ,'|',board['mid-right'])
    print('-+ - +-')
    print(board['bot-left'] ,'|',board['bot-mid'] ,'|',board['bot-right'])


turn = 'x'

for i in range(9):
    createBoard(theboard)
    print('Turn', turn,'to where?')
    move = input()

    theboard[move] =turn

    if turn =='x':
        turn = 'o'
    else:
        turn = 'x'      


createBoard(theboard)