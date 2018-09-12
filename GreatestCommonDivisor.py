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

testList = list()
findFactors(10000000000,testList)
print (testList)