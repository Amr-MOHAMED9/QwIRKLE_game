import random
from termcolor import colored
from copy import deepcopy

22


def bag_of_tiles():
    bag = []
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    CYAN = 'cyan'
    MAGENTA = 'magenta'
    BLUE = 'blue'
    GREY='grey'
    
    TRIANGLE = '▲'
    DIAMOND = '◆'
    SQUARE = '■'
    CIRCLE = '●'
    STAR = '★'
    SPARKLE = '❈'
    CLUBS='♣'
    SPADES='♠'
    HEART='♥'     
    
    n=int(input('\nEnter the number of colors \nMax is 7 : '))
    if n>7:
        print('\nInvalid input \nPlease enter a value less than or equal to 7 : ')
        n=int(input('\nEnter the number of colors \nMax is 7 : '))
    y=int(input('\nEnter the number of shapes \nMax is 9 : '))
    if y>9:
        print('\nInvalid input \nPlease enter a value less than or equal to 9 : ')
        y=int(input('\nEnter the number of shapes \nMax is 9 : '))
    x=int(input('\nEnter the number of identical tiles: '))

    shapes = [CIRCLE,DIAMOND,SPARKLE,SQUARE,STAR,TRIANGLE,CLUBS,HEART,SPADES]

    colors = [BLUE,CYAN,GREEN,MAGENTA,RED,YELLOW,GREY]

    for i in range(n):
        for k in range(y):
            s=[colors[i],shapes[k]]
            bag.append(s)
            s=[]
    bag=bag*x
    return bag



def pick_tiles(bag):
    tiles=[]
    while len(tiles)<6:
        a=random.choice(bag)
        tiles.append(a)
        bag.remove(a)
    return tiles



def display_tiles(s):
    r=[]
    for i in s:
        d=colored(i[1],i[0])
        r.append(d)
    f=""
    for i in range (len(r)):
        f+=r[i]+" "
        d=""
    return f



def grid():
    grid=[["3",0,0,0],["2",0,0,0],["1",0,0,0],[".","a","b","c"]]
    
    return grid


def display_board(board):
    s=deepcopy(board)
    for i in range (len(s)):
        for k in range(0,len(s)):
            if s[i][k]== 0:
                s[i][k]=" _ "
            elif len(s[i][k])==2:    
                s[i][k]=" "+colored(s[i][k][1],s[i][k][0])
            else:
                s[i][k]=" "+str(s[i][k])+" "
    """d=" "
    for i in range (len(board[-1])):
        d+=" "+board[-1][i]+" "
    s[-1]=d"""
    d=""
    for i in s:
        for k in i:
            d+=k
        print(d)
        d=""
    
    return s


def increase_board(board):#increas board after each play , we might add variable d should be == to int(board[0[0]])
    m=len(board[0])
    l=[str(m)]
    ll=[str(m+1)]
    for i in range (m-1):
        l.append(0)
        ll.append(0) 
    board.insert(0,l)
    board.insert(0,ll)
    
    for i in board:
        if i[0] != '.':
            for k in range (2):
                i.append(0)
        else:
            o=ord(i[-1])
            board[-1].append(chr(o+1))
            board[-1].append(chr(o+2))
    return board

def choose_tile(tiles):
    
#    y=display_tiles(tiles).split()
#    for i in range (1,len(y)+1):
#       tt+=str(i)+"."+y[i-1]+" "
#    print(tt)   
    e=int(input('Choose a tile\n'))  
    while e>len(tiles)or e<1:
        print("Invalid input\n")
    tile =tiles[e-1]
    tiles.pop(e-1)
    return tile

def has_no_tiles(tiles):
    return len(tiles) == 0


def co_or():
    r=input("Enter the x-axis letter followed by a space and the y-axis number\n")
    while len(r.split())<2:
        print("invalid entry\n")
        r=input("Enter the x-axis letter followed by the y-axis number\n")
    r=r.split()
    x=r[0]
    y=int(r[1])
    y=(-1*(y+1))
    x=ord(x)-96
    return x,y


def play_tile(board,tile,x,y):
    
    board[y][x] = tile
    
    return board

