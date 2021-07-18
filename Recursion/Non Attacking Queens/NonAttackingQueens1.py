# Lower Bound: O(n!) time | O(n) space - where n is the input number

def nonAttackingQueens(n):
    # Each index of `columnPlacements` represents a row of the chessboard,
    # and the value at each index is the column (on the relevant row) where
    # a queen is currently placed.
    columnPlacements = [0] * n
    return getNumberOfNonAttackingQueenPlacements(0, columnPlacements, n)

def getNumberOfNonAttackingQueenPlacements(row, columnPlacements, boardSize):
    if row == boardSize:
        return 1
    validPlacements = 0

    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, columnPlacements):
            columnPlacements[row] = col

            validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnPlacements, boardSize)
    return validPlacements

# As `row` tends to `n`, this becomes an O(n)-time operation.

def isNonAttackingPlacement(row, col, columnPlacements):
    for previousRow in range(row):

        columnToCheck = columnPlacements[previousRow]
        sameColumn = columnToCheck == col

        onDiagonal = abs(columnToCheck - col) == row - previousRow
        if sameColumn or onDiagonal:
            return False
    return True