from functools import cmp_to_key
'''
Problem: https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0
We have to take care of cases where there is a prefix. 
'''

# def cmp2(s1, s2):
#     '''
#     This solution is not intutuve and doesn't work on many test cases
#     '''
#     if s1 == s2:
#         return 0

#     # For handling prefix problem
#     if len(s1) > len(s2):
#         s2 += s2 * (len(s1) - len(s2))
#         s2 = s2[:len(s1)]
#         x = 1
#     elif len(s2) > len(s1):
#         s1 += s1 * (len(s2) - len(s1))
#         s1 = s1[:len(s2)]
#         x = -1

#     i = 0
#     while i < len(s1) and i < len(s2):
#         if int(s1[i]) < int(s2[i]):
#             return 1
#         if int(s1[i]) > int(s2[i]):
#             return -1
#         i += 1

#     return x


def cmp1(s1, s2):
    '''
    if arg 2 is greater than arg 1, return 1
    if arg 2 is smaller than arg 1, return -1
    else return 0
    '''
    X = s1 + s2
    Y = s2 + s1

    return int(Y) - int(X)


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = input().strip().split()
        A = sorted(A, key=cmp_to_key(cmp1))
        print(''.join(A))


if __name__ == '__main__':
    main()
