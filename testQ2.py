# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    pass


A = [[1, 0, 0],
     [0, 0, 0],
     [0, 0, 1],
     [0, 1, 0]]
print(A)
numrows = len(A)
numcols = len(A[0])
print(numrows, numcols)

k = 1
for i, each_row in enumerate(A):
    print(i, each_row)
    for j, each_element in enumerate(each_row):

        print(i, j, each_element)
        if each_element == 1:
            temp_row = [x for x in range(i-k)]
            temp_col =