def valid_play(board,tile,x,y,turn):
    # Make sure the placement is not on a corner and is inside the board
    if x==0 and y==0:
        return False
    elif x==-1 and y==0:
        return False
    elif x==0 and y==-1:
        return False
    elif x==-1 and y==-1:
        return False
    elif y>len(board[0]):
        return False
    elif x>len(board[0]):
        return False
    elif x==-1 and y==-2:
        return False
    elif x==1 and y==-2:
        return False
    elif x==0:
        return False
    elif y==-1:
        return False
    elif board[y][x]!=0 and len(board[y][x])==2 :#check if spot is not empty
        return False
    elif board[y-1][x]==0 and board[y][x-1]==0 and board[y+1][x]==0 and board[y][x+1]==0 and turn!=0:
        return False
   
    #    Make sure the placement has at least one adjacent placement
    adjacent_checks = []
    if y + 1 >= 0:
        adjacent_checks.append((board[y - 1][x] ==0))
    if y - 1 < len(board):
        adjacent_checks.append((board[y + 1][x]  ==0))
    if x - 1 >= 0:
        adjacent_checks.append((board[y][x - 1]  ==0))
    if x + 1 < len(board[y]):
        adjacent_checks.append((board[y][x + 1] ==0))
    
    if all(adjacent_checks) and turn>0:
        return False
    


    return True





                        
            
def score(board,x,y):
    """Return the score for the current turn"""
    score = 0
    scored_horizontally = []
    scored_vertically = []

    min_x = x
    while min_x - 1 >= 0 and board[y][min_x - 1] != 0:
        min_x -= 1

    max_x = x
    while max_x + 1 < len(board[y]) and board[y][max_x + 1] != 0 :
        max_x += 1

    if min_x != max_x:
        qwirkle_count = 0
        for t_x in range(min_x, max_x + 1):
            if (t_x, y) not in scored_horizontally:
                score += 1
                qwirkle_count += 1
                scored_horizontally.append((t_x, y))

                if (x, y) not in scored_horizontally:
                    score += 1
                    qwirkle_count += 1
                    scored_horizontally.append((x, y))
            t_x += 1

        if qwirkle_count == 6:
            score += 6

    min_y = y
    while min_y - 1 >= 0 and board[min_y - 1][x]  !=0:
        min_y -= 1

    max_y = y
    while max_y + 1 < len(board) and board[max_y + 1][x] !=0:
        max_y += 1

    if min_y != max_y:
        qwirkle_count = 0
        for t_y in range(min_y, max_y + 1):
            if (x, t_y) not in scored_vertically:
                score += 1
                qwirkle_count += 1
                scored_vertically.append((x, t_y))

                if (x, y) not in scored_vertically:
                    score += 1
                    qwirkle_count += 1
                    scored_vertically.append((x, y))
            t_y += 1

        if qwirkle_count == 6:
            score += 6

    return score


def human():

    players = []
    bag=bag_of_tiles()
    board = grid()
    points=0
    turnn=0
    n=int(input("no. of players : "))
    players=[]
    for i in range(n):
        players.append("Player"+str(i+1))
    players_tiles=[]
    item=[]
    for i in range (n):
        item.append(players[i])
        item.append(pick_tiles(bag))
        item.append(0)
        players_tiles.append(item)
        item=[]
    turn=0
    while len(bag)>0:
        m=input("Press b to save the game and play later\nPress l to load a saved game\nOr Enter to skip to the Game\n")
        if m=="b":
            with open("qqq.txt", "w") as qqq:
                for line in board:
                    qqq.write(" ".join(str(line)) + "\n")
            break
        if m=="l":
            from ast import literal_eval
            with open('qqq.txt') as f:
                board = literal_eval(f.read())
                open('qqq.txt', 'w').close()
        
        for i in range (0,len(players_tiles)):
            print("Player "+str(i+1)+" score : "+str(players_tiles[i][2]) )
            
        for i in players_tiles:
            while len(i[1])<6:
                t=random.choice(bag)
                i[1].append(t)
                bag.remove(t)
                
        print('Player ' +str(turn+1)+' turn\n')
        points=0
        r="response"
        
        while r!= "p":
            tiles=players_tiles[turn][1]
            display_board(board)
            y=display_tiles(tiles).split()
            tt=""
            for i in range (1,len(y)+1):
               tt+=str(i)+"."+y[i-1]+" "
            print(tt)
            y=input("Press Enter to play or p to pass\n")
            if y!="p":
                
                tile=choose_tile(tiles)
                x,y=co_or()

                while  valid_play(board,tiles,x,y,turnn)==False:  
                    print('Invalid entry\n')
                    tile=choose_tile(tiles)
                    x,y=co_or()
                board=play_tile(board,tile,x,y)  
                board=increase_board(board)
                #display_board(board)
                #if board[y][x][]
                points=score(board,x,y)
                players_tiles[turn][2]+=points
                points=0
                
            else:
                
                break
            
        if turn+1<n:
            turn+=1
        else:
            
            turn=0
        turnn+=1
    
    k=0
    x=0
    
    for i in players_tiles:
        if i[2]>x:
            x=i[2]
            k=i.index()
    print("Player "+str(k+1)+" won!!!!")


