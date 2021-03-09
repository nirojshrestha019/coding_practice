def solution(A, K):
    n = len(A)
    B = [None] * n
    for i in range(0, n):
        B[(i + K) % n] = A[i]
    return B

# OR
# def solution(A, K):
#     """
#     Rotate the array A by k steps
#     :param A: an array of integers
#     :param K: number of times to shift right
#     :return: the rotated array
#     """
#     # A is empty
#     if not len(A):
#         return A

#     # netK is the net number of shifts to apply (omits spinning round and round)
#     netK = (len(A) + K) % len(A)
#     if netK > 0:
#         head = A[len(A)-netK:]
#         tail = A[:-netK]
#         return head + tail
#     else:
#         return A


A = [3, 8, 9, 7, 6]
K = 2
print(solution(A, K))
