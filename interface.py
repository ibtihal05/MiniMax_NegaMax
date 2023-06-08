import pygame
from time import sleep
import sys
from button import Button

nodes_positions=[(650,100), (350,200),(940,200),(195.5,300), (490,300),(115,400),(260.5,400), (75,500), (150,500),(225,500),(300,500), (410.5,400), (562.5,400),(375,500),(450,500),(525,500),(600,500), (794.5,300), (1087.5,300), (712.5,400), (862.5,400),(675,500),(750,500),(825,500),(900,500), (1021.5,400), (1162.5,400),(975,500),(1050,500),(1125,500),(1200,500)]
rec_positions=[(1180,560,40,40),(1105,560,40,40),(1030,560,40,40),(955,560,40,40),(880,560,40,40),(805,560,40,40),(730,560,40,40),(655,560,40,40),(580,560,40,40),(505,560,40,40),(430,560,40,40),(355,560,40,40),(280,560,40,40),(205,560,40,40),(130,560,40,40),(55,560,40,40)]

vals=["10","5","7","11","12","8","9","8","5","12","11","12","9","8","7","10"]
valpos=[(1200,580),(1125,580),(1050,580),(975,580),(900,580),(825,580),(750,580),(675,580),(600,580),(525,580),(450,580),(375,580),(300,580),(225,580),(150,580),(75,580)]

grey = (150, 150, 150)  
white = (255, 255, 255) 
yellow = (200, 200, 0)  
red = (200,0,0) 
black = (0, 0, 0) 
blue = (50,50,160)

display_width = 1300
display_height = 650
radius = 20 # node size

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white) 
def updatenode(node,color):
    pygame.draw.circle(screen, color, node.position, radius) 

def updatearc(node,color):
    if(node.parent != None) :
        pygame.draw.line(screen, color, node.position, node.parent.position,2)

def printdatas(data,positions) :
    i=len(data)-1
    for pos in positions :
            printdata(data[i],(pos[0], pos[1]))
            i=i-1

def printdata(data,position,size=20,color=black) :
    font = get_font(size)
    text= font.render(data,True, (color))
    textrect = text.get_rect(center=position)
    screen.blit(text, textrect)

def get_font(size): 
    return pygame.font.SysFont('segoeuisymbol',size,italic=False,bold=True)

def MinMax(node,player,depth,bestvalue=-99999,bestPath=None):
    if player == 1 :
        printdata("max",(30,depth*100))
    else :
        printdata("min",(30,depth*100))
    #Initially depth == 1
    if depth==5:
        # Display the current node’s value and mark it as explored
        updatenode(node,yellow)
        printdata(str(node.val),node.position)
        pygame.display.update() 
        sleep(1)
        return
    else:
        #Mark the current node as explored
        updatenode(node,yellow)
        pygame.display.update() 
        sleep(1)
        listChildren=[]
        if(node.leftChild != None) :
            listChildren.append(node.leftChild)
        if(node.rightChild != None) :
            listChildren.append(node.rightChild)
 
        if player==1:
            bestvalue=-99999
            bestPath=None
            for child in listChildren :
                # Mark the link between the current node and the child node as explored
                updatearc(child,yellow)
                updatenode(child,grey)
                pygame.display.update() 
                sleep(1)
                # Apply the MiniMax function on each child
                MinMax(child,-player,depth+1,bestvalue,bestPath)
                if child.val >bestvalue:
                    bestvalue=child.val
                    bestPath=child
        else:
            bestvalue=99999
            bestPath=None
            for child in listChildren :
                # Mark the link between the current node and the child node as explored
                updatearc(child,yellow)
                updatenode(child,grey)
                pygame.display.update() 
                sleep(1)
                # Apply the MiniMax function on each child
                MinMax(child,-player,depth+1,bestvalue,bestPath)
                if child.val <bestvalue:
                    bestvalue=child.val
                    bestPath=child
    node.val=bestvalue
    node.path=bestPath
    # Display the best path and the current node’s value
    updatearc(node.path,red)
    updatenode(node.path,red)

    updatenode(node,yellow)
    printdata(str(node.val),node.position)
    printdata(str(node.path.val),node.path.position)
    pygame.display.update() 
    sleep(1)

def NegaMax(node,player,depth,bestvalue=99999,bestPath=None):
    if player == 1 :
        printdata("max",(30,depth*100))
    else :
        printdata("min",(30,depth*100))
    #Initially depth == 1
    if depth==5:
        if player==-1:
            node.val=-node.val
        # Display the current node’s value and m ark it as explored
        updatenode(node,yellow)
        printdata(str(node.val),node.position)
        pygame.display.update() 
        sleep(1)
        return
    else:
        # Mark the current node as explored
        updatenode(node,yellow)
        pygame.display.update() 
        sleep(1)
        listChildren=[]
        if(node.leftChild != None) :
            listChildren.append(node.leftChild)
        if(node.rightChild != None) :
            listChildren.append(node.rightChild)
        bestvalue=-99999
        bestPath=None
        for child in listChildren :
            # Mark the link between the current node and the child node as explored
            updatearc(child,yellow)
            updatenode(child,grey)
            pygame.display.update() 
            sleep(1)
            # Apply the NegaMax function on each child
            NegaMax(child,-player,depth+1,bestvalue,bestPath)
            child.val=-child.val
            if child.val >bestvalue:
                    bestvalue=child.val
                    bestPath=child
    node.val=bestvalue
    node.path=bestPath
    # Display the best path and the current node’s value
    updatearc(node.path,red)
    updatenode(node.path,red)

    updatenode(node,yellow)
    printdata(str(node.val),node.position)
    printdata(str(-node.path.val),node.path.position)
    pygame.display.update() 
    sleep(1)


