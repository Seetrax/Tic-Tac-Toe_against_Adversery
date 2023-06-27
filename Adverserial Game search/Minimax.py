def c(a,state):#To return the no of a in state
    c=0
    for i in state:
        for j in i:
            if j==a:
                c+=1
    return c
cou=0
def adj_states(state):#Gives children of given state
    s=[]
    disc=[]
    temps=state.copy()
    for i in range (3):
        for j in range(3):
            if temps[i][j]==' ':
                temp2=temps[i].copy()
                if c('O',state)>c('X',state):#No of O> No of  X implies its X turn 
                    temp2[j]='X'
                elif c('O',state)==c('X',state):#No of O== No of  X implies its O turn
                    temp2[j]='O'

                temps[i]=temp2
                if temps not in disc:

                    s.append(temps)
                    disc.append(temps)#Appends a child into disc so its never revisited and reappended

                    temps=state.copy()
                temp2=temps[i].copy()

    return s
def pr(state):#Prints state
    for i in state:
        print("+---+---+---+")
        for j in i:
            print(f"| {j} ",end='')
        print("|")
    print("+---+---+---+")
def Utility(leaf):#Gives utility value of a leaf
    for i in leaf:
        if i==['X','X','X']:#If one of rows is full of X or O
            return 1
        elif i==['O','O','O']:
            return -1
    for i in range(len(leaf)):
        if(leaf[0][i]==leaf[1][i]==leaf[2][i]=='X'):#If one of cols is full of X or O
            return 1
        elif(leaf[0][i]==leaf[1][i]==leaf[2][i]=='O'):
            return -1
    if (leaf[0][0]==leaf[1][1]==leaf[2][2]=='X') or (leaf[0][2]==leaf[1][1]==leaf[2][0]=='X'):#If one of diagnolss is full of X or O
        return 1
    if (leaf[0][0]==leaf[1][1]==leaf[2][2]=='O') or (leaf[0][2]==leaf[1][1]==leaf[2][0]=='O'):
        return -1
    for i in leaf:##if its not a leaf state
        for j in i:
            if j==' ':
                return None
    return 0
def leaf_test(state):#Checks if given node is leaf
    global cou
    cou+=1
    if Utility(state)==None:
        return 0
    else:
        return 1
def max_val(state):#Gives maximum value of all children of a gicven node
    if leaf_test(state)==1:
        return Utility(state)
    v=-10000000000 #-infinity
    adj=adj_states(state)
    for i in adj:
        v=max(v,min_val(i))
    return v
def min_val(state):#Gives minimum value of all children of a gicven node
    if leaf_test(state)==1:
        return Utility(state)
    v=1000000000000 #Infinity
    adj=adj_states(state)
    for i in adj:
        v=min(v,max_val(i))
    return v
def dec(state):#Gives the decision/state after decision with minimax algo ie  it returns a state with highest propagated utility
    ut={}
    adj=adj_states(state)
    for i in adj:
        ut[(tuple(i[0]),tuple(i[1]),tuple(i[2]))]=min_val(i)
    arr=list(ut.values())
    arr2=list(ut.keys())
    t=arr.index(max(arr))
    t2=arr2[t]
    tt=[]
    for i in t2:
        tt.append(list(i))
    return tt


def play_game():
    ini=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]##Taken initial staate to be all empty
    curr=ini
    posi=[[1,2,3],[4,5,6],[7,8,9]]
    print("The positions are as follows")
    pr(posi)
    while(leaf_test(curr)==0):##The game runs till there is a winner or draww
        n=int(input("Enter pos of O"))
        if n<=3:
            x=0##Based on n we calc x and y in state
            y=n-1
        else:
            
            if n%3!=0:
                x=n//3
                y=(n%3)-1
            else:
                x=(n//3)-1
                y=2
        if(curr[x][y]!=' '):
            print("Enter diferent position ")
            continue
        curr[x][y]='O'
        pr(curr)
        if(Utility(curr)!=None):
            break
        
        curr=dec(curr)#For each state we find minimax decision and print it
        pr(curr)
    if Utility(curr)==1:
        print("Player X won")
    elif Utility(curr)==-1 :
        print("Player O won")
    else:
        print("Draw")

