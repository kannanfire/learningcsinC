#! /usr/bin/env python3

import unittest

'''
This file is for methods to find the least common substring between two strings of varying length.
Exploring Dynamic Programming and the methods to reduce work in this problem.
'''



def printArr(arr: list):
    for i in arr:
        print(i)

def lcs1(a: str, b: str):
    arr  = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    
    for i in range(1, len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    printArr(arr)
                    
def laux(a: str, b: str, arr: list):
    print('a: ' + a)
    print('b: ' + b)
    printArr(arr)
    if len(a) <= 0 or len(b) <= 0:
        return 0
    if a[-1] == b[-1]:
        arr[len(a)][len(b)] = arr[len(a)][len(b)+1] + 1
        return laux(a[0:-1], b[0:-1], arr)

    arr[len(a)][len(b)] = max(laux(a[0:-1], b, arr), laux(a, b[0:-1], arr))
    return arr[len(a)][len(b)]

def lcs(A: str, B: str, S: set):
    '''
    No memoization version of LCS
    '''
    # print("A: " + A + " | B: " + B)
    if len(A) <= 0 or len(B) <= 0:
        return 0

    if A[-1] == B[-1]:
        return lcs(A[0:-1], B[0:-1]) + 1

    return max(lcs(A[0:-1], B), lcs(A, B[0:-1]))


def lcs_memo(a: str, b: str):
    '''
    Regular Method that calls aux for memoized version of LCS
    '''
    return aux1(a, b, {})

def aux1(a: str, b: str, m: map):
    '''
    Aux method for lcs_memo
    '''
    # print("A: " + a + " | B: " + b)
    if len(a) <= 0 or len(b) <= 0:
        return 0

    if (a,b) in m:
        return m[a,b]

    if a[-1] == b[-1]:
        m[a,b] = aux1(a[0:-1], b[0:-1], m) + 1
    else:
        m[a,b] = max(aux1(a[0:-1], b, m), aux1(a, b[0:-1], m))
    return m[a,b]


'''
the following class is to perform unit tests to verify if the methods are working appropriately.

the first lcs class (not lcs_memo) is the verification that the methods are correct. If lcs_memo matchs lcs
then this can be assumed as correct.
'''

class TestLCS(unittest.TestCase):

    def testEqualLength(self):
        a = "XYXYZAZB"
        b = "XXYYZZAB"

        self.assertEqual(lcs(a, b), lcs_memo(a, b))

        c = "BABABAB"
        d = "ABABABA"

        self.assertEqual(lcs(c, d), lcs_memo(c, d))
        

    def testVaryingLength(self):
        a = "XYXYXYXY"
        b = "XXYYXXYYXXYYXXYYXXYYXXYY"

        self.assertEqual(lcs(a, b), lcs_memo(a, b))

        c = "XXXXXXX"
        d = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

        self.assertEqual(lcs(c, d), lcs_memo(c,d))

    def testZeroLength(self):
        a = ""
        b = "XX"

        self.assertTrue(lcs_memo(a,b) == 0)
        self.assertTrue(lcs(a,b) == 0)

        self.assertEqual(lcs(a,b), lcs_memo(a,b))

        c = "YY"
        d = ""

        self.assertTrue(lcs_memo(c,d) == 0)
        self.assertTrue(lcs(d,c) == 0)

        self.assertEqual(lcs(c,d), lcs_memo(c,d))

    def testNotEqual(self):
        a = "AAAAA"
        b = "BBBBB"

        self.assertTrue(lcs_memo(a,b) == 0)
        self.assertFalse(lcs_memo(a,b) != 0)

        self.assertEqual(lcs(a,b), lcs_memo(a,b))

    def testSameValues(self):
        a = "aaaaa"
        b = "aaaaa"

        self.assertEqual(lcs(a,b), lcs_memo(a,b))

        c = "bbbbbbbbb"
        d = "bbbbbbbbb"

        self.assertEqual(lcs_memo(c,d), lcs(c,d))

    def testRandomStrings(self):
        print()

    def testRandomStringsLong(self):
        print()


      

if __name__ == '__main__':
    a = "xyxyz"
    b = "xyabxyc"
    # unittest.main()
    print()
    arr = lcs1(a,b)
    print()
    lcs1("abcd", "dcba")