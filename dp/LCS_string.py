# def LCSS(str1: str, str2: str, strlen1: int, strlen2: int):
# 	ret = []

# 	if str1[-1] == str2[-1]:
# 		return LCSS(str1[:strlen1-1], str2[:strlen2-1], strlen1-1, strlen2-1) + str1[-1]

# 	max(len(LCSS(str1[:strlen-1], str2)), len(LCSS(str1, str2[:strlen2-1]))), 

# 	return ""

# def LCS(A: str, lenA: int, B: str, lenB: int):
# 	if lenA <= 0 or lenB <= 0:
# 		return 0
# 	print("A: " + A[0:lenA])
# 	if A[-1] == B[-1]:
# 		return LCS(A, lenA-1, B, lenB-1) + 1
	
# 	return max(LCS(A, lenA-1, B, lenB), LCS(A, lenA, B, lenB-1))

def LCS(A: str, B: str):
	print("A: " + A + " | B: " + B)
	if len(A) <= 0 or len(B) <= 0:
		return 0

	if A[-1] == B[-1]:
		return LCS(A[0:-1], B[0:-1]) + 1

	return max(LCS(A[0:-1], B), LCS(A, B[0:-1]))


def LCSmemo(A: str, B: str):
	S = set()
	return aux(A, B, S)
	
def aux(A: str, B: str, S: set):
	print("A: " + A + " | B: " + B)
	if len(A) <= 0 or len(B) <= 0:
		return 0

	if A[-1] == B[-1] or A in S or B in S:
		return aux(A[0:-1], B[0:-1], S) + 1

	S.add(A)
	S.add(B)

	return max(aux(A[0:-1], B, S), aux(A, B[0:-1], S))
	


# print(LCSS("ABCADB", "BABDCAB"))
# print(LCSS("ABCAD",  "BABDCA" ) + "B")
# print(LCSS("ABCA ",  "BABDCA" ) + "B")
# print(LCSS("ABCAD",  "BABDC " ) + "B")
A = "ABCADB"
B = "BABDCAB"
# print(LCS(A, len(A), B, len(B)))

# print(LCS(A, B))
print(LCSmemo(A, B))