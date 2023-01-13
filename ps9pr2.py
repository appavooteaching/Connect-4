#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    ''' a datatype for a person playing with the connect 4 board '''
    #1
    def __init__(self, checker):
        assert(checker == "X" or checker == "O")
        self.checker = checker
        self.num_moves = 0
    
    #2
    def __repr__(self):
        ''' takes in self (Player object) and returns the player's checker' '''
        return "Player " + self.checker
    
    #3
    def opponent_checker(self):
        ''' takes in self (Player object) and returns opponent's checker' '''
        if(self.checker == "X"):
            return "O"
        return "X"
        
    #4
    def next_move(self, b):
        ''' takes in self (Player object) and b (Board object) and asks the user
        which column to put a checker in, and then returns that column if valid '''
        
        userCol = int(input("Enter a column: "))
        while not (b.can_add_to(userCol)):
            print("Try again!")
            userCol = int(input("Enter a column: "))
        self.num_moves += 1
        return userCol