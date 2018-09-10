def main():
    matrix = [
        [4.0, -1.0, 0.0, -1.0, 30.0],
        [-1.0, 4.0, -1.0, 0.0, 60.0],
        [0.0, -1.0, 4.0, -1.0, 70.0],
        [-1.0, 0.0, -1.0, 4.0, 40.0]
    ]

    text = 'null'

    while text != 'quit':
        print_matrix(matrix)
        text = input('Enter Command: ')
        if text == 'switch':
            switch_rows(matrix)
        elif text == 'multiply':
            multiply(matrix)
        elif text == 'divide':
            divide(matrix)
        elif text == 'add':
            add_rows(matrix, False)
        elif text == 'subtract':
            add_rows(matrix, True)
        else:
            print('usage: switch | add | subtract | multiply | divide | quit')


def add_rows(matrix, subtract):
    row_to_modify = input('Row to store end result: ')
    row_to_subtract = -1
    row_to_add = -1

    if subtract:
        row_to_subtract = input('Row to subtract from that row: ')
        confirm = input('Setting row ' + row_to_modify + ' equal to row ' + row_to_modify +
                        ' minus row ' + row_to_subtract + ' is that correct? (Y/n): ')
        confirm = confirm.lower()
    else:
        row_to_add = input('Row to add to that row: ')
        confirm = input('Setting row ' + row_to_modify + ' equal to the sum of row ' + row_to_modify +
                        ' and row ' + row_to_add + ' is that correct? (Y/n): ')
        confirm = confirm.lower()

    if confirm == 'n':
        print('Cancelled')
    else:
        if subtract:
            subtract_row_helper(matrix, row_to_subtract, row_to_modify)
        else:
            add_row_helper(matrix, row_to_add, row_to_modify)


def subtract_row_helper(matrix, row_to_subtract, row_to_modify):
    row_to_subtract = int(row_to_subtract)
    row_to_modify = int(row_to_modify)

    for i in range(len(matrix[row_to_modify])):
        matrix[row_to_modify][i] = matrix[row_to_modify][i] - matrix[row_to_subtract][i]


def add_row_helper(matrix, row_to_add, row_to_modify):
    row_to_add = int(row_to_add)
    row_to_modify = int(row_to_modify)

    for i in range(len(matrix[row_to_modify])):
        matrix[row_to_modify][i] = matrix[row_to_modify][i] + matrix[row_to_add][i]


def divide(matrix):
    const_to_divide_by = input('Enter non-zero constant: ')
    row_to_divide = input('Enter the row to divide: ')
    confirm = input('Dividing row ' + row_to_divide + ' by ' + const_to_divide_by +
                    ' is that correct? (Y/n): ')
    confirm = confirm.lower()
    if confirm == 'n':
        print('Cancelled')
    else:
        divide_helper(matrix, row_to_divide, const_to_divide_by)


def divide_helper(matrix, row_to_divide, const_to_divide_by):
    row_to_divide = int(row_to_divide)
    const_to_divide_by = float(const_to_divide_by)

    for i in range(len(matrix[row_to_divide])):
        matrix[row_to_divide][i] = matrix[row_to_divide][i] / const_to_divide_by


def multiply(matrix):
    const_to_multiply = input('Enter non-zero constant: ')
    row_to_multiply = input('Enter the row to multiply: ')
    confirm = input('Multiplying row ' + row_to_multiply + ' by ' + const_to_multiply +
                    ' is that correct? (Y/n): ')
    confirm = confirm.lower()
    if confirm == 'n':
        print('Cancelled')
    else:
        multiply_helper(matrix, row_to_multiply, const_to_multiply)


def multiply_helper(matrix, row_to_multiply, const_to_multiply):
    row_to_multiply = int(row_to_multiply)
    const_to_multiply = float(const_to_multiply)

    for i in range(len(matrix[row_to_multiply])):
        matrix[row_to_multiply][i] = matrix[row_to_multiply][i] * const_to_multiply


def switch_rows(matrix):
    row1 = input('Enter Row Index: ')
    row2 = input('Enter Row Index: ')
    confirm = input('Switching rows ' + row1 + ' and ' + row2 +
                    ' is that correct? (Y/n): ')
    confirm = confirm.lower()
    if confirm == 'n':
        print('Cancelled')
    else:
        switch_row_helper(matrix, row1, row2)


def switch_row_helper(matrix, row1, row2):
    row1 = int(row1)
    row2 = int(row2)

    copy = []
    for i in range(len(matrix[row1])):
        copy.append(matrix[row1][i])

    matrix[row1] = matrix[row2]
    matrix[row2] = copy


def print_matrix(matrix):
    print(' ')
    for i in range(len(matrix)):
        row_to_print = str(i) + ':|'
        for j in range(len(matrix[i])):
            if abs(matrix[i][j]) < 0.001:
                matrix[i][j] = 0.0
            spaces = ' '
            if matrix[i][j] >= 0:
                spaces += ' '
            if abs(matrix[i][j]) < 10:
                spaces += ' '
            if abs(matrix[i][j]) < 100:
                spaces += ' '
            row_to_print += spaces
            # + str(matrix[i][j])
            row_to_print += format(matrix[i][j], '.2f')

            if (j + 2) == len(matrix[i]):
                row_to_print += ' |'
        row_to_print += ' |'
        print(row_to_print)
    print(' ')


if __name__ == '__main__':
    main()
