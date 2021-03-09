"""
his is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""


def solution(A):
    A = sorted(set(A))
    counter = A[0]
    # fails when only one int in list is negative and set will put it at last
    if A[0] < 0:
        return 1

    for i in A:
        if counter == i:
            counter += 1
        else:
            return counter
    return counter


print(solution([-1, -3]))


# perfect solution
def solution(A):
    A.sort()
    A = list(filter(lambda x: x > 0, A))
    n = len(A)
    if n == 0 or A[0] != 1:
        return 1
    for i in range(n - 1):
        if A[i + 1] - A[i] > 1:
            return A[i] + 1
    return A[n - 1] + 1
