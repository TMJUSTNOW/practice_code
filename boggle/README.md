#Background
* Setup, populate and search a "boggle" style board of (w * h) dimensions. 
* Board height & width, board fill string, target string and search type (breadth vs depth) are all abstracted out. 

#To run:
1. change board and search parameters in boggle_driver.py
2. run boggle_driver.py


#Board dimentions:
    board = Board(width, height)
    input_string = 'this is the string that populates the board'

* if input_string is too long: board will not overflow
* if input_string is too short: raise Exception('string is too small')

    
#Search:
    target = 'this is the string that you are searching for'
    found = traverse_board(board, input_string, target, search_type='depth')
    
* search_type can be 'depth' (default if not provided) or 'breadth'
* found is returned as a list of lists, where each list is the indices of board for chars in target
    
#Example:
    board = Board(4, 4)
    input_string = 'thecatisntthehat'
    board.fill_board(input_string)
    target = 'tis'
    found = traverse_board(board, input_string, target, 'breadth')
    print(found)

board: 

    t h e c
    a t i s
    n t t h
    e h a t

search returns:

    [[5, 6, 7], [9, 6, 7], [10, 6, 7]]

* found 'tis' 3 times in the board 
    
