import numpy as np
import sys
class SudokuSolver:
  def __init__(self,matrix):
    self.mat = matrix
    
    # Pre-allocate numbers list for multiple use
    self.numbers = np.arange(1,10)

  def solve(self):
    if (np.all(np.logical_not(self.mat == 0))):
      print("Solution found!")
      print(self.mat) 
      return True
    
    # Find unsolved locations (2 arrays of size nidx, 1 for i and 1 for j)
    idx = np.where(self.mat==0)
    nidx = np.shape(idx)

    # Loop over all unsolved
    for n in range(0,nidx[1]):
      i = idx[0][n]
      j = idx[1][n]
      # Determine possible values for unsolved
      possible = self.numbers[self.possibleValues(i,j)]
      if len(possible) == 0:
        return False
      else:
        for val in possible:
          # Test possible values
          self.mat[i][j] = val
          if (self.solve() == False):
            # If it leads to conflict, revert
            self.mat[i][j] = 0
          else:
            return True
        return False

  def possibleValues(self,i,j):
    return np.logical_not(np.logical_or(np.logical_or(self.valuesInColumn(j),self.valuesInRow(i)),self.valuesInSquare(i,j)))

  def valuesInRow(self,i):
    # Check if the row finds an occurrence of any number in the list
    hasValues = [self.mat[i,:]==c for c in self.numbers]

    # Reduce the list for all the values in the row, so that we
    # obtain a single boolean per number
    return np.any(hasValues,axis=1)

  def valuesInColumn(self,j):
    # Check if the column finds an occurrence of any number in the list
    hasValues = [self.mat[:,j]==c for c in self.numbers]

    # Reduce the list for all the values in the column, so that we
    # obtain a single boolean per number
    return np.any(hasValues,axis=1)

  def valuesInSquare(self,i,j):
    # Get index of top-left of the square
    isl = 3*np.floor(i/3).astype('int')
    jsl = 3*np.floor(j/3).astype('int')

    # Get the current square, stretch it out to a single row
    sq = (self.mat[isl:isl+3,jsl:jsl+3]).reshape(9)

    # Check if the row finds an occurrence of any number in the list
    hasValues = [sq==c for c in self.numbers]

    # Reduce the list for all the values in the row, so that we
    # obtain a single boolean per number
    return np.any(hasValues,axis=1)


# a = S.possibleInColumn(0,2,8)
# b = S.possibleInRow(0,2,7)
# c = S.possibleInRow(0,2,1)
# d = S.possibleInSquare(1,1,8)

# print(a,b,c,d)
# S.checkPossibleValues(0,2,3)

