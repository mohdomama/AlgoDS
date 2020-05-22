'''
Problem: https://practice.geeksforgeeks.org/problems/stock-span-problem/0
- We use stack to solve it in O(n)
'''


def print_span(C, N):
    span = [0] * N
    stack = []

    stack.append(0)
    span[0] = 1

    for i in range(1, N):
        # This is more pythonic way than len(Stack) > 0
        count = 1
        while stack and C[stack[-1]] <= C[i]:
            count += span[stack[-1]]
            stack.pop()

        stack.append(i)
        span[i] = count

    print(' '.join(list(map(str, span))))


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        print_span(C, N)


if __name__ == '__main__':
    main()
