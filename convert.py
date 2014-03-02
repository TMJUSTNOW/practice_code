def int_to_string(x):
    '''converts an int into a string representation'''
    conversion_dict = {1:'1', 2:'2', 3:'3', 4:'4',
         5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 0:'0'}
    string_out = []
    abs_x = abs(x)

    if x == 0:
        return '0'

    while abs_x > 0:
        digit = abs_x % 10
        string_out.append(conversion_dict[digit])
        abs_x /= 10

    if x < 0:
        string_out.append('-')

    string_out.reverse()
    return ''.join(string_out)


if __name__ == '__main__':
    print int_to_string(42)
    print int_to_string(24)
