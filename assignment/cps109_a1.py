#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
As a student at Toronto Metropolitan University who attends almost all of her lectures, I happen to see students getting bored during a lecture. This causes them to resort to several solutions: mindlessly scrolling through social media, taking naps, or simply just leaving mid-lecture! Now all of these are harmless solutions, but often times I will witness students playing games on their laptops, and it can get extremely distracting for me. The bright colours and wanting to know whether my fellow classmate will win or beat that level keeps me checking their screen more often than the powerpoint being shared by the professor. Thus I’ve decided to program a solution. A console based game that will keep students entertained without distracting me! Being console based, it eliminates the factor of bright colours that seem to catch my eye. Furthermore, this game consists of numbers and boxes, there are no levels or lives for me to keep looking back at from the back of the room.  This game is a mathematical version of tic-tac-toe and this is how it works:

Players will take turns placing numbers 1 through 9 inclusive until a row, column or diagonal adds up to 15. The only rule being that the first move placed cannot be a 5 in the middle box. The user can play against a classmate, but to avoid distracting others during the lecture, I have implemented a game mode to play against the computer. 
@author: sadikshadahal
"""

import gameFuncs as g
import time as t


# displaying welcome message
g.printer("==============================================================================")
g.printer("Welcome to mathematical tic-tac-toe! Here are the rules and how to play: ")
g.printer("Mathematical tic-tac-toe is a two player game, it can be played against another player, or againtst the computer. \nIn this game, players take turns placing digits 1-9 on a 3x3 board. \nTo win, one of the players must place the number that forms a row, column, or diagonal who's sum adds up to 15.\nThe only rule in this game is that the first move cannot be the digit 5 placed in the middle as this is a guaranteed win.")
g.printer()
g.printer("==============================================================================")
t.sleep(0.5)
g.printer("Please select a game mode.\n")


# creating file to store game stats 
stats = open("game_stats", 'w')
stats.close()

# variables to check game state
run_game = True
run_stats = False

# variables to store game stats 
player1_moves = g.p1
player2_moves = g.p2  
comp_moves = g.cp

player1_wins = g.p1_wins
player2_wins = g.p2_wins
comp_wins = g.cp_wins
  
games_played = 0             


def main_game(running=True):
    ''' 
    function that runs the game
    '''
    while running:
        
        mode = g.get_mode()
        
        if not g.runGame(mode):
            running = False
            return running
            
def show_stats():
    '''
    reads in stats from file and displays them to player after all games done
    '''
   
    stats = open('game_stats', 'r')
    
    
    statGame = [] 
    game = 0
    
    # reading in stats from the file
    for game in range(games_played):
        game+= 1
        
        # organizing stats into variables and lists
        p1_moves = stats.readline().split('), (')
        p2_moves = stats.readline().split('), (')
        cp_moves = stats.readline().split('), (')
        win = stats.readline().split('|')
        
        winner = win[0]
        typeWin = win[1].split(':')
        method = typeWin[0]
        
        # printing game statistics 
        g.printer("\nGame %s stats: " % str(game))
        if 'No' in winner:
            g.printer("No Winner! It was a draw.")
        else:
            g.printer('The winner of this game was player %s' % winner)
  
            spot = ''
            if 'd' in method:
                spot = 'from'
            else:
                spot = 'in'
                if 'v' in method:
                    spot += ' column'
                else:
                    spot += ' row'
            
    
            if typeWin[1] != " ":
                g.printer('Player %s won%s  %s %s' % (winner, method ,spot, typeWin[1].strip()))
                
            else:
                g.printer('Player %s won%s' % (winner, method))
        
       
        g.printer('Player 1 had: ' + str(len(p1_moves)) + ' moves')
        
        if len(p2_moves) != 0:
            g.printer('Player 2 had: ' + str(len(p2_moves)) + ' moves')
        else: 
            g.printer('Computer had: ' + str(len(cp_moves)) + ' moves')   
        
    stats.close()
    
  
    
def save_stats():
    '''
    saves stats to file after end of each game  

    '''
    stats = open('game_stats', 'a')
    
    stats.write(str(player1_moves)+"\n")
    stats.write(str(player2_moves)+"\n")
    stats.write(str(comp_moves) +'\n')
    
    if 'Draw' in player1_wins:
        stats.write(" No Winner |")
        stats.write(" Match Draw :")
        stats.write("Full Board")
        stats.write("\n")
    
    else:
        if len(player1_wins) != 0:
            stats.write("1| ")
            typeWin, spot = player1_wins[0]
            stats.write(typeWin)
            stats.write(str(spot))
            stats.write("\n")
        
        if len(player2_wins) != 0: 
            stats.write('2| ' )
            typeWin, spot = player2_wins[0]
            stats.write(typeWin)
            stats.write(str(spot))
            stats.write("\n")
    
        if len(comp_wins) != 0:
            stats.write('3| ')
            typeWin, spot = comp_wins[0]
            stats.write(typeWin)
            stats.write(str(spot))
            stats.write("\n")

    stats.close()


def clearStats():
    '''
    function that clears the game statistics
    '''
    player1_moves.clear()
    player2_moves.clear()
    player1_wins.clear()
    player2_wins.clear()
    comp_moves.clear()
    comp_wins.clear()


# runs while game is occuring
while run_game:
    run_stats = False
    
    # occurs when game is ove r
    if not main_game():
        games_played += 1 
        save_stats()
        g.clearBoard()
        clearStats()

    # asking user if they want to play again
    p = input('type y to play again: ')
    g.writer('type y to play again: ')
    g.writer(p)
    
    # if user does not want to play, game state switches to showing stats
    if p != 'y':
        run_game = False
        run_stats = True

# shows stats 
while run_stats:
    show_stats()
    run_stats = False

# exit message
g.printer('thanks for playing.')
            


    

