To run:
change board and search parameters in boggle_driver.py
run boggle_driver.py


Board dimentions:
    board = Board(width, height)
    input_string = 'this is the string that populates the board'
    if input_string is too long: board will not overflow
    if input_string is too short: raise Exception('string is too small')
    
    board.fill_board(input_string)
    print(board)
    
Search:
    target = 'this is the string that you are searching for'
    found = traverse_board(board, input_string, target, 'breadth')
    
    print(found)
    
    found is returned as a list of lists, where each list is the indices of board for chars in target
    
Example:
    input_string = 'thecatisntthehat'
    target = 'tis'

    board:    
 t h e c
 a t i s
 n t t h
 e h a t

[[5, 6, 7], [9, 6, 7], [10, 6, 7]]

    found the 'tis' 3 times in the board 
    
