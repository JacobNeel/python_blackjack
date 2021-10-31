#4 players  a dealer blackjack with betting and ace changing
from random import randint
import os
import time
import sys;
from cards import *
import ctypes
###################IMPORTANT##############
card=51
acecount=0
ply2bust=0
ply3bust=0
dlrbust=0
pot=0
plytot=0
dlrtot=0
ply2tot=0
ply3tot=0
quest=0
drawncardval=0
chips=2000
game=1
bet=0
###################################################
title='Blackjack'
ctypes.windll.kernel32.SetConsoleTitleW(title)
os.system('Color 06')
######################################################FUNCTIONS###################################################
def gamestart():
    global chips
    global drawncardval
    global game
    global card
    global pot
    global bet
    print("              ________________________________________________")
    print("             /                                                \ ")
    print("            |    _________________________________________     |")
    print("            |   |                                         |    |")
    print("            |   |  C:\> Blackjack _                       |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |                                         |    |")
    print("            |   |_________________________________________|    |")
    print("            |                                                  |")
    print("             \_________________________________________________/")
    print("                    \___________________________________/")
    print("                 ___________________________________________")
    print("             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
    print("          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
    print("        -'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
    print("        _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
    print("  :-------------------------------------------------------------------------:")
    print("  `---._.-------------------------------------------------------------._.---'")
    game=1
    print("You have",chips,"chips")
    while True:
        try:
            bet=int(input("Your bet?:   "))
            if bet > chips:
                print("You don't have that many chips!")
            else:
                chips=chips-bet
                print(f'You now have {chips} chips')
                pot=bet*2
                print(f'The pot is {pot} chips')
                break
        except ValueError as e:
            print("enter a valid number of chips!")
    plydealcard()
    ply2dealblank()
    ply3dealblank()
    dlrdealblank()
    plydealcard()
    ply2dealcard()
    ply3dealcard()
    dlrdealcard()
def plydealcard():
    global card
    global plytot
    global drawncardval
    global quest
    global plybust
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print(f'You are dealt a {draw}')
    cardart[draw]()
    plydck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    card=card-1
    plytot=plytot+drawncardval
    time.sleep(1.5)
    if plytot>21:
            print("You have gone bust")
            time.sleep(2)
            quest="stay"
            plybust=1
def dlrdealcard():
    global card
    global dlrtot
    global drawncardval
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print(f'The dealer is dealt a {draw}')
    cardart[draw]()
    dlrdck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    if drawncardval==1:
        if dlrtot>10:
            drawncardval=1
        else:
            drawncardval=11
    card=card-1
    dlrtot=dlrtot+drawncardval
    time.sleep(1.5)
def dlrdealblank():
    global card
    global dlrtot
    global drawncardval
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print("The dealer is dealt a card")
    blankcard()
    dlrdck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    if drawncardval==1:
     if dlrtot>10:
       drawncardval=1
     else:
       drawncardval=11
    card=card-1
    dlrtot=dlrtot+drawncardval
    time.sleep(1.5)
def ply3dealcard():
    global card
    global ply3tot
    global drawncardval
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print(f'Player three is dealt a {draw}')
    cardart[draw]()
    ply3dck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    #Change to match specific scenarios
    if drawncardval==1:
        if ply3tot>10:
            drawncardval=1
        else:
            drawncardval=11
    card=card-1
    ply3tot=ply3tot+drawncardval
    time.sleep(1.5)
def ply3dealblank():
    global card
    global ply3tot
    global drawncardval
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print("Player three is dealt a card")
    blankcard()
    ply3dck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    if drawncardval==1:
      if ply3tot>10:
        drawncardval=1
      else:
        drawncardval=11
    card=card-1
    ply3tot=ply3tot+drawncardval
    time.sleep(1.5)
def ply2dealcard():
    global card
    global ply2tot
    global drawncardval
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print(f'Player two is dealt a {draw}')
    cardart[draw]()
    ply2dck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    if drawncardval==1:
        if ply2tot>10:
            drawncardval=1
        else:
            drawncardval=11
    card=card-1
    ply2tot=ply2tot+drawncardval
    time.sleep(1.5)
def ply2dealblank():
    global card
    global ply2tot
    global drawncardval
    cardnum=randint(0,card)
    draw=cards[cardnum]
    print("Player two is dealt a card")
    blankcard()
    ply2dck.append(draw)
    cards.remove(draw)
    drawncardval=cardvalues[draw]
    if drawncardval==1:
     if ply2tot>10:
       drawncardval=1
     else:
       drawncardval=11
    card=card-1
    ply2tot=ply2tot+drawncardval
    time.sleep(1.5)
def gamereset():
    global card
    global cards
    global cardvalues
    global plydck
    global ply2dck
    global ply3dck
    global dlrdck
    global plytot
    global ply2tot
    global ply3tot
    global dlrtot
    global quest
    cards=['Jack of clubs','Jack of diamonds','Jack of spades','Jack of hearts','King of clubs','King of diamonds','King of spades','King of hearts','Queen of clubs','Queen of diamonds','Queen of spades','Queen of hearts','Ace of clubs','Ace of diamonds','Ace of spades','Ace of hearts','10 of clubs','10 of diamonds','10 of spades','10 of hearts','9 of clubs','9 of diamonds','9 of spades','9 of hearts','8 of clubs','8 of diamonds','8 of spades','8 of hearts','7 of clubs','7 of diamonds','7 of spades','7 of hearts','6 of clubs','6 of diamonds','6 of spades','6 of hearts','5 of clubs','5 of diamonds','5 of spades','5 of hearts','4 of clubs','4 of diamonds','4 of spades','4 of hearts','3 of clubs','3 of diamonds','3 of spades','3 of hearts','2 of clubs','2 of diamonds','2 of spades','2 of hearts']
    cardvalues={'Jack of clubs':10,'Jack of diamonds':10,'Jack of spades':10,'Jack of hearts':10,'King of clubs':10,'King of diamonds':10,'King of spades':10,'King of hearts':10,'Queen of clubs':10,'Queen of diamonds':10,'Queen of spades':10,'Queen of hearts':10,'Ace of clubs':11,'Ace of diamonds':11,'Ace of spades':11,'Ace of hearts':11,'10 of clubs':10,'10 of diamonds':10,'10 of spades':10,'10 of hearts':10,'9 of clubs':9,'9 of diamonds':9,'9 of spades':9,'9 of hearts':9,'8 of clubs':8,'8 of diamonds':8,'8 of spades':8,'8 of hearts':8,'7 of clubs':7,'7 of diamonds':7,'7 of spades':7,'7 of hearts':7,'6 of clubs':6,'6 of diamonds':6,'6 of spades':6,'6 of hearts':6,'5 of clubs':5,'5 of diamonds':5,'5 of spades':5,'5 of hearts':5,'4 of clubs':4,'4 of diamonds':4,'4 of spades':4,'4 of hearts':4,'3 of clubs':3,'3 of diamonds':3,'3 of spades':3,'3 of hearts':3,'2 of clubs':2,'2 of diamonds':2,'2 of spades':2,'2 of hearts':2}
    plydck=[]
    ply2dck=[]
    ply3dck=[]
    dlrdck=[]
    card=51
    acecount=0
    time.sleep(2)
    plytot=0
    ply2tot=0
    ply3tot=0
    dlrtot=0
    plybust=0
    quest=0
    gamestart()
#checks if game is over and if player wants to play again
def gameend():
    global ending
    global game
    while True:
            try:
                ending=input("Play again(Y or N):   ")
                ending=ending.lower()
                if ending == 'y':
                    gamereset()
                    break
                elif ending == 'n':
                    sys.exit()
                else:
                    print('Enter "Y" or "N"')
            except Exception as e:
                print(e)
def showplycards():
    global cardart
    global q
    print("=========================YOURCARDS=========================")
    q=0
    for card in plydck:
        cardart[plydck[q]]()
        q=q+1
    time.sleep(2)
#####USE FOR THE END BECUASE OF STARTING HIDDEN CARD
def showply2endcards():
    global cardart
    global q
    print("=========================ply2CARDS=========================")
    q=0
    for card in ply2dck:
     cardart[ply2dck[q]]()
     q=q+1
    time.sleep(2)
def showply3endcards():
    global cardart
    global q
    print("=========================ply3CARDS=========================")
    q=0
    for card in ply3dck:
     cardart[ply3dck[q]]()
     q=q+1
    time.sleep(2)
def showdlrendcards(): 
    global cardart
    global q
    print("=========================dlerCARDS=========================")
    q=0
    for card in dlrdck:
     cardart[dlrdck[q]]()
     q=q+1
    time.sleep(2)
#FOR IN GAME
def showply2cards():
    global cardart
    global q
    print("=========================ply2CARDS=========================")
    q=1
    for card in ply2dck:
     cardart[ply2dck[q]]()
     q=q+1
    time.sleep(2)
def showply3cards():
    global cardart
    global q
    print("=========================ply3CARDS=========================")
    q=1
    for card in ply3dck:
     cardart[ply3dck[q]]()
     q=q+1
    time.sleep(2)
def showdlrcards():
    global cardart
    global q
    print("=========================dlerCARDS=========================")
    q=1
    for card in dlrdck:
     cardart[dlrdck[q]]()
     q=q+1
    time.sleep(2)
def playerturn():
#ACE FINALLY WORKS
    global game
    global plytot
    global acecount
    global quest
    global chips
    global bet
    global pot
    showplycards()
    quest=input("hit,stay, or double?:\t")
    if quest=="double":
        plydealcard()
        chips=chips-bet
        pot=pot*2
        print("the pot is now",pot)
        quest="stay"
    if quest=="hit":
        plydealcard()
    while quest!="stay":
        quest=input("hit or stay?:\t")
        time.sleep(1)
        if quest=="hit":
         plydealcard()
        showplycards()
    acenum=plydck.count('Ace of spades')
    acenum2=plydck.count('Ace of hearts')
    acenum3=plydck.count('Ace of diamonds')
    acenum4=plydck.count('Ace of clubs')
    acecount=(acenum+acenum2+acenum3+acenum4)
    while acecount!=0:
        plytot=plytot+10
        if plytot>21:
            plytot=plytot-10
        acecount=acecount-1
def player2turn():
    print("=========================ply2TURN=========================")
    global ply2bust
    global ply2tot
    while ply2tot<17:
        ply2dealcard()
        if ply2tot>21:
            print("Player 2 busts")
            time.sleep(2)
            ply2bust=1
        time.sleep(1.5)
def player3turn():
    global ply3bust
    global ply3tot
    print("=========================ply3TURN=========================")
    while ply3tot<17:
        ply3dealcard()
        if ply3tot>21:
            print("Player 3 busts")
            time.sleep(2)
            ply3bust=1
        time.sleep(1.5)
def dlrturn():
    global dlrbust
    global dlrtot
    print("=========================dlrTURN==========================")
    while dlrtot<17:
        dlrdealcard()
        if dlrtot>21:
            print("The Dealer busts")
            time.sleep(2)
            dlrbust=1
        time.sleep(1.5)
def windec():
    global pot
    global chips
    global plytot
    global dlrtot
    global ply2tot
    global ply3tot
    global game
    if plytot>dlrtot and plytot<=21:
        print(f'your hand total: {plytot} > the dealers hand total: {dlrtot}')
        print("You have one the hand!")
        print(f'You win the pot of {pot}')
        chips=chips+pot
    if dlrtot>plytot and dlrtot<=21:
        print(f'your hand total: {plytot} < the dealers hand total: {dlrtot}')
        print("You have lost the hand!")
        print('You have lost the pot of {pot}')
    if plytot==dlrtot and dlrtot<=21:
        print("Your hand and the Dealer's hand are equal.")
        print("Your bet is returned to you")
        chips=chips+(pot/2)
    if dlrtot>21 and plytot<=21:
        print("The dealer busted")
        print(f'You win the pot of {pot}')
        chips=chips+pot
    if plytot>21:
        print("Your hand is bust")
        print(f'plus you lost the pot of{pot}')
    time.sleep(3)
###################################################################
    if ply2tot>dlrtot and ply2tot<=21:
        print(f'player 2s hand total: {ply2tot} > the Dealers hand total: {dlrtot}')
        print("Player 2 has won their hand")
    if dlrtot>ply2tot and dlrtot<=21:
        print(f'player 2s hand total: {ply2tot} < the Dealers hand total: {dlrtot}')
        print("Player 2 has lost their hand")
    if ply2tot==dlrtot and dlrtot<=21:
        print("Player 2s hand and the Dealer's hand were equal")
    if dlrtot>21 and ply2tot<=21:
        print("The dealer busted and player 2 didn't")
    if ply2tot>21:
        print("Player 2's hand is bust")
    time.sleep(3)
###################################################################
    if ply3tot>dlrtot and ply3tot<=21:
        print(f'player 3s hand total: {ply3tot} > the Dealers hand total: {dlrtot}')
        print("Player 3 has won their hand")
    if dlrtot>ply3tot and dlrtot<=21:
        print(f'player 3s hand total: {ply3tot} < the Dealers hand total: {dlrtot}')
        print("Player 3 has lost their hand")
    if ply3tot==dlrtot and dlrtot<=21:
        print("Player 3s hand and the Dealer's hand were equal")
    if dlrtot>21 and ply3tot<=21:
        print("The dealer busted and player 3 didn't")
    if ply3tot>21:
        print("Player 3's hand is bust")
    time.sleep(3)
############################################
########################################################DECKS#####################################################
#playercards to see if there is an ace or not
plydck=[]
#dealer deck
dlrdck=[]
#player2dck
ply2dck=[]
#player3dck
ply3dck=[]
#reset deck
basic=['Jack of clubs','Jack of diamonds','Jack of spades','Jack of hearts','King of clubs','King of diamonds','King of spades','King of hearts','Queen of clubs','Queen of diamonds','Queen of spades','Queen of hearts','Ace of clubs','Ace of diamonds','Ace of spades','Ace of hearts','10 of clubs','10 of diamonds','10 of spades','10 of hearts','9 of clubs','9 of diamonds','9 of spades','9 of hearts','8 of clubs','8 of diamonds','8 of spades','8 of hearts','7 of clubs','7 of diamonds','7 of spades','7 of hearts','6 of clubs','6 of diamonds','6 of spades','6 of hearts','5 of clubs','5 of diamonds','5 of spades','5 of hearts','4 of clubs','4 of diamonds','4 of spades','4 of hearts','3 of clubs','3 of diamonds','3 of spades','3 of hearts','2 of clubs','2 of diamonds','2 of spades','2 of hearts']
#starting deck
cards=['Jack of clubs','Jack of diamonds','Jack of spades','Jack of hearts','King of clubs','King of diamonds','King of spades','King of hearts','Queen of clubs','Queen of diamonds','Queen of spades','Queen of hearts','Ace of clubs','Ace of diamonds','Ace of spades','Ace of hearts','10 of clubs','10 of diamonds','10 of spades','10 of hearts','9 of clubs','9 of diamonds','9 of spades','9 of hearts','8 of clubs','8 of diamonds','8 of spades','8 of hearts','7 of clubs','7 of diamonds','7 of spades','7 of hearts','6 of clubs','6 of diamonds','6 of spades','6 of hearts','5 of clubs','5 of diamonds','5 of spades','5 of hearts','4 of clubs','4 of diamonds','4 of spades','4 of hearts','3 of clubs','3 of diamonds','3 of spades','3 of hearts','2 of clubs','2 of diamonds','2 of spades','2 of hearts']
#a dictionary that is intended to shorten the if statment for cards like draw=dict[card](aces need to be worked on)
cardvalues={'Jack of clubs':10,'Jack of diamonds':10,'Jack of spades':10,'Jack of hearts':10,'King of clubs':10,'King of diamonds':10,'King of spades':10,'King of hearts':10,'Queen of clubs':10,'Queen of diamonds':10,'Queen of spades':10,'Queen of hearts':10,'Ace of clubs':1,'Ace of diamonds':1,'Ace of spades':1,'Ace of hearts':1,'10 of clubs':10,'10 of diamonds':10,'10 of spades':10,'10 of hearts':10,'9 of clubs':9,'9 of diamonds':9,'9 of spades':9,'9 of hearts':9,'8 of clubs':8,'8 of diamonds':8,'8 of spades':8,'8 of hearts':8,'7 of clubs':7,'7 of diamonds':7,'7 of spades':7,'7 of hearts':7,'6 of clubs':6,'6 of diamonds':6,'6 of spades':6,'6 of hearts':6,'5 of clubs':5,'5 of diamonds':5,'5 of spades':5,'5 of hearts':5,'4 of clubs':4,'4 of diamonds':4,'4 of spades':4,'4 of hearts':4,'3 of clubs':3,'3 of diamonds':3,'3 of spades':3,'3 of hearts':3,'2 of clubs':2,'2 of diamonds':2,'2 of spades':2,'2 of hearts':2}
#this is a table with all the fuctions in order to correspond with the cards
cardart={'Jack of clubs':Jackofclubs,'Jack of diamonds':Jackofdiamonds,'Jack of spades':Jackofspades,'Jack of hearts':Jackofhearts,'King of clubs':Kingofclubs,'King of diamonds':Kingofdiamonds,'King of spades':Kingofspades,'King of hearts':Kingofhearts,'Queen of clubs':Queenofclubs,'Queen of diamonds':Queenofdiamonds,'Queen of spades':Queenofspades,'Queen of hearts':Queenofhearts,'Ace of clubs':Aceofclubs,'Ace of diamonds':Aceofdiamonds,'Ace of spades':Aceofspades,'Ace of hearts':Aceofhearts,'10 of clubs':tenofclubs,'10 of diamonds':tenofdiamonds,'10 of spades':tenofspades,'10 of hearts':tenofhearts,'9 of clubs':nineofclubs,'9 of diamonds':nineofdiamonds,'9 of spades':nineofspades,'9 of hearts':nineofhearts,'8 of clubs':eightofclubs,'8 of diamonds':eightofdiamonds,'8 of spades':eightofspades,'8 of hearts':eightofhearts,'7 of clubs':sevenofclubs,'7 of diamonds':sevenofdiamonds,'7 of spades':sevenofspades,'7 of hearts':sevenofhearts,'6 of clubs':sixofclubs,'6 of diamonds':sixofdiamonds,'6 of spades':sixofspades,'6 of hearts':sixofhearts,'5 of clubs':fiveofclubs,'5 of diamonds':fiveofdiamonds,'5 of spades':fiveofspades,'5 of hearts':fiveofhearts,'4 of clubs':fourofclubs,'4 of diamonds':fourofdiamonds,'4 of spades':fourofspades,'4 of hearts':fourofhearts,'3 of clubs':threeofclubs,'3 of diamonds':threeofdiamonds,'3 of spades':threeofspades,'3 of hearts':threeofhearts,'2 of clubs':twoofclubs,'2 of diamonds':twoofdiamonds,'2 of spades':twoofspades,'2 of hearts':twoofhearts}
#################################################GAMESTART#########################################################
gamestart()
while game==1:
    playerturn()
    player2turn()
    player3turn()
    dlrturn()
    showplycards()
    showply2endcards()
    showply3endcards()
    showdlrendcards()
    windec()
    gameend()
    time.sleep(5)
 
