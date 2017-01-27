#https://www.hackerrank.com/challenges/word-order
import collections, sys

dictionary = collections.OrderedDict() #orderedDict remembers order entered
numLine = int(sys.stdin.readline())

for i in range(0,numLine):
    line = sys.stdin.readline()
    if(line in dictionary):
        dictionary[line] += 1
    else:
        dictionary[line] = 1

print(len(dictionary))

print(" ".join(str(e) for e in dictionary.values()))
    
