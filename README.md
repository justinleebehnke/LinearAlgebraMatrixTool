# LinearAlgebraMatrixTool
I just wanted a basic tool for operating on matrices

* It can add or subtract any two rows
* It can multiply or divide any given row by a non-zero constant
* It can switch the location of any two rows

After each operation the table is printed showing 2 decimal places

## Usage
Before running the program you just need to hard code in the matrix you
want to start with.

Once you start the process this is an example flow of finding the Reducded Row Echelon form of a simple matrix

```
0:|    1.00    2.00    4.00 |    5.00 |
1:|    2.00    4.00    5.00 |    4.00 |
2:|    4.00    5.00    4.00 |   -1.00 |
 
Enter Command: divide
Enter non-zero constant: 2
Enter the row to divide: 1
Dividing row 1 by 2 is that correct? (Y/n): n
Cancelled
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    2.00    4.00    5.00 |    4.00 |
2:|    4.00    5.00    4.00 |   -1.00 |
 
Enter Command: subtract
Row to store end result: 2
Row to subtract from that row: 1
Setting row 2 equal to row 2 minus row 1 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    2.00    4.00    5.00 |    4.00 |
2:|    2.00    1.00   -1.00 |   -5.00 |
 
Enter Command: subtract
Row to store end result: 1
Row to subtract from that row: 2
Setting row 1 equal to row 1 minus row 2 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    0.00    3.00    6.00 |    9.00 |
2:|    2.00    1.00   -1.00 |   -5.00 |
 
Enter Command: subtract
Row to store end result: 2
Row to subtract from that row: 0
Setting row 2 equal to row 2 minus row 0 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    0.00    3.00    6.00 |    9.00 |
2:|    1.00   -1.00   -5.00 |  -10.00 |
 
Enter Command: subtract
Row to store end result: 2
Row to subtract from that row: 0
Setting row 2 equal to row 2 minus row 0 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    0.00    3.00    6.00 |    9.00 |
2:|    0.00   -3.00   -9.00 |  -15.00 |
 
Enter Command: add
Row to store end result: 2
Row to add to that row: 1
Setting row 2 equal to the sum of row 2 and row 1 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    0.00    3.00    6.00 |    9.00 |
2:|    0.00    0.00   -3.00 |   -6.00 |
 
Enter Command: divide
Enter non-zero constant: 3
Enter the row to divide: 1
Dividing row 1 by 3 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    0.00    1.00    2.00 |    3.00 |
2:|    0.00    0.00   -3.00 |   -6.00 |
 
Enter Command: divide
Enter non-zero constant: -3
Enter the row to divide: 2
Dividing row 2 by -3 is that correct? (Y/n): 
 
0:|    1.00    2.00    4.00 |    5.00 |
1:|    0.00    1.00    2.00 |    3.00 |
2:|    0.00    0.00    1.00 |    2.00 |
 
Enter Command: subtract
Row to store end result: 0
Row to subtract from that row: 1
Setting row 0 equal to row 0 minus row 1 is that correct? (Y/n): 
 
0:|    1.00    1.00    2.00 |    2.00 |
1:|    0.00    1.00    2.00 |    3.00 |
2:|    0.00    0.00    1.00 |    2.00 |
 
Enter Command: subtract
Row to store end result: 0
Row to subtract from that row: 1
Setting row 0 equal to row 0 minus row 1 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00 |   -1.00 |
1:|    0.00    1.00    2.00 |    3.00 |
2:|    0.00    0.00    1.00 |    2.00 |
 
Enter Command: subtract
Row to store end result: 1
Row to subtract from that row: 2
Setting row 1 equal to row 1 minus row 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00 |   -1.00 |
1:|    0.00    1.00    1.00 |    1.00 |
2:|    0.00    0.00    1.00 |    2.00 |
 
Enter Command: subtract
Row to store end result: 1
Row to subtract from that row: 2
Setting row 1 equal to row 1 minus row 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00 |   -1.00 |
1:|    0.00    1.00    0.00 |   -1.00 |
2:|    0.00    0.00    1.00 |    2.00 |
```

## Warning
There are no test cases and there is almost no error handling for invalid input (beyond the scope of its purpose)
