n = 4
target = 4
book = [3, 4, 5, 6]
def fun():
    # filter out books having pages less than target - 1
    for i in range(n):
        if book[i] < (target-1):
    # checking if (target-book[i]) is in the list 
            if (target - book[i]) in book:
    # if it becomes true then return Yes
                print("Yes")
    # otherwise return No
    print("No")
fun()