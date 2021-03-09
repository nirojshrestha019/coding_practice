

# sol 1


def minpositive(a):
    A = set(a)
    ans = 1
    while ans in A:
        ans += 1
    return ans

# sol 2


def solution(A):
    sorted_set = set(sorted(A))
    sol = 1
    for x in sorted_set:
        if x == sol:
            sol += 1
        else:
            break
    return sol


data_list = [-2, 5, -5, 6, 9, 1]
print("minpositive: ", minpositive(data_list))
print("solution: ", solution(data_list))
