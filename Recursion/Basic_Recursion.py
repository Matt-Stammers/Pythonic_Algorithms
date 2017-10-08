# This is an example of a basic recursive program:

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

# It will call itself until the list gets smaller and smaller such that the initial problem is solved.
