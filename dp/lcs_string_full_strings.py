#! /usr/bin/env python3

import unittest

'''
This file is for methods to find the least common substring between two strings of varying length.
Exploring Dynamic Programming and the methods to reduce work in this problem.
'''



def printArr(arr: list):
    print()
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
    print("a: " + a + " b: " + b)
    # ret = ""
    # curr = 0
    # for i in range(1,len(arr)):
    #     for j in range(1,len(arr[0])):
    #         if arr[i][j] > curr:
    #             ret += a[i-1]
    #             curr = arr[i][j]
    #         else:

    ret = aux(a,b,arr,len(arr)-1,len(arr[0])-1)      
    print(ret)
    # print(ret)

def aux(a: str, b: str, arr: list, i: int, j: int) -> str:
    if i <= 0 or j <= 0 or arr[i][j] == 0:
        return [""]

    if a[i-1] == b[j-1]:
        return [x + a[i-1] for x in aux(a, b, arr, i-1, j-1)]
    else:
        if arr[i-1][j] > arr[i][j-1]:
            return aux(a, b, arr, i-1, j)
        elif arr[i-1][j] < arr[i][j-1]:
            return aux(a, b, arr, i, j-1)
        else:
            # v1 = aux(a,b,arr,i-1,j)
            # v2 = aux(a,b,arr,i,j-1)

            # if v1 == v2:
            #     return v1
            # else:
            #     return v1+ v2

            return aux(a,b,arr,i-1,j) + aux(a,b,arr,i,j-1)

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
    lcs1(a,b)
    print()
    lcs1("abcd", "dcba")
    print()
    lcs1("kannan", "ranganathan")

    lcs1("bdcaba", "abcbdab")
    lcs1("abcbdab", "bdcaba")

    lcs1("abc", "cba")