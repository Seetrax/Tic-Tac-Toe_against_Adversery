import Minimax as mini
import Tic
import pygame
import os
import time
import math
pygame.init()
PI=math.radians(180)

WIDTH,HEIGHT=(900,600)
screen=pygame.display.set_mode([WIDTH,HEIGHT])
WIN = pygame.Surface(screen.get_size())
pygame.display.set_caption("TIC-TAC-TOE")
RED=(255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
COL="yellow"
VEL=5
FPS=60 ##To have a definite speed for game
num1=(HEIGHT)//30
num2=(WIDTH-300)//30
pygame.font.init()

buffer_surface = pygame.Surface(WIN.get_size())
actions_allowed=[False,False,False,False] ##left,right,up,down
boards=[
    [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [1,4,2,2,2,2,3,4,2,2,2,2,3,4,2,2,2,2,3,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,5,2,2,2,2,6,5,2,2,2,2,6,5,2,2,2,2,6,1],
    [1,4,2,2,2,2,3,4,2,2,2,2,3,4,2,2,2,2,3,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,5,2,2,2,2,6,5,2,2,2,2,6,5,2,2,2,2,6,1],
    [1,4,2,2,2,2,3,4,2,2,2,2,3,4,2,2,2,2,3,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
    [1,5,2,2,2,2,6,5,2,2,2,2,6,5,2,2,2,2,6,1],
    [5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6]
    ]

textfont=pygame.font.SysFont("monospace",30)

WALLS=[]
def draw_x(pos,inte):
    global arr_x,x_turn
    x=pos[0]
    y=pos[1]
    if arr_x[inte]==1:
        pygame.draw.lines(WIN, RED, True, [(x-40,y-40),(x+40,y+40)], 5)
        pygame.draw.lines(WIN, RED, True, [(x-40,y+40),(x+40,y-40)], 5)

        pygame.display.update()
def draw_o(pos,inte):
    global arr_y,x_turn
    if arr_y[inte]==1:
        pygame.draw.circle(WIN, 'green', pos, 40 ,5)
    

        pygame.display.update()

def draw_board(lvl):
    
    for i in range (len(lvl)):
        for j in range (len(lvl[i])):
            if lvl[i][j]==1:
                pygame.draw.line(WIN,COL,(j*num2+(0.5*num2),i*num1),(j*num2+(0.5*num2),i*num1+num1),3)
                WALLS.append((j*num2+(0.5*num2),(i*num1+num1)//2))
            if lvl[i][j]==2:
                pygame.draw.line(WIN,COL,(j*num2,i*num1+(0.5*num1)),(j*num2+num2,i*num1+(0.5*num1)),3)
                WALLS.append(((j*num2+num2)//2,i*num1+(0.5*num1)))
            if lvl[i][j]==3:
                pygame.draw.arc(WIN,COL,[(j*num2-(0.5*num2)+1.5),(i*num1+(0.5*num1)),num2,num1],0,PI/2,3)
            if lvl[i][j]==4:
                pygame.draw.arc(WIN,COL,[(j*num2+(0.5*num2)),(i*num1+(0.5*num1)),num2,num1],PI/2,PI,3)
            if lvl[i][j]==5:
                pygame.draw.arc(WIN,COL,[(j*num2+(0.5*num2)),(i*num1-(0.5*num1)),num2,num1],PI,3*PI/2,3)
            if lvl[i][j]==6:
                pygame.draw.arc(WIN,COL,[(j*num2-(0.5*num2)),(i*num1-(0.5*num1)+1.5),num2,num1],3*PI/2,0,3)
   

DIRECTION=0
score=0
state=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def check_pos(centrex,centrey):
    turns=[False,False,False,False]
    ##print(centrex,centrey)
    num3=39
    if (centrex)+num3<22*num2:
        turns[1]=True
    if (centrex)-num3>0:
        turns[0]=True
    if (centrey)+num3<22*num1:
        turns[3]=True
    if (centrey)-num3>0:
        turns[2]=True
    
    return turns
TIME=0
High=-100000
x_turn=False
GameOver=False
POS_X=[]
POS_Y=[]
posi={1:(80,80),2:(200,80),3:(320,80),4:(80,200),5:(200,200),6:(320,200),7:(80,320),8:(200,320),9:(320,320),}
arr_x=[0,0,0,0,0,0,0,0,0]
arr_y=[0,0,0,0,0,0,0,0,0]
def main():
    clock=pygame.time.Clock()
  
    global DIRECTION, POS_X,POS_Y ,High, posi ,arr_x,arr_y , x_turn , score , GameOver , state , TIME
    
    Run=True
    
    while(Run):
        WIN.fill(BLACK)
        draw_board(boards)
        mouse=pygame.mouse.get_pos()
        press=pygame.mouse.get_pressed()
        if GameOver==True:
            TIME+=1/60

        for i in POS_X:
            draw_x(posi[i],i-1)
        for i in POS_Y:
            draw_o(posi[i],i-1)

        for event in  pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_q:
                Run=False
            if event.type==pygame.MOUSEBUTTONUP and ((mouse[0]<7*num1 and mouse[0]>2*num1) or (mouse[0]<13*num1 and mouse[0]>8*num1) or  (mouse[0]<19*num1 and mouse[0]>14*num1)) and ((mouse[1]<7*num2 and mouse[1]>2*num2) or (mouse[1]<13*num2 and mouse[1]>8*num2) or (mouse[1]<19*num2 and mouse[1]>14*num2)):
                
                press=(False,False,False)
                x_turn=not x_turn
            if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
                                if High<=score and score!=0:
                                    High=score
                                score=0
                                POS_X=[]
                                POS_Y=[]
                                GameOver=False
                                arr_x=[0,0,0,0,0,0,0,0,0]
                                arr_y=[0,0,0,0,0,0,0,0,0]
                                x_turn=False
                                state=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
                                mini.cou=0
                                TIME=0
        if not GameOver:
            if not x_turn:
                for i in range(9):
                    if (press[0]==1) and (mouse[0]<(7+(i%3)*6)*num1 and mouse[0]>(2+(i%3)*6)*num1) and (mouse[1]<(7+(i//3)*6)*num2 and mouse[1]>(2+(i//3)*6)*num2):
                        if arr_x[i]==0 and arr_y[i]==0:
                            
                            if x_turn:
                    
                                 POS_X.append(i+1)
                                 arr_x[i]=1
                            else:
                                 POS_Y.append(i+1)
                                 arr_y[i]=1
                for ki in range(len(arr_y)):
                    if arr_y[ki]==1:
                        state[ki//3][ki%3]='O'
            else:
                
                if mini.Utility(state)==None:
                    state=mini.dec(state)
                    for i in range(len(state)):
                        for j in range(len(state[i])):
                            if state[i][j]=='X':
                                arr_x[3*i+j]=1
                                POS_X.append(3*i+j+1)
                x_turn=not x_turn
  
        if TIME<10:
            if (arr_x[0]==1 and arr_x[1]==1 and arr_x[2]==1) or (arr_x[3]==1 and arr_x[4]==1 and arr_x[5]==1) or (arr_x[6]==1 and arr_x[7]==1 and arr_x[8]==1) or (arr_x[0]==1 and arr_x[3]==1 and arr_x[6]==1) or (arr_x[1]==1 and arr_x[4]==1 and arr_x[7]==1) or (arr_x[2]==1 and arr_x[5]==1 and arr_x[8]==1) or (arr_x[0]==1 and arr_x[4]==1 and arr_x[8]==1) or (arr_x[6]==1 and arr_x[4]==1 and arr_x[2]==1) :
                  if not GameOver:
                      score-=100
                  if TIME==0:
                      print("You Lose")
                      print("Score : " + str(score))
                      print("No. of nodes explored: "+str(mini.cou))
                  GameOver=True
                  TIME=0
                  textTBD=textfont.render("Score : " + str(score),1,WHITE)
                  WIN.blit(textTBD,(500,200))
                  textTBD=textfont.render("You Lose!!! ",1,WHITE)
                  WIN.blit(textTBD,(500,500))
                  for i in POS_X:
                    draw_x(posi[i],i-1)
                  
            elif (arr_y[0]==1 and arr_y[1]==1 and arr_y[2]==1) or (arr_y[3]==1 and arr_y[4]==1 and arr_y[5]==1) or (arr_y[6]==1 and arr_y[7]==1 and arr_y[8]==1) or (arr_y[0]==1 and arr_y[3]==1 and arr_y[6]==1) or (arr_y[1]==1 and arr_y[4]==1 and arr_y[7]==1) or (arr_y[2]==1 and arr_y[5]==1 and arr_y[8]==1) or (arr_y[0]==1 and arr_y[4]==1 and arr_y[8]==1) or (arr_y[6]==1 and arr_y[4]==1 and arr_y[2]==1) :
                  
                  if not GameOver:
                      score+=100
                  if TIME==0:
                      print("You Win")
                      print("Score : " + str(score))
                      print("No. of nodes explored: "+str(mini.cou))
                  GameOver=True
                  TIME=0
                  textTBD=textfont.render("Score : " + str(score),1,WHITE)
                  WIN.blit(textTBD,(500,200))
                  textTBD=textfont.render("You Win!!! ",1,WHITE)
                  WIN.blit(textTBD,(500,500))
                  for i in POS_Y:
                    draw_o(posi[i],i-1)
            elif sum(arr_x)+sum(arr_y)==9:
                  if not GameOver:
                      score+=50
                  if TIME==0:
                      print("Draw")
                      print("Score : " + str(score))
                      print("No. of nodes explored: "+str(mini.cou))
                  GameOver=True
                  TIME=0
                  textTBD=textfont.render("Score : " + str(score),1,WHITE)
                  WIN.blit(textTBD,(500,200))
                  textTBD=textfont.render("Draw!!!! ",1,WHITE)
                  WIN.blit(textTBD,(500,500))
                  for i in POS_Y:
                    draw_o(posi[i],i-1)
              

        ##wumpus_movement(keys_pressed,wumpus)
        if High==-100000:
            textTBD=textfont.render("High Score : " + str("None"),1,WHITE)
            WIN.blit(textTBD,(500,100))
        else:
            textTBD=textfont.render("High Score : " + str(High),1,WHITE)
            WIN.blit(textTBD,(500,100))
        textTBD=textfont.render("Score : " + str(score),1,WHITE)
        WIN.blit(textTBD,(500,200))
        textTBD=textfont.render("Press P to play again",0.3,WHITE)
        WIN.blit(textTBD,(100,450))
        textTBD=textfont.render(''' Press Q to quit''',0.3,WHITE)
        WIN.blit(textTBD,(80,500))
        screen.blit(WIN, (0, 0))
        pygame.display.flip()
        if GameOver==True and TIME >10:
            
            break
        ##clock.tick(FPS)
       
    pygame.quit()
if __name__=="__main__":
    main()

