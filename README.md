# Sudoku solver

In the context of 'let's clean up some old tryouts and projects from my harddrive', here's a sudoku solver I made some time ago to get used to slicing/logical indexing operations in Python. 

# How to use

 * Create a Numpy 9x9 matrix with numbers, where a 0 indicates an empty box.
 * Create a solver instance using the matrix as init
 * Call the .solve method.
 * The result will be printed to the screen.

# Notes
* No solution is given in case an inconsistent input matrix is given
* No detection of cases with multiple solutions.

