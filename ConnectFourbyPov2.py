## Game of ConnectFour
## 2 human players take turns
## Objective is to make 4 in a row
## Pieces drop to lowest available spot in column selected


class Board(object):
    def __init__(self):
        self.num_row = 6
        self.num_col = 7
        self.matrix = [[0 for i in range(self.num_col)] for j in range(self.num_row)]

    def __str__(self):
    ## iterate through gameboard and print current positions
        output  = "-----------------------------\n"
        output += "| 0 | 1 | 2 | 3 | 4 | 5 | 6 |\n"
        output += "-----------------------------\n"

        #for x in self.matrix:
        for x in range(self.num_row-1, -1, -1):
            print_row = "|"
            for y in range(self.num_col):
                player = self.matrix[x][y]

                if player == 0:
                    print_row += "   |"
                elif player == 1:
                    print_row += " X |"
                elif player == 2:
                    print_row += " O |"
            output += print_row + "\n"
        output += "-----------------------------\n"
        output += "Turn: " + str(turn) + "\n"
        return output

    def win_condition(self):
    ## return which player wins (1 or 2) or 0 if nobody wins
        win_player = 0

        ## check VERTICAL
        for y in range(self.num_col):
            for x in range(self.num_row-3):
                if self.matrix[x][y] != 0 and \
                    self.matrix[x][y] == self.matrix[x+1][y] and \
                    self.matrix[x+1][y] == self.matrix[x+2][y] and \
                    self.matrix[x+2][y] == self.matrix[x+3][y]:
                    win_player = self.matrix[x][y]
                    print "\nVERTICAL WINNER! Column", y
                    return win_player

        ## check HORIZONTAL
        ## (should update to use splat and vertical check)
        for x in range(self.num_row):
            for y in range(self.num_col-3):
                if self.matrix[x][y] != 0 and \
                    self.matrix[x][y] == self.matrix[x][y+1] and \
                    self.matrix[x][y+1] == self.matrix[x][y+2] and \
                    self.matrix[x][y+2] == self.matrix[x][y+3]:
                    win_player = self.matrix[x][y]
                    print "\nHORIZONTAL WINNER! Row", x
                    return win_player

        ## check DIAGONAL \
        for x in range(self.num_row-3):
            for y in range(3, self.num_col):
                if self.matrix[x][y] != 0 and \
                    self.matrix[x][y] == self.matrix[x+1][y-1] and \
                    self.matrix[x+1][y-1] == self.matrix[x+2][y-2] and \
                    self.matrix[x+2][y-2] == self.matrix[x+3][y-3]:
                    win_player = self.matrix[x][y]
                    print "\nDIAGONAL WINNER! Column", y-3, "through", y
                    return win_player

        ## check DIAGONAL /
        for y in range(self.num_col-3):
            for x in range(self.num_row-3):
                if self.matrix[x][y] != 0 and \
                    self.matrix[x][y] == self.matrix[x+1][y+1] and \
                    self.matrix[x+1][y+1] == self.matrix[x+2][y+2] and \
                    self.matrix[x+2][y+2] == self.matrix[x+3][y+3]:
                    win_player = self.matrix[x][y]
                    print "\nDIAGONAL WINNER! Column", y, "through", y+3
                    return win_player
        return win_player

    def is_full(self):
    ## check if there are any available spots left on the gameboard
    ## return True if gameboard is full
        for x in range(self.num_row):
            for y in range(self.num_col):
                if self.matrix[x][y] == 0:
                    return False
        return True

    def make_move(self, player, column):
    ## update the gameboard for a given turn
    ## player can be either 1 or 2
    ## location will be a column between 0-6
        assert player == 1 or player == 2
        assert column >= 0 and column < self.num_col

        y = column
        for x in range(self.num_row):
            if self.matrix[x][y] == 0:
                self.matrix[x][y] = player
                return

    def valid_input(self, userinput):
        ## validate userinput as number 0-6
        try:
            userinput = int(userinput)
        except ValueError:
            return False

        ## validate column is in range and available
        if userinput >= 0 and userinput < self.num_col:
            column = userinput
            if self.matrix[self.num_row-1][column] != 0:
                return False
            else:
                return True
        else:
            return False

turn = 0
playing = True

while playing:
    ## create new gameboard
    if turn == 0:
        board = Board()
        player = 1
        winner = 0
        print ""
        print "Welcome to my ConnectFour clone!"
        print board

    ## let players take turns
    assert winner == 0

    while player == 1 and winner == 0:
        userinput = raw_input("X, pick column number:")
        if board.valid_input(userinput):
            column = int(userinput)
            board.make_move(player, column)
            turn += 1
            winner = board.win_condition()
            print board
            player = 2
        else:
            print "That's not a valid input. Try again."
            print "Select a column 0-6, which is open."

    while player == 2 and winner == 0:
        userinput = raw_input("O, pick column number:")
        if board.valid_input(userinput):
            column = int(userinput)
            board.make_move(player, column)
            turn += 1
            winner = board.win_condition()
            print board
            player = 1
        else:
            print "That's not a valid input. Try again."
            print "Select a column 0-6, which is open."

    ## check for tie
    if board.is_full():
        print "Nobody wins, it's a draw!"
        playing = False
        break

    ## check for winner
    if winner == 1:
        print "X wins! Great job"
        playing = False
        break

    elif winner == 2:
        print "O wins! Great job"
        playing = False
        break
