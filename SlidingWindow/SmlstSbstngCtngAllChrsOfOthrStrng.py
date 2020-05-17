from sys import stdin, stdout
'''
Smallest window in a string containing all the characters of another string 
Problem: https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string/0#ExpectOP
- We use hash and two pointers
'''


def is_satis(reqhash, prsnthash):
    for i in reqhash.keys():
        if reqhash[i] > prsnthash[i]:
            return False
    return True


def smallest_substring(N, X):
    reqhash, prsnthash = {}, {}

    for i in X:
        reqhash[i] = reqhash.get(i, 0) + 1
        prsnthash[i] = 0

    p1, p2, minp1, minp2 = 0, 0, -1, len(N)

    if N[p2] in prsnthash:
        prsnthash[N[p2]] += 1

    while p2 < len(N):
        if is_satis(reqhash, prsnthash):
            if (minp2 - minp1) > (p2 - p1):
                minp2, minp1 = p2, p1

            if N[p1] in prsnthash:
                prsnthash[N[p1]] -= 1
            p1 += 1

            while (p1 < p2) and N[p1] not in prsnthash:
                p1 += 1

        else:
            p2 += 1
            if p2 < len(N):
                if N[p2] in prsnthash:
                    prsnthash[N[p2]] += 1

    if minp1 == -1:
        print('-1')
    else:
        print(N[minp1:minp2+1])


def main():

    T = int(stdin.readline())
    for i in range(T):
        N = stdin.readline().strip()
        X = stdin.readline().strip()
        smallest_substring(N, X)


if __name__ == '__main__':
    main()