def bot(board,tile,turnn):
    l=[]
    for i in range (len(board)):
        for k in range (len(board)):
            if board[i][k]==0:
                l.append((i,k))
    x,y=random.choice(l)
    if valid_play(board,tile,x,y,turnn)== False:
        board=play_tile(board,tile,x+1,y+1) 
    elif valid_play(board,tile,x,y,turnn)== True:
        board=play_tile(board,tile,x,y)
    else:
        board=play_tile(board,tile,x+2,y+2) 
    return board


def ag_bot():
    players = []
    bag=bag_of_tiles()
    board = grid()
    points=0
    turnn=0
    n=2
    players=[]
    for i in range(2):
        players.append("Player"+str(i+1))
    players_tiles=[]
    item=[]
    for i in range (n):
        item.append(players[i])
        item.append(pick_tiles(bag))
        item.append(0)
        players_tiles.append(item)
        item=[]
    turn=0
    while len(bag)>0:
        m=input("Press b to save the game and play later\nPress l to load a saved game\nOr Enter to skip to the Game\n")
        if m=="b":
            with open("qqq.txt", "w") as qqq:
                for line in board:
                    qqq.write(" ".join(str(line)) + "\n")
            break
        if m=="l":
            from ast import literal_eval
            with open('qqq.txt') as f:
                board = literal_eval(f.read())
                open('qqq.txt', 'w').close()
        for i in range (0,len(players)):
            print("Player "+str(i+1)+" score :"+str(players_tiles[i][2]) )
        print('Player ' +str((turn%2)+1)+' turn\n')
        for i in players_tiles:
            while len(i[1])<6:
                t=random.choice(bag)
                i[1].append(t)
                bag.remove(t)
        points=0
        r="response"
        if turn%2==0:
            while r!= "p":
                display_board(board
                              )
                r=input("Press Enter to play or p to pass\n")
                if r!="p":
                    tiles=players_tiles[turn%2][1]
                    display_board(board)
                    y=display_tiles(tiles).split()
                    tt=""
                    for i in range (1,len(y)+1):
                       tt+=str(i)+"."+y[i-1]+" "
                    print(tt)
                        
                    tile=choose_tile(tiles)
                    x,y=co_or()
    
                    while  valid_play(board,tiles,x,y,turnn)==False: 
                        print('Invalid entry')
                        tile=choose_tile(tiles)
                        x,y=co_or()
                    board=play_tile(board,tile,x,y)  
                    board=increase_board(board)
                    #display_board(board)
                    points=score(board,x,y)
                    players_tiles[turn][2]+=points
                    points=0
                else:
                    r="p"
                    break
        else:
            
            tiles=players_tiles[turn%2][1]
            tile=random.choice(tiles)
            tiles.remove(tile)
            board=bot(board,tile,turnn)
            board=increase_board(board)
            display_board(board)
            if turnn==0:
                turnn+=1
        turn+=1
        turnn+=1
    k=0
    x=0
    for i in players_tiles:
        if i[2]>x:
            x=i[2]
            k=i.index()
    print("Player "+str(k+1)+" won!!!!")
    
        
    
    
n=int(input('Enter 1 for Human vs Human \nPress 2 for Human vs Bot\n'))
while n!=1 and n!=2:
    print('inalid Entryn\n')
if n==1:
    human()
elif n==2:
    ag_bot()
    