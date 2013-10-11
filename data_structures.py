class queue(object):
    def __init__(self):
        self.new_list = list()  # constructor same as []

    def __str__(self):
        return str(self.new_list)

    def push(self, new_element):
        self.new_list.append(new_element)

    def pop(self):
        return self.new_list.pop(0)


class stack(object):
    def __init__(self):
        self.new_list = list()  # constructor same as []

    def __str__(self):
        return str(self.new_list)

    def __len__(self):
        return len(self.new_list)

    def push(self, new_element):
        self.new_list.append(new_element)

    def pop(self):
        list_length = len(self.new_list)
        return self.new_list.pop(list_length - 1)

    def min(self):
        return self.min_list[0]


class stack_queue():  # make a queue out of stacks
    def __init__(self):
        self.new_stack = stack()

    def push(self, new_element):
        self.new_stack.push(new_element)

    def pop(self):
        stack1 = self.new_stack
        stack2 = stack()
        self.new_stack = stack()

        while len(stack1) != 1:
            stack2.push(stack1.pop())

        for i in range(len(stack2)):
            self.new_stack.push(stack2.pop())

        return stack1.pop()

    def __str__(self):
        return str(self.new_stack)


test_queue = stack_queue()
test_queue.push(9)
test_queue.push(5)
test_queue.push(7)
test_queue.push(-1)
print test_queue

test_queue.pop()
print test_queue

test_queue.pop()
print test_queue
