class Solution:
    def setZeroes(self, matrix):
        rows_with_zero = set()
        cols_with_zero = set()

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    rows_with_zero.add(i)
                    cols_with_zero.add(j)

        for i in rows_with_zero:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in cols_with_zero:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        return matrix
