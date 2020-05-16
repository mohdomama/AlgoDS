from collections import deque
from sys import stdin, stdout
'''
Given an array and an integer K,
find the maximum for each and every
contiguous subarray of size k.

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6

'''

##############################################

'''
Deque Approach. Storing elements in "useful" order O(n).
Other approach: AVL trees. O(nlgk)
Link: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
'''


def print_max_elem(A, K):
    q = deque()

    for i in range(K):
        while q and A[q[-1]] < A[i]:
            q.pop()
        q.append(i)
    stdout.write(str(A[q[0]]) + ' ')

    for i in range(K, len(A)):
        while q and q[0] <= i-K:
            q.popleft()


        while q and A[q[-1]] <= A[i]:
            q.pop()

        q.append(i)

        stdout.write(str(A[q[0]]) + ' ')

    stdout.write('\n')



def main():
    '''
    Map is faster than comprehesion for simple funcitons
    stdin/stdout is faster than print
    '''
    T = int(stdin.readline())  # for single input
    for i in range(T):
        N, K = map(int, stdin.readline().strip().split())
        A = list(map(int, stdin.readline().strip().split()))

        print_max_elem(A, K)
        # stdout.write(' '.join([str(N), str(K), '\n']))
        # stdout.write(' '.join(map(str, A)) + '\n')


if __name__ == '__main__':
    main()
