
def solution(A, B):
	if B > 0:
		for i in xrange(1, int(B**0.5) + 1):
			if A <= i ** 2 <= B:
				print i**2
				yield i


print len(list(solution(4, 17)))
print len(list(solution(0, 2147483647)))