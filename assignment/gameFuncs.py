#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:44:43 2023

@author: sadikshadahal
"""

import random
import time as t

# creating output file 
file = 'cps109_a1_output.txt'
output = open(file, 'w')
output.close()


# declaring game variable 
board = [] 
p1 = []
p1_wins=[]
p2 = []
p2_wins= []
cp = []
cp_wins = []
size = 9
moves = [i for i in range(1,10)]

# creating list that updates as user places moves
for i in range(size):
    board.append(' ')
    

def printer(s = ""):
    '''
    
    function that takes a string s, then prints it and writes it to output file


    '''
    print(s)
    output = open(file, 'a')
    output.write(str(s) + '\n')
    output.close()


def writer(s):
    '''
    
    function that takes a string s, then writes it to output file

    '''
    
    output = open(file, 'a')
    output.write(str(s) + '\n')
    output.close()
    

def makeBoard():
    """
    
    function that creates visual gameboard 

    """
    printer("     |     |     ")
    printer("  %s  |  %s  |  %s" % (board[0], board[1], board[2]))
    printer("_____|_____|_____")
    printer("     |     |     ")
    printer("  %s  |  %s  |  %s"  %(board[3], board[4], board[5]))
    printer("_____|_____|_____")
    printer("     |     |    ")
    printer("  %s  |  %s  |  %s" % (board[6], board[7], board[8]))
    printer("     |     |     \n") 

    

def get_mode():
    '''
    
    function that gets the game mode from player and returns it 

    '''
    valid_mode = False
   
    mode = input("Mode 1: Player vs. Player\nMode 2: Player vs. Computer\nEnter '1' or '2': \n")
    writer("Mode 1: Player vs. Player\nMode 2: Player vs. Computer\nEnter '1' or '2': \n")
    writer(mode)
    
    # repeatedly asks user for input til the given input is an integer
    while not valid_mode:
        try:
                mode = int(mode)
                valid_mode = True
        except:
               mode = (input("\nInvalid input, Enter an integer: "))
               writer("\nInvalid input, Enter an integer: ")
               writer(mode)
               if type(mode) == int:
                   valid_mode = True
                   
    # repeatedly asks user for input til given input is either 1 or 2              
    else:
        if valid_mode:
            if mode == 1 or mode == 2:
                return mode
            else:
                printer("\nInvalid input.")
                return get_mode()
            
            
def playerMove():
    '''
    
    function that gets player move and places it onto gameboard
    returns tuple containing the number placed and its location on the board

    '''
    box = validBox()
    num = validNum()
    
    if box == 4 and num == 5 and board.count(' ') == 9: 
        printer("Rule: 5 cannot be placed into box 5 on first turn, try again.")
        return playerMove()
    else:
                
        board[box] = num
        makeBoard()
        
        return (box+1, num)


def compMove():
    '''
    function that gets the computers move
    '''
    
    valid_box = False
    valid_num = False
    
    printer("computer move! \n")
    t.sleep(1)
    
    # checks that the random integer spot on board is empty 
    while not valid_box:
        box = random.randint(0, 8)
        if board[box] == ' ':
            valid_box = True
        
    # checks that the random integer has not already been placed on board
    while not valid_num:
        num = random.randint(1, 9)
        if num not in board:
            valid_num = True
    
    # places number onto specified box space and displays board
    if valid_num and valid_box:
        board[box] = num
        makeBoard()
        printer("comp placed %s in box %s" % (num, box+1) + "\n")

        
    return(box+1, num)
            
        


def validBox():
    '''
    function that gets and returns the box that player wants to place number in

    '''
    valid = False
    
    while not valid:
        try:
            box = int(input("What box would you like to place in? \n"))-1
            writer("What box would you like to place in? \n")
            writer(box)
            if board[box] == ' ' :
                valid = True
                return int(box)
            else: printer("Box already used or not allowed.")
        except: printer("invalid input")
    return validBox()

    
    
    

def validNum():
    '''
    function that gets and returns the number that player wants to place
    '''
    valid = False
    
    while not valid:
        try:
            num = int(input("What number would you like to place? \n"))
            writer("What number would you like to place? \n")
            writer(num)
            if num not in board and num in moves:
                valid = True
                return num
            else: printer("Number already used or not allowed.\n")
        except: printer("invalid input")
    return validNum()   

    

def checkWin():
    '''
    function that checks whether a win has occured on the board
    returns type of win and location of win
    '''
    # checking horizontal wins 
    for i in range(0,9,3):
        if board[i] == ' ' or board[i+1] == ' ' or board[i+2] == ' ':
            continue

        else:
            sums = board[i] + board[i+1] + board[i+2]
            if sums == 15:
                return (sums == 15, "horizontally:", i+1)
        
    #checking vertical wins
    for i in range(3):
        if board[i] == ' ' or board[i+3] == ' ' or board[i+6] == ' ':
            continue
        else: 
            sums = board[i] + board[i+3] + board[i+6]
            if sums == 15:
                return (sums == 15, "vertically: ", i+1)
    
    
    #checking diagonal wins
    sums1 = 0
    for i in range(2,7,2):
        if board[i] == " ":
            check_sums1 = False
            continue
        else:
            sums1 += board[i]
            
    if board[2] != ' ' and board[4] != ' ' and board[6] != ' ':
        check_sums1 = True 

  
    sums2 = 0
    for i in range(0,9,4):
       if board[i] == " ":
           check_sums2 = False
           continue
       else:
          sums2 += board[i]
          
    if board[0] != ' ' and board[4] != ' ' and board[8] != ' ':
        check_sums2 = True
    
        
    if sums1 == 15 and check_sums1:
            return (sums1 == 15, "diagonally: left to right", " ")
    elif sums2 == 15 and check_sums2:
            return (sums2 == 15, "diagonally: right to left", ' ')
    else: return (False, " ", None)




def clearBoard():
    '''
    function that clears the board 

    '''
    board.clear()
    for i in range(size):
        board.append(' ')

    
def runGame(mode):
    ''' 
    function that runs the game
    '''
    
    # occurs if game mode is player vs. player 
    if mode == 1:
         while " " in board:
            # checks if board is full 
            if " " not in board:
                p1_wins.append('Draw')
                p2_wins.append('Draw')
                printer('\nMatch was a draw!')
                break
            
            # player 1 move and checking if game is won
            p1.append(playerMove())
            check1 = checkWin()
            if check1[0] == True:
                printer('\n Player 1 won!')
                p1_wins.append((check1[1], check1[2]))
                break
            
            # checks if board is full 
            if " " not in board:
                p1_wins.append('Draw')
                p2_wins.append('Draw')
                break
           
            # player 2 move and checking if game is won
            p2.append(playerMove())
            check2 = checkWin()
            if check2[0] == True:
                printer('\n Player 2 won!')
                p2_wins.append((check2[1], check2[2]))
                break
            
    # occurs if game mode is player vs. computer       
    if mode == 2:
        while " " in board:
            # checking if board full
            if " " not in board:
                p1_wins.append('Draw')
                p2_wins.append('Draw')
                printer('\nMatch was a draw!')
                break
            t.sleep(1)
            
            # player 1 move and checking if game is won
            p1.append(playerMove())
            check1 = checkWin()
            if check1[0] == True:
               printer('\n Player 1 won!')
               p1_wins.append((check1[1], check1[2]))
               break
           
            t.sleep(1)        
            
            # checking if board full
            if " " not in board:
                p1_wins.append('Draw')
                p2_wins.append('Draw')                
                printer('\nMatch was a draw!')
                break
            
            # compute rmove and checking if game is won
            cp.append(compMove())
            checkc = checkWin()
            if checkc[0] == True:
                printer('\nComputer won!')
                cp_wins.append((checkc[1], checkc[2]))
                break
           
            
    printer('game over')
    return False
            