import numpy as np
import random
O = []
X = []
win = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]]

def checkWin(P):
    for w in win:
        if all(x-1 in P for x in w):
            return True
    return False
def dispOX():
    OX = np.array([' ']*9)
    OX[O] = ['O']
    OX[X] = ['X']
    print(OX.reshape([3,3]))

def AI():
    winmove = list(set(range(9)) - set(O+X))
    W = [-100] * 9
    for m in winmove:
        tempO = O+[m]
        W[m], criticalmoveX = evalXX(X,tempO)
        if len(criticalmoveX) > 0:
            move = [i-1 for i in criticalmoveX if i-1 in winmove]
            return random.choice(move)
    validmove = list(set(range(9)) - set(O+X))
    V = [-100] * 9
    for m in validmove:
        tempX = X+[m]
        V[m], criticalmove = evalOX(O,tempX)
        if len(criticalmove) > 0:
            move = [i-1 for i in criticalmove if i-1 in validmove]
            return random.choice(move)
    maxV = max(V)
    imaxV = [i for i,j in enumerate(V) if j == maxV]
    return random.choice(imaxV)
    
def evalXX(X,O):
    SO, SX, criticalmoveX = calSXX(X,O)
    return SO - SX - 1, criticalmoveX
def calSXX(X,O):
    SO = SX = 0
    criticalmoveX = []
    for w in win:
        o = [i-1 in O for i in w]
        x = [i-1 in X for i in w]
        if not any(o):
            nX = x.count(True)
            SX += nX
            if nX == 2:
                print ('criX', w)
                criticalmoveX = w
        if not any(x):
            SO += o.count(True)
    return SO, SX, criticalmoveX
def evalOX(O,X):
    SO, SX, criticalmove = calSOX(O,X)
    return 1 + SX - SO, criticalmove
def calSOX(O,X):
    SO = SX = 0
    criticalmove = []
    for w in win:
        o = [i-1 in O for i in w]
        x = [i-1 in X for i in w]
        if not any(x):
            nO = o.count(True)
            SO += nO
            if nO == 2:
                print ('critical', w)
                criticalmove = w
        if not any(o):
            SX += x.count(True)
    return SO, SX, criticalmove
while True:
    move = int(input('Choose [1-9]'))-1
    while move in O+X or move > 8 or move < 0:
        move = int(input('Bad move: Choose[1-9]'))-1
    O.append(move)
    #dispOX()
    if checkWin(O):
        print('O win')
        break
    if len(O) + len(X) == 9:
        print('Draw')
        break
    X.append(AI())
    dispOX()
    if checkWin(X):
        print('X win')
        break
    if len(O) + len(X) == 9:
        print('Draw')
        break
    