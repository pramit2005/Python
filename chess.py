moves={'m-1':['Pe4','Pe5'],'m-2':['Bc4','Ph6'],'m-3':['Qh5','Pg6'],'m-4':['Qxe5+','Be7'],'m-5':['Qxh8','Kf8'],
      'm-6':['Nc3','Bf6'],'m-7':['Nf3','Bxh8'],'m-8':['Pd3','Bg7'],'m-9':['O-O','Pd6'],'m-10':['Pe5','Bxe5'],
      'm-11':['Re1','Bxc3'],'m-12':['Pxc3','Be6'],'m-13':['Bxh6+','Nxh6'],'m-14':['Ng5','Bxc4'],'m-15':['Pxc4','Qxg5'],
      'm-16':['Re3','Ne6'],'m-17':['Re1','Nf5'],'m-18':['Rg3','']}

def count_moves(list):
    Notation={
        'P': 'Pawn',
        'K': 'King',
        'Q': 'Queen',
        'R': 'Rook',
        'B': 'Bishop',
        'N': 'Knight'
    }
    white = {'Pawn': 0, 'King': 0, 'Queen': 0, 'Bishop': 0, 'Knight': 0, 'Rook': 0}
    black = {'Pawn': 0, 'King': 0, 'Queen': 0, 'Bishop': 0, 'Knight': 0, 'Rook': 0}
    for move_num,(white_move,black_move) in moves.items():
        for move,count in [(white_move,white),(black_move,black)]:
           if move in  ['O-O','O-O-O']:
            count['King']+=1
            count['Rook']+=1
            continue
        first_char=move[0]
        if first_char.isupper():
            piece=Notation.get(first_char,'Pawn')
            count[piece]+=1
    return white,black
white_result, black_result = count_moves(moves)
print("White has moved:")
for piece,count in white_result.items():
    if count>0:
        print(f'{piece}: {count}')
print("Black has moved:")
for piece,count in black_result.items():
    if count>0:
        print(f'{piece}: {count}')


