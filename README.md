# Linear Algebra Matrix Tool
I just wanted a basic tool for operating on matrices

* It can add or subtract any two rows
* It can multiply or divide any given row by a non-zero constant
* It can switch the location of any two rows

After each operation the table is printed showing 2 decimal places
I have a large example below

## New Feature
- Temporarily add a non-zero const to a row before performing an addition allowing 
a common operation to be done in one step where it used to take 3
```
0:|    1.00    2.00    1.00 |    0.00 |
1:|    5.00   12.00    0.00 |    1.00 |
 
Enter Command: add
Row to store end result: 1
Row to add to that row: 0
Temporary multiply row 0 by what const? (1): -5
Setting row 1 equal to the sum of row 1 and row 0(-5.0) is that correct? (Y/n): 
 
0:|    1.00    2.00    1.00 |    0.00 |
1:|    0.00    2.00   -5.00 |    1.00 |
```

## Future Features
- Specify a csv file for matrix input
- Automatically find the Echelon and reduced row Echelon forms detailing the steps taken

## Warning
There are no test cases and there is almost no error handling for invalid input (beyond the scope of its purpose)

## Usage
Before running the program you just need to hard code in the matrix you
want to start with.

Once you start the program, this is an example flow of finding the `Reduced Row Echelon Form` of a pretty decent sized augmented matrix 
(Note: I probably did not do a very good job solving this one because I am just starting out but the final solution is correct):

```
0:|    4.00   -1.00    0.00   -1.00 |   30.00 |
1:|   -1.00    4.00   -1.00    0.00 |   60.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|   -1.00    0.00   -1.00    4.00 |   40.00 |
 
Enter Command: switch
Enter Row Index: 3
Enter Row Index: 0
Switching rows 3 and 0 is that correct? (Y/n): 
 
0:|   -1.00    0.00   -1.00    4.00 |   40.00 |
1:|   -1.00    4.00   -1.00    0.00 |   60.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    4.00   -1.00    0.00   -1.00 |   30.00 |
 
Enter Command: multiply
Enter non-zero constant: -1
Enter the row to multiply: 0
Multiplying row 0 by -1 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|   -1.00    4.00   -1.00    0.00 |   60.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    4.00   -1.00    0.00   -1.00 |   30.00 |
 
Enter Command: add
Row to store end result: 1
Row to add to that row: 0
Setting row 1 equal to the sum of row 1 and row 0 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    4.00    0.00   -4.00 |   20.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    4.00   -1.00    0.00   -1.00 |   30.00 |
 
Enter Command: divide
Enter non-zero constant: 4
Enter the row to divide: 1
Dividing row 1 by 4 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    4.00   -1.00    0.00   -1.00 |   30.00 |
 
Enter Command: subtract
Row to store end result: 3
Row to subtract from that row: 0
Setting row 3 equal to row 3 minus row 0 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    3.00   -1.00   -1.00    3.00 |   70.00 |
 
Enter Command: subtract
Row to store end result: 3
Row to subtract from that row: 0
Setting row 3 equal to row 3 minus row 0 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    2.00   -1.00   -2.00    7.00 |  110.00 |
 
Enter Command: subtract
Row to store end result: 3
Row to subtract from that row: 0
Setting row 3 equal to row 3 minus row 0 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    1.00   -1.00   -3.00   11.00 |  150.00 |
 
Enter Command: subtract
Row to store end result: 3
Row to subtract from that row: 0
Setting row 3 equal to row 3 minus row 0 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00   -1.00    4.00   -1.00 |   70.00 |
3:|    0.00   -1.00   -4.00   15.00 |  190.00 |
 
Enter Command: add
Row to store end result: 2
Row to add to that row: 1
Setting row 2 equal to the sum of row 2 and row 1 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00    0.00    4.00   -2.00 |   75.00 |
3:|    0.00   -1.00   -4.00   15.00 |  190.00 |
 
Enter Command: add
Row to store end result: 3
Row to add to that row: 1
Setting row 3 equal to the sum of row 3 and row 1 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00    0.00    4.00   -2.00 |   75.00 |
3:|    0.00    0.00   -4.00   14.00 |  195.00 |
 
Enter Command: add
Row to store end result: 3
Row to add to that row: 2
Setting row 3 equal to the sum of row 3 and row 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00    0.00    4.00   -2.00 |   75.00 |
3:|    0.00    0.00    0.00   12.00 |  270.00 |
 
Enter Command: divide
Enter non-zero constant: 12
Enter the row to divide: 3
Dividing row 3 by 12 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00    0.00    4.00   -2.00 |   75.00 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: divides
Enter non-zero constant: 4
Enter the row to divide: 2
Dividing row 2 by 4 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00   -4.00 |  -40.00 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: subtract
Row to store end result: 0
Row to subtract from that row: 2
Setting row 0 equal to row 0 minus row 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00   -3.50 |  -58.75 |
1:|    0.00    1.00    0.00   -1.00 |    5.00 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: add
Row to store end result: 1
Row to add to that row: 3
Setting row 1 equal to the sum of row 1 and row 3 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00   -3.50 |  -58.75 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: multiply
Enter non-zero constant: 4
Enter the row to multiply: 3
Multiplying row 3 by 4 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00   -3.50 |  -58.75 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    4.00 |   90.00 |
 
Enter Command: add
Row to store end result: 0
Row to add to that row: 3
Setting row 0 equal to the sum of row 0 and row 3 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00    0.50 |   31.25 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    4.00 |   90.00 |
 
Enter Command: divide
Enter non-zero constant: 4
Enter the row to divide: 3
Dividing row 3 by 4 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00    0.50 |   31.25 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: add
Row to store end result: 0
Row to add to that row: 2
Setting row 0 equal to the sum of row 0 and row 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00    0.00 |   50.00 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    1.00   -0.50 |   18.75 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: multiply
Enter non-zero constant: 2
Enter the row to multiply: 2
Multiplying row 2 by 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00    0.00 |   50.00 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    2.00   -1.00 |   37.50 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: add
Row to store end result: 2
Row to add to that row: 3
Setting row 2 equal to the sum of row 2 and row 3 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00    0.00 |   50.00 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    2.00    0.00 |   60.00 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: divide
Enter non-zero constant: -2
Enter the row to divide: 2
Dividing row 2 by -2 is that correct? (Y/n): 
 
0:|    1.00    0.00    1.00    0.00 |   50.00 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00   -1.00    0.00 |  -30.00 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: add
Row to store end result: 0
Row to add to that row: 2
Setting row 0 equal to the sum of row 0 and row 2 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00    0.00 |   20.00 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00   -1.00    0.00 |  -30.00 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
 
Enter Command: multiply
Enter non-zero constant: -1
Enter the row to multiply: 2
Multiplying row 2 by -1 is that correct? (Y/n): 
 
0:|    1.00    0.00    0.00    0.00 |   20.00 |
1:|    0.00    1.00    0.00    0.00 |   27.50 |
2:|    0.00    0.00    1.00    0.00 |   30.00 |
3:|    0.00    0.00    0.00    1.00 |   22.50 |
```