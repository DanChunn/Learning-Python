# https://www.hackerrank.com/challenges/python-sort-sort
# Assumes correct inputs

from operator import itemgetter
import sys

first = sys.stdin.readline()
nums = [int(n) for n in first.split()]
N = nums[0] # rows
M = nums[1] # elements per row

listOfRows = []

for i in range (0,N): #reads N rows of M elements
    row = sys.stdin.readline()
    nums = [int(n) for n in row.split()]
    listOfRows.append(nums)

K = int(sys.stdin.readline()) #sort by kth element, 0 indexed

# answer = sorted(listOfRows,key=itemgetter(K)) another way to sort
listOfRows.sort(key=itemgetter(K))

for i in listOfRows:
    print(" ".join(str(e) for e in i))
