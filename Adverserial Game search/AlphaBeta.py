def c(a,state):#To return the no of a in state
    c=0
    for i in state:
        for j in i:
            if j==a:
                c+=1
    return c
cou2=0
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
def leaf_test(state):
    c=0
    global cou2
    cou2+=1
    if Utility(state)== 1 or Utility(state)== -1 or Utility(state)==0:
                return 1
    
    return 0
def max_val_ab(state,alph,beta):##Fuction that returns maximum utility among the children of children states taking into consideration the present alpha and beta values
    
    if(leaf_test(state)):
        
        return Utility(state)
    v=-1000000 #V is set to be - infinity
    for i in adj_states(state):
        v=max(v,min_val_ab(i,alph,beta))
        if v>=beta:
            return v
        alph=max(alph,v)
    return v
def min_val_ab(state,alph,beta):##Fuction that returns minimum utility among the children of children states taking into consideration the present alpha and beta values

    
    if(leaf_test(state)):
        
        return Utility(state)
    v=1000000## v is set to be infinty
    for i in adj_states(state):
        v=min(v,max_val_ab(i,alph,beta))
        if v<=alph:
            return v
        beta=min(beta,v)
    return v
def dec_ab(state):##Inititally alpha was set to be -infinity and beta was infintiy. this fn finds the max val of the children of state with these alpha and beta and returns the state with this max val as utility
    ut={}
    v=max_val_ab(state,-10000000,10000000000)
    adj=adj_states(state)
    for i in adj:
        ut[(tuple(i[0]),tuple(i[1]),tuple(i[2]))]=min_val_ab(i,-1000000,1000000)
    arr=list(ut.values())
    arr2=list(ut.keys())
    t=arr.index(v)
    t2=arr2[t]
    tt=[]
    for i in t2:
        tt.append(list(i))
    return tt
