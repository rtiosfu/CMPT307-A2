#Written by Ryan Tio
#SFU ID: 301380126

import time
import random

def randPart(A, l, r):
	i = random.randint(l, r - 1)
	A[i], A[r] = A[r], A[i]
	return partition(A, l, r)

def partition(A, l, r):
	# print(A)
	piv = A[r]
	# print("piv = ", piv, " l = ", l, " r = ", r)
	i = l - 1
	for j in range(l, r):
		if A[j] <= piv:
			i = i + 1
			# print(i)
			A[i], A[j] = A[j], A[i]

	# print("i after loop =", i)
	A[i + 1], A[r] = A[r], A[i + 1]
	# print(A)

	return i + 1


def insertionSort(A):
	for i in range(1, len(A)):
		j = i
		while j > 0 and A[j] < A[j - 1]:
			A[j], A[j - 1] = A[j - 1], A[j]
			j -= 1


def quickSortMod(A, l, r, k):
	if (l < r) and ((r - l) >= k):
		# print(r - l)
		q = randPart(A, l, r)
		quickSortMod(A, l, q - 1, k)
		quickSortMod(A, q + 1, r, k)


def introSort(A, l, r, k):
	quickSortMod(A, l, r, k)
	insertionSort(A)


#begins with l = 0, r = sizeof(A)
def quickSort(A, l, r):
	# print(A)
	if l < r:
		q = randPart(A, l, r)
		# print("q = ", q)
		# print(A)
		quickSort(A, l, q - 1)
		quickSort(A, q + 1, r)


def generateArr(size):
	arr = [0] * size
	for i in range(0, size):
		arr[i] = i
	random.shuffle(arr)
	# print(arr)
	return arr

def checkSorted(A):
	test = list(A)
	test.sort()
	if (test == A): return True
	else: return False

def testSize(size):
	A = generateArr(size)
	B = list(A)

	print("Testing size = ", size)
	times = []
	for i in range(0, 101):
		startTime = time.perf_counter_ns()
		quickSort(B, 0, len(B) - 1)
		elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
		times.append(elapsedTime)
		if(not checkSorted(B)): print("Sort failed for: ", B)
	print("Average for Quicksort: ", sum(times) / len(times))
	times.clear()
	B = list(A)

	for i in range(0, 101):
		startTime = time.perf_counter_ns()
		introSort(B, 0, len(B) - 1, 100)
		elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
		times.append(elapsedTime)
		if(not checkSorted(B)): print("Sort failed for: ", B)
	print("Average for variant:", sum(times) / len(times), " k = ", 100)
	times.clear()
	B = list(A)

	for i in range(0, 101):
		startTime = time.perf_counter_ns()
		introSort(B, 0, len(B) - 1, 500)
		elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
		times.append(elapsedTime)
		if(not checkSorted(B)): print("Sort failed for: ", B)
	print("Average for variant:", sum(times) / len(times), " k = ", 500)
	times.clear()
	B = list(A)

	for i in range(0, 101):
		startTime = time.perf_counter_ns()
		introSort(B, 0, len(B) - 1, 1000)
		elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
		times.append(elapsedTime)
		if(not checkSorted(B)): print("Sort failed for: ", B)
	print("Average for variant:", sum(times) / len(times), " k = ", 1000)
	times.clear()
	B = list(A)

	for i in range(0, 101):
		startTime = time.perf_counter_ns()
		introSort(B, 0, len(B) - 1, 5000)
		elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
		times.append(elapsedTime)
		if(not checkSorted(B)): print("Sort failed for: ", B)
	print("Average for variant:", sum(times) / len(times), " k = ", 5000)
	times.clear()
	B = list(A)


def main():
	testSize(2**5 * 1000)
	# A = generateArr(100000)
	# introSort(A, 0, len(A) - 1, 100)
	# print(checkSorted(A))
	# print(A)
	# partition(A, 0, len(A) - 1)


main()