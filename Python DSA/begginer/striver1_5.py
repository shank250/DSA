# printing my name n time using recursion
num_of_times = 3
iteration = 0
def itsMe(iteration = 0):
    if iteration == num_of_times :
        print("where is the error")
        return
    iteration += 1
    print("its me")
    itsMe(iteration)
itsMe()
# printing from 1 to n using recurssion
N = 5

def see(C = 1):
    if C > N:
        return
    print(C)
    C += 1
    see(C)
see()
# reverse of an array or list
array = [3,4,8,5,58,9,3]
length = len(array)
def printer(ptr = -1):
    print(array[ptr])
    if ptr == (-(length)):
        return
    ptr -= 1
    printer(ptr)
printer()