#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[" "]*self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        
        s += ("-"*2*self.width) + "-\n"
        
        s += " "
        for col in range(self.width):
            if col <= 9:
                s += str(col) + " "
            else:
                s += str(col % 10) + " "
        
        
        return s

    #3
    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        
        index = 0
        while(self.slots[index][col] == " "):
            index += 1
            if (index > (self.height-1)):
                break
        self.slots[index-1][col] = checker

    
    ### add your reset method here ###
    
    #4
    def reset(self):
        ''' takes in self and resets the board '''
        self.slots = [[" "]*self.width for row in range(self.height)]
    
    #5
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    
    ### add your remaining methods here
    
    #6
    def can_add_to(self, col):
        ''' takes in self and int col and returns True if a checker can be added there
        and False otherwise '''
        return (col <= (self.width-1) and col >= 0 and self.slots[0][col] == " ")
    
    #7
    def is_full(self):
        ''' takes in self (board) and returns True if board is full of checkers, False otherwise '''
        for col in range(self.width):
            if(self.can_add_to(col)):
                return False
        return True

    #8
    def remove_checker(self, col):
        ''' takes in self (board object) and int col, removes the top most
        checker if there is any in the column '''
        index = 0
        while(self.slots[index][col] == " "):
            index += 1
            if(index > (self.height-1)):
                break

        self.slots[index][col] = " " #if there is nothing to remove, it replaces nothing with nothing

    
    def is_horizontal_win(self, checker):
        ''' takes in self (board object) and str checker and
        checks for horizontal win for given checker '''
        for row in range(self.height):
            for col in range(self.width - 3):
                if(self.slots[row][col] == checker and self.slots[row][col + 1] == checker \
                and self.slots[row][col + 2] == checker and self.slots[row][col + 3] == checker):
                    return True
        return False
    
    def is_vertical_win(self, checker):
        ''' takes in self (board object) and str checker and
        checks for horizontal win for given checker '''
        for col in range(self.width):
            for row in range(self.height - 3):
                if(self.slots[row][col] == checker and self.slots[row + 1][col] == checker \
                and self.slots[row + 2][col] == checker and self.slots[row + 3][col] == checker):
                    return True
        return False
    
    def is_down_diagonal_win(self, checker):
        ''' takes in self (board object) and str checker and
        checks for down diagonal win given a checker '''
        for row in range(self.height - 3): 
            for col in range(self.width - 3): 
                if(self.slots[row][col] == checker and self.slots[row + 1][col + 1] == checker \
                and self.slots[row + 2][col + 2] == checker and self.slots[row + 3][col + 3] == checker):
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        ''' takes in self (board object) and str checker and
        checks for up diagonal win given a checker '''
        for row in range(self.height - 3): 
            for col in range(self.width - 3): 
                if(self.slots[row][col + 3] == checker and self.slots[row + 1][col + 2] == checker \
                and self.slots[row + 2][col + 1] == checker and self.slots[row + 3][col] == checker):
                    return True
        return False
    
    #9
    def is_win_for(self, checker):
        ''' takes in self (board object) and str checker and
        checks for all diagonals for a win '''
        assert(checker == "O" or checker == "X")
        return (self.is_horizontal_win(checker) or self.is_vertical_win(checker) or self.is_down_diagonal_win(checker) \
        or self.is_up_diagonal_win(checker))

        

            
        



















