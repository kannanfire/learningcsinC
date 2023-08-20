#! /usr/bin/env python3

'''
DOCSTRING
'''

def lcs(A: str, B: str):
    '''
    DOCSTRING
    '''
    print("A: " + A + " | B: " + B)
    if len(A) <= 0 or len(B) <= 0:
        return 0

    if A[-1] == B[-1]:
        return lcs(A[0:-1], B[0:-1]) + 1

    return max(lcs(A[0:-1], B), lcs(A, B[0:-1]))


def lcs_memo(a: str, b: str):
    '''
    DOCSTRING
    '''
    return aux1(a, b, {})

def aux1(a: str, b: str, m: map):
    '''
    DOCSTRING
    '''
    print("A: " + a + " | B: " + b)
    if len(a) <= 0 or len(b) <= 0:
        return 0

    if (a,b) in m:
        return m[a,b]

    if a[-1] == b[-1]:
        m[a,b] = aux1(a[0:-1], b[0:-1], m) + 1
    else:
        m[a,b] = max(aux1(a[0:-1], b, m), aux1(a, b[0:-1], m))
    return m[a,b]


if __name__ == '__main__':
    # A = "ABCADB"
    # B = "BABDCAB"
    # print(lcs(A, len(A), B, len(B)))
    S1 = "XYXYZ"
    S2 = "XYABXYC"
    print(lcs(S1, S2))
    print("--------------------------------------------------\n\n")
    print(lcs_memo(S1, S2))
