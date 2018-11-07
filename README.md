# Illumio - System Test Intern

###### 1) Max Value:

`usage: python max_value.py <values>`

```
$ python max_value.py 6 1 2 7
13.0
```

There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal value in these houses, but he cannot steal in two adjacent houses because the owner of a robbed house will tell his two neighbors on the left and right side.

For e.g. if there are four houses with values {6, 1, 2, 7}, the maximum stolen value is 13 when the first and fourth houses are robbed.

Write a program to determine the maximum value that the thief can steal given dynamic values for n houses.

</br>

###### 2) Grid Folding:

`usage: python grid_folding.py <sequence>`

```
$ python grid_folding.py TBRLTBRL
[165, 85, 37, 213, 220, 44, 92, 172, 173, 93, 45, 221, 212, 36, 84, 164, 148, 100, 20, 228, 237, 29, 109, 157, 156, 108, 28, 236, 229, 21, 101, 149, 133, 117, 5, 245, 252, 12, 124, 140, 141, 125, 13, 253, 244, 4, 116, 132, 180, 68, 52, 196, 205, 61, 77, 189, 188, 76, 60, 204, 197, 53, 69, 181, 184, 72, 56, 200, 201, 57, 73, 185, 192, 80, 64, 208, 193, 49, 65, 177, 129, 113, 1, 241, 256, 16, 128, 144, 137, 121, 9, 249, 248, 8, 120, 136, 152, 104, 24, 232, 233, 25, 105, 153, 160, 112, 32, 240, 225, 17, 97, 145, 161, 81, 33, 209, 224, 48, 96, 176, 169, 89, 41, 217, 216, 40, 88, 168, 167, 87, 39, 215, 218, 42, 90, 170, 175, 95, 47, 223, 210, 34, 82, 162, 146, 98, 18, 226, 239, 31, 111, 159, 154, 106, 26, 234, 231, 23, 103, 151, 135, 119, 7, 247, 250, 10, 122, 138, 143, 127, 15, 255, 242, 2, 114, 130, 178, 66, 50, 194, 207, 63, 79, 191, 186, 74, 58, 202, 199, 55, 71, 183, 182, 70, 54, 198, 203, 59, 75, 187, 190, 78, 62, 206, 195, 51, 67, 179, 131, 115, 3, 243, 254, 14, 126, 142, 139, 123, 11, 251, 246, 6, 118, 134, 150, 102, 22, 230, 235, 27, 107, 155, 158, 110, 30, 238, 227, 19, 99, 147, 163, 83, 35, 211, 222, 46, 94, 174, 171, 91, 43, 219, 214, 38, 86, 166]
```

You have a square sheet of grid paper, 16 cells across by 16 down. A number is written in each cell, starting at 1 in the upper-left corner, going across each line then down the paper, ending with 256 in the lower-right corner.

Write a function to fold the paper in half repeatedly (along the horizontal or vertical middle), until you are left with a single cell, 256 layers thick, and report back on the order of those layers, top to bottom.

The input to the function is a string containing the characters, "T" (the top edge folded down to the bottom edge), "B" (bottom up to top), "R" (right to left) and "L" (left to right). Not every combination of those will be valid, so make sure you verify your input. Output will be an Array of Integers from 1 to 256, arranged in the top-to-bottom layer order after all folds are done.

Simplified example of a 2x2 grid:
fold("RB") => [3,4,2,1]
fold("TL") => [3,1,2,4]
fold("LR") => raise exception for invalid input
