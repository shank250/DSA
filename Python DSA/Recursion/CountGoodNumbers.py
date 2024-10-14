

n = str(50)
def countGoodNumbers():
    def isEven(num):
        if num%2 == 0:
            return True
        else:
            return False
    def isPrime(nums):
        div = 0 
        for i in range(1, nums+1):
            if nums%i == 0:
                div += 1
        if div > 2:
            return False
        else:
            return True
    def isGoodNumber(no):    
        for index, num in enumerate(no):
            if isEven(index):
                if isEven(num):
                    pass
                else:
                    return False
            else:
                if isPrime(num):
                    pass
                else:
                    return False
    count = 0
    
    return count

print(countGoodNumbers())
