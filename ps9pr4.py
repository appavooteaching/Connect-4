#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *
class AIPlayer(Player):
    ''' a datatype for an AI player. Inherits Player class '''
    def __init__(self, checker, tiebreak, lookahead):
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    #3
    def __repr__(self):
        ''' takes in self (AIPlayer object) and returns checker, tiebreak, and lookahead '''
        return super().__repr__() + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
    
    #4
    def max_score_column(self, scores):
        ''' takes in int scores [] and returns index of column with maximum score 
        if tied for maximum score, will use tiebreaking strategy '''
        
        maximum_score = max(scores)
        score_indexes = []
        for index in range(len(scores)):
            if(scores[index] == maximum_score):
                score_indexes += [index]
        if(self.tiebreak == "LEFT"):
            return score_indexes[0]
        elif(self.tiebreak == "RIGHT"):
            return score_indexes[-1]
        else:
            return random.choice(score_indexes)
        
    #5
    def scores_for(self, b):
        ''' takes in self (AIPlayer object) and b (Board object). returns a list of scores for the cols'''
        
        scores = ["50"]*b.width
        
        for col in range(b.width):
            if not(b.can_add_to(col)):
                scores[col] = -1
            elif(b.is_win_for(self.checker)):
                scores[col] = 100
            elif(b.is_win_for(self.opponent_checker())):
                scores[col] = 0
            elif(self.lookahead == 0):  #LA 0, must be 50 then
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                
                storage = opponent.scores_for(b)  #scores of opponent
                if(max(storage) == 0):
                    scores[col] = 100
                elif(max(storage) == 100):
                    scores[col] = 0
                else:
                    scores[col] = 50
                
                #scores[col] = 100 - storage[col] 
                
                b.remove_checker(col)
        return scores
    
    #6
    def next_move(self, b):
        ''' takes in self (AIPlayer object) and b (board object) and overrides next_move from Player.
        returns best possible move according scores_for ad max_score_column '''
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))


















