from sys import stdin, stdout
'''
Problem: https://practice.geeksforgeeks.org/problems/next-larger-element/0
The approach is similar to the 'useful' element approach in
Max in all sub arrays of size K problem.
We maintain a stack. Whenever a new element comes, we remove all elements that
are less than this elem from top of the stack. Then we add this element to the stack.
'''


def next_max(A):
    stack = []
    stack.append(A[-1])
    nextmax = ['-1'] * len(A)

    for i in range(len(A)-2, -1, -1):
        while len(stack) > 0 and int(stack[-1]) < int(A[i]):
            stack.pop()

        if len(stack) > 0:
            nextmax[i] = stack[-1]

        stack.append(A[i])

    stdout.write(' '.join(nextmax) + '\n')


def main():
    T = int(stdin.readline())
    for i in range(T):
        N = int(stdin.readline())
        # convert to int when required
        A = stdin.readline().strip().split()
        next_max(A)


if __name__ == '__main__':
    main()
