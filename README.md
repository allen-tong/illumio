# Illumio - System Test Intern

###### 1) Max Value:

There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal value in these houses, but he cannot steal in two adjacent houses because the owner of a robbed house will tell his two neighbors on the left and right side.

For e.g. if there are four houses with values {6, 1, 2, 7}, the maximum stolen value is 13 when the first and fourth houses are robbed.

Write a program to determine the maximum value that the thief can steal given dynamic values for n houses.

###### 2) Grid Folding:

You have a square sheet of grid paper, 16 cells across by 16 down. A number is written in each cell, starting at 1 in the upper-left corner, going across each line then down the paper, ending with 256 in the lower-right corner.

Write a function to fold the paper in half repeatedly (along the horizontal or vertical middle), until you are left with a single cell, 256 layers thick, and report back on the order of those layers, top to bottom.

The input to the function is a string containing the characters, "T" (the top edge folded down to the bottom edge), "B" (bottom up to top), "R" (right to left) and "L" (left to right). Not every combination of those will be valid, so make sure you verify your input. Output will be an Array of Integers from 1 to 256, arranged in the top-to-bottom layer order after all folds are done.

Simplified example of a 2x2 grid:
fold("RB") => [3,4,2,1]
fold("TL") => [3,1,2,4]
fold("LR") => raise exception for invalid input
