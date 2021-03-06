# ======================================
#  Function: Factoriztion of a number
# ======================================
def findFactors(num,resultList):
    found = False
    for i in range(2,num):
        if(num % i == 0):
            resultList.append(i)    # A factor found
            num = int(num / i)      # Reduce the number by dividing the factor
            found = True            # Set flag for recursion
            break
    if (found):
        findFactors(num,resultList) # Continue the process until no more factor is found
    else:
        resultList.append(num)      # Append last factor
# ======================================
#  Function: Cell a number is divisible
#            by element in factorList
# ======================================
def checkFactors(num,factorList):
    tempList = list()
    for f in factorList:
        if (num % f == 0):
            tempList.append(f)
    return tempList
# ======================================
#  Function: Calculate product
# ======================================
def product(arr):
    temp = 1
    for i in arr:
        temp = temp * i
    return temp
# ======================================
#  Function: Calculate GCD
# ======================================
def GreatestCommonDivisor(num,arr):
    if 0 in arr:
        return 0
    if 1 in arr:
        return 1
    # Sort arr in asceding order
    arr.sort()
    # 1st element is the smallest
    tempFactorList = list()
    findFactors(arr[0],tempFactorList) # Factorize the 1st element
    for i in range(1,num):
        # Check any factor is present in the rest of the elements
        tempFactorList = checkFactors(arr[i],tempFactorList)
        if not tempFactorList:
            return 1
    return product(tempFactorList)

testList = list()
findFactors(1,testList)
print (testList)
testList = checkFactors(7,testList)
print (testList)
testArr = [21,12,36,48,66]
num = 5
print (GreatestCommonDivisor(num,testArr))