def NegaMaxAlphaBetaPruning (node, player, depth, alpha, beta) :
    #Initially, depth 1, alpha= -inf and beta=+inf
    if player == 1 :
        printdata("max",(30,depth*100))
    else :
        printdata("min",(30,depth*100))
    if (depth == 5) :
        if (player == -1): 
            node.val =-node.val
        # Display the current node’s value and mark it as explored
        updatenode(node,yellow)
        printdata(str(node.val),node.position)
        pygame.display.update() 
        sleep(1)
        # Display the values of alpha and beta
        if(alpha==-99999):
            printdata("\u03B1=-inf",(node.position[0],node.position[1]+50),15)
        else :
            printdata("\u03B1="+str(alpha),(node.position[0],node.position[1]+50),15)
        if(beta==99999):
            printdata("\u03B2=inf",(node.position[0],node.position[1]+30),15)
        else :
            printdata("\u03B2="+str(beta),(node.position[0],node.position[1]+30),15)
        return
    else :
        # Mark the current node as explored
        updatenode(node,yellow)
        pygame.display.update() 
        sleep(1)
        # Display the values of alpha and beta
        if(alpha==-99999):
            printdata("\u03B1=-inf",(node.position[0],node.position[1]-50),15)
        else :
            printdata("\u03B1="+str(alpha),(node.position[0],node.position[1]-50),15)
        if(beta==99999):
            printdata("\u03B2=inf",(node.position[0],node.position[1]-30),15)
        else :
            printdata("\u03B2="+str(beta),(node.position[0],node.position[1]-30),15)
        listChildren=[]
        if(node.leftChild != None) :
            listChildren.append(node.leftChild)
        if(node.rightChild != None) :
            listChildren.append(node.rightChild)
        bestValue = -99999
        bestPath = None
        for child in listChildren :
            # Mark the link between the current node and the child node as explored
            updatearc(child,yellow)
            updatenode(child,grey)
            pygame.display.update() 
            sleep(1)

            NegaMaxAlphaBetaPruning (child, -player, depth+1, -beta, -alpha) 
            child.val=-child.val
            if (child.val > bestValue) :
                    bestValue = child.val
                    bestPath = child
            if (bestValue > alpha) :
                alpha = bestValue
                # Display the new value of alpha
                screen.fill(white,(node.position[0]-24,node.position[1]-58,50,20))
                if(alpha==-99999):
                    printdata("\u03B1=-inf",(node.position[0],node.position[1]-50),15)
                else :
                    printdata("\u03B1="+str(alpha),(node.position[0],node.position[1]-50),15)
            if (beta <= alpha) :
                 break
    node.val = bestValue
    node.path = bestPath
    #Display the best path and the current node’s va lue
    updatearc(node.path,red)
    updatenode(node.path,red)

    updatenode(node,yellow)
    printdata(str(node.val),node.position)
    printdata(str(-node.path.val),node.path.position)
    pygame.display.update() 
    sleep(1)

def run():
        #boucle du jeu
        running = True
        while running :
            for event in pygame.event.get():
             if event.type == pygame.QUIT :
                    running=False

        pygame.quit()   
        sys.exit()      

def menu():
    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        printdata("MENU",(640, 100),100,yellow)
        

        MINMAX_BUTTON = Button(image=pygame.image.load("Method Rect.png"), pos=(640, 250), 
                            text_input="MINMAX", font=get_font(50), base_color="White", hovering_color="Red")
        NEGAMAX_BUTTON = Button(image=pygame.image.load("Method Rect.png"), pos=(640, 400), 
                            text_input="NEGAMAX", font=get_font(50), base_color="White", hovering_color="Red")
        ALPHABETA_BUTTON = Button(image=pygame.image.load("Method Rect.png"), pos=(640, 550), 
                            text_input="ALPHABETAPRUNING", font=get_font(50), base_color="White", hovering_color="Red")
        


        for button in [MINMAX_BUTTON, ALPHABETA_BUTTON, NEGAMAX_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MINMAX_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return("MinMax")
                if NEGAMAX_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return("NegaMax")
                if ALPHABETA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return("NegaMaxAlphaBetaPruning")

        pygame.display.update()
        
def play(nodes):
        method=menu()
        screen.fill(white)
        for node in nodes:
            pygame.draw.circle(screen, grey, node.position, radius) 
            if(node.parent != None) :
                pygame.draw.line(screen, grey, node.position, node.parent.position,2)
        
        for pos in rec_positions :

            pygame.draw.rect(screen, grey ,pos )
        
        printdatas(vals,valpos)
        pygame.display.update() 
        sleep(1)
        
        if(method=="MinMax"):
            printdata("MinMax",(650,30))
            pygame.display.update() 
            sleep(1)
            MinMax(nodes.pop(0), 1, 1)
        elif(method=="NegaMax") :
            printdata("NegaMax",(650,30))
            pygame.display.update() 
            sleep(1)
            NegaMax(nodes.pop(0), -1, 1)

        else :
            printdata("AlphaBetaPruning",(650,15))
            pygame.display.update() 
            sleep(1)
            NegaMaxAlphaBetaPruning (nodes.pop(0), 1, 1, -99999, 99999)

        run()

