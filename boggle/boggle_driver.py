#!/usr/bin/env python

from boggle import Board, traverse_board

if __name__ == '__main__':
    board = Board(4, 4)
    # neighbors = board.get_neighbors(8)

    input_string = 'thecatisntthehat'
    board.fill_board(input_string)
    print(board)
    target = 'tis'

    found = traverse_board(board, input_string, target, 'breadth')
    print(found)
