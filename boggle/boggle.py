from storage import Stack, Queue


class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = ['0'] * (width * height)
        self.char_dict = {}

    def __str__(self):
        print_board = []
        for i in range(0, len(self.board)):
            print_board.append(' ')
            print_board.append(str(self.board[i]))

            if (i + 1) % self.width == 0:
                print_board.append('\n')

        return ''.join(print_board)

    def get_char(self, index):
        return self.board[index]

    def fill_board(self, string):
        if len(string) < self.width * self.height:
            raise Exception('string is too small')
        for index, char in enumerate(string):
            if index >= self.width * self.height:
                break
            self.board[index] = char

            # store char dict here
            self.add_to_char_dict(char, index)

    def add_to_char_dict(self, char, index):
        if char in self.char_dict:
            self.char_dict[char].append(index)
        else:
            self.char_dict[char] = [index]

    def get_char_indices(self, char):
        if char not in self.char_dict:
            return []
        return self.char_dict[char]

    def get_neighbors(self, index):
        neighbors = []
        if index >= len(self.board):
            raise IndexError
        left = self.has_left(index)
        right = self.has_right(index)
        top = self.has_top(index)
        bottom = self.has_bottom(index)

        if left:
            neighbors.append(index - 1)
        if right:
            neighbors.append(index + 1)
        if top:
            neighbors.append(index - self.width)
        if bottom:
            neighbors.append(index + self.width)
        if left and top:
            neighbors.append(index - self.width - 1)
        if right and top:
            neighbors.append(index - self.width + 1)
        if left and bottom:
            neighbors.append(index + self.width - 1)
        if right and bottom:
            neighbors.append(index + self.width + 1)
        return neighbors

    def has_left(self, index):
        return (index + 1) % self.width != 1

    def has_right(self, index):
        return (index + 1) % self.width != 0

    def has_top(self, index):
        return index >= self.width

    def has_bottom(self, index):
        return index < (self.width * self.height) - self.width


def traverse_board(board, input_string, target, search_type='depth'):
    def search(search_type):
        search_type = Stack() if search_type == 'depth' else Queue()
        return search_type

    open_paths = search(search_type)
    found_target_path = []
    i = 0
    start = target[i]

    if start in board.char_dict:
        for node in board.char_dict[start]:
            open_paths.put([node])

        # for start_index in board.get_char_indices(start):
        #     traverse_path(board.get_neighbors(start_index), [node])

        while len(open_paths) > 0 and i < len(target):
            current_path = open_paths.get()
            i = len(current_path)
            nodes = board.get_neighbors(current_path[-1])
            occurances = board.char_dict[target[i]]
            available_nodes = set.intersection(set(occurances), set(nodes))
            for node in available_nodes:
                if node not in current_path:
                    new_path = current_path + [node]
                    if len(new_path) == len(target):
                        found_target_path.append(new_path)
                    else:
                        open_paths.put(new_path)
        return found_target_path
    return False